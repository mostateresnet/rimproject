from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, ListView
from rim.models import Equipment
from rim.forms import AddForm

class HomeView(ListView):
    template_name = 'rim/home.html'
    def get_queryset(self):
        return Equipment.objects.all()

class AddView(CreateView):
    template_name = 'rim/add.html'
    model = Equipment
    form_class = AddForm
    success_url = reverse_lazy('home')
