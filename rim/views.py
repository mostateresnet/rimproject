from django.shortcuts import render
from django.views.generic import ListView
from rim.models import Equipment


class HomeView(ListView):
	template_name='rim/home.html'
	def get_queryset(self):
		return Equipment.objects.all()
