from django.urls import path
from django.conf.urls import url, include

from rim import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
]
