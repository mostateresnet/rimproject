from django.shortcuts import render
from django.urls import reverse_lazy
from django.db.models import Count, Max
from django.db.models.functions import Lower
from django.views.generic import CreateView, ListView, UpdateView
from django.utils.translation import ugettext_lazy as _
from rim.models import Equipment, Group, Checkout, EquipmentType, Location
from rim.forms import GroupForm, EquipmentForm

class HomeView(ListView):
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

    def get_context_data(self):
        context = super(HomeView, self).get_context_data()
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

        return qset


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
