from django.urls import path
from django.conf.urls import url, include

from rim import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('export', views.HomeView.as_view(export_csv=True), name='export'),
    path('add/', views.AddEquipmentView.as_view(), name='add'),
    path('edit/<int:pk>', views.EditEquipmentView.as_view(), name='edit'),
    path('client/<int:pk>', views.ClientView.as_view(), name='client'),
    path('client/', views.ListClientView.as_view(), name='client_list'),
    path('check_serial_nums/', views.CheckSerialView.as_view(), name='check_serial_nums'),
]
