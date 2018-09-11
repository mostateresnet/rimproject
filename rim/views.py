from django.shortcuts import render
from django.urls import reverse_lazy
from django.db.models import Count
from django.views.generic import CreateView, ListView, UpdateView
from django.utils.translation import ugettext_lazy as _
from rim.models import Equipment, Group
from rim.forms import GroupForm, EquipmentForm

class HomeView(ListView):
    template_name = 'rim/home.html'
    def get_queryset(self):
        return Equipment.objects.all()

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
