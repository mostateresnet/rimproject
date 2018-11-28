import csv

from django.shortcuts import render
from django.urls import reverse_lazy
from django.db.models import Count, Max, Q, F
from django.db.models.functions import Lower
from django.views.generic import CreateView, ListView, UpdateView, DetailView
from django.utils.translation import ugettext_lazy as _
from django.http import HttpResponse
from django.forms.utils import pretty_name
from django.utils.timezone import now, localtime
from rim.models import Equipment, Group, Checkout, EquipmentType, Location, Client
from rim.forms import GroupForm, EquipmentForm, ClientForm

class HomeView(ListView):
    export_csv = False
    template_name = 'rim/home.html'
    queryset = Equipment.objects.select_related('latest_checkout')

    valid_params = ['serial_no', 'equipment_type__type_name', 'group__name', 'equipment_model', 'service_tag',
                    'smsu_tag', 'manufacturer', 'latest_checkout__location__building', 'latest_checkout__location__room']

    def get_ordering(self):
        self.order = self.request.GET.get('order', '-latest_checkout__timestamp')
        if self.order[0] == '-':
            return [Lower(self.order[1:]).desc()]
        else:
            return [Lower(self.order).asc()]

    def get(self, request, *args, **kwargs):
        if self.export_csv:
            keys = ['serial_no', 'equipment_model', 'manufacturer', 'equipment_type__type_name', 'latest_checkout__location__building', 'latest_checkout__location__room']
            verbose_keys = []
            for key in keys:
                split_key = key.split('__')
                field = Equipment._meta.get_field(split_key[0])
                while True:
                    if len(split_key) > 1:
                        field = field.remote_field.model._meta.get_field(split_key[1])
                        split_key = split_key[1:]
                    else:
                        verbose_keys.append(pretty_name(field.verbose_name))
                        break

            equipment_list = self.get_queryset().values(*keys)
            current_time = localtime(now()).strftime("%Y-%m-%d-%I%M")
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="RIMreport_' + current_time + '.csv"'

            writer = csv.DictWriter(response, fieldnames=keys)
            writer.writerow(dict(zip(keys, verbose_keys)))

            for equipment in equipment_list:
                writer.writerow(equipment)
            return response
        else:
            return super().get(request, *args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context['current_order_desc'] = self.order[0] == '-'
        context['current_ordering_name'] = self.order[1:] if context['current_order_desc'] else self.order
        context['equipment_types'] = EquipmentType.objects.all()
        context['groups'] = Group.objects.all()
        context['buildings'] = Location.objects.values('building').distinct().order_by('building').values_list('building', flat=True)

        data = self.request.GET.copy()
        for k, v in self.request.GET.items():
            if k not in self.valid_params or not v:
                del data[k]

        context['search_data'] = data

        return context

    def get_queryset(self):
        qset = super(HomeView, self).get_queryset()

        for item, value in self.request.GET.items():
            if item in self.valid_params:
                if value != '':
                    qset = qset.filter(**{item + '__icontains': value})

        qset = qset.select_related('latest_checkout__location', 'equipment_type')
        return qset

class ListClientView(ListView):
    template_name = 'rim/client_list.html'
    model = Client
    form_class = ClientForm

    def get_queryset(self):
        queryset = super(ListClientView, self).get_queryset()
        query = self.request.GET.get('search', '')
        queryset = Client.objects.filter(Q(name__contains=query)|Q(bpn__iexact=query)).annotate(equipment_count=Count('checkout', filter=Q(checkout__equipment__latest_checkout__pk=F("checkout__pk"))))
        return queryset

    def get_context_data(self):
        context = super(ListClientView, self).get_context_data()
        query = self.request.GET.get('search', '')
        context['searchterm'] = query
        return context

class ListGroupView(ListView):
    template_name = 'rim/group.html'
    model = Group

    def get_queryset(self):
        return super().get_queryset().annotate(equipment_count=Count('equipment'))

class AddGroupView(CreateView):
    template_name = 'rim/edit_group.html'
    model = Group
    form_class = GroupForm
    success_url = reverse_lazy('group')

    def get_context_data(self):
        context = super(AddGroupView, self).get_context_data()
        context["group_title"] = _("Add A Group")
        return context

class EditGroupView(UpdateView):
    template_name = 'rim/edit_group.html'
    model = Group
    form_class = GroupForm
    success_url = reverse_lazy('group')

    def get_context_data(self):
        context = super(EditGroupView, self).get_context_data()
        context["group_title"] = _("Edit Group")
        context['equipments'] = Equipment.objects.filter(group_id=self.kwargs['pk'])

        return context

class AddEquipmentView(CreateView):
    template_name = 'rim/edit.html'
    model = Equipment
    form_class = EquipmentForm
    success_url = reverse_lazy('home')

class EditEquipmentView(UpdateView):
    template_name = 'rim/edit.html'
    model = Equipment
    form_class = EquipmentForm
    success_url = reverse_lazy('home')

class ClientView(DetailView):
    template_name = 'rim/client.html'
    model = Client

    def get_context_data(self, *args, **kwargs):
        context = super(ClientView, self).get_context_data(*args, **kwargs)
        context['active'] = Client.objects.get(pk=self.kwargs['pk']).checkout_set.filter(equipment__latest_checkout__pk=F('pk'))
        context['previous'] = Client.objects.get(pk=self.kwargs['pk']).checkout_set.exclude(equipment__latest_checkout__pk=F('pk'))
        return context
