import csv

from django.shortcuts import render
from django.urls import reverse_lazy
from django.core.paginator import Paginator
from django.db.models import Count, Max, Q, F
from django.db.models.functions import Lower
from django.views.generic import CreateView, ListView, UpdateView, DetailView
from django.utils.translation import ugettext_lazy as _
from django.http import HttpResponse
from django.forms.utils import pretty_name
from django.utils.timezone import now, localtime
from rim.models import Equipment, Checkout, EquipmentType, Location, Client
from rim.forms import EquipmentForm

class PaginateView(object):
    def get_paginate_by(self, queryset):
        self.invalid_per_page = False
        obj_per_page = 15
        try:
            obj_per_page = int(self.request.COOKIES['paginate'])
        except ValueError:
            self.invalid_per_page = True
        except KeyError:
            pass
        obj_per_page = min(obj_per_page, 1000)
        obj_per_page = max(obj_per_page, 1)
        return obj_per_page

    def dispatch(self, *args, **kwargs):
        response = super().dispatch(*args, **kwargs)
        if(self.invalid_per_page):
            response.delete_cookie('paginate')
        return response


class HomeView(PaginateView, ListView):
    export_csv = False
    template_name = 'rim/home.html'
    queryset = Equipment.objects.select_related('latest_checkout')

    valid_params = ['serial_no', 'equipment_type__type_name', 'latest_checkout__client__name', 'equipment_model', 'service_tag',
                    'smsu_tag', 'manufacturer', 'latest_checkout__location__building', 'latest_checkout__location__room']


    def get_ordering(self):
        self.order = self.request.GET.get('order', '-latest_checkout__timestamp')
        if self.order[0] == '-':
            return [Lower(self.order[1:]).desc()]
        else:
            return [Lower(self.order).asc()]

    def get(self, request, *args, **kwargs):
        if self.export_csv:
            keys = ['serial_no', 'equipment_model', 'manufacturer',
                    'equipment_type__type_name', 'latest_checkout__client__name',
                    'latest_checkout__client__bpn', 'latest_checkout__location__building', 'latest_checkout__location__room']
            verbose_keys = []
            for key in keys:
                split_key = key.split('__')
                field = Equipment._meta.get_field(split_key[0])
                while True:
                    if len(split_key) > 1:
                        field = field.remote_field.model._meta.get_field(split_key[1])
                        split_key = split_key[1:]
                    else:
                        verbose_keys.append(field._verbose_name or pretty_name(field.verbose_name))
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

class ListClientView(PaginateView, ListView):
    template_name = 'rim/client_list.html'
    model = Client


    def get_queryset(self):
        query = self.request.GET.get('search', '')
        queryset = Client.objects.filter(Q(name__icontains=query) | Q(bpn__iexact=query)).annotate(equipment_count=Count('checkout', filter=Q(checkout__equipment__latest_checkout__pk=F("checkout__pk"))))
        return queryset

    def get_context_data(self, *args, **kwargs):
        context = super(ListClientView, self).get_context_data(*args, **kwargs)
        query = self.request.GET.get('search', '')
        context['searchterm'] = query
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
        context['active'] = context['client'].checkout_set.filter(equipment__latest_checkout__pk=F('pk'))
        context['previous'] = context['client'].checkout_set.exclude(equipment__latest_checkout__pk=F('pk'))
        return context
