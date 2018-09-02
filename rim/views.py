from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, ListView, UpdateView
from rim.models import Equipment

from rim.models import Group
from rim.forms import GroupForm

class HomeView(ListView):
    template_name = 'rim/home.html'
    def get_queryset(self):
        return Equipment.objects.all()

class ListGroupView(ListView):
    template_name='rim/group.html'
    model = Group

    def get_queryset(self):
        qset = super(ListGroupView, self).get_queryset()
        qset = Group.objects.all()
        return qset

class AddGroupView(CreateView):
    template_name='rim/add_group.html'
    model = Group
    form_class = GroupForm
    success_url = reverse_lazy('group')

class EditGroupView(UpdateView):
    template_name='rim/edit_group.html'
    model = Group
    form_class = GroupForm
    success_url = reverse_lazy('group')
