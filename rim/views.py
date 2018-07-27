from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView

from rim.models import Equipment
from rim.forms import AddForm

class BaseView(TemplateView):
    template_name = 'rim/base.html'

class AddView(CreateView):
    template_name = 'rim/add.html'
    model = Equipment
    form_class = AddForm
    success_url = reverse_lazy('add')
