from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView

from rim.models import Group
from rim.forms import GroupForm

class BaseView(TemplateView):
    template_name='rim/base.html'

class GroupView(CreateView):
    template_name='rim/group.html'
    model = Group
    form_class = GroupForm
    success_url = reverse_lazy('group')
