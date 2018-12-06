from django.urls import path
from django.conf.urls import url, include

from rim import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('export', views.HomeView.as_view(export_csv=True), name='export'),
    path('add/', views.AddEquipmentView.as_view(), name='add'),
    path('edit/<int:pk>', views.EditEquipmentView.as_view(), name='edit'),
    path('group/', views.ListGroupView.as_view(), name='group'),
    path('group/add', views.AddGroupView.as_view(), name='addgroup'),
    path('group/edit/<int:pk>', views.EditGroupView.as_view(), name='editgroup'),
    path('client/<int:pk>', views.ClientView.as_view(), name='client'),
    path('client/', views.ListClientView.as_view(), name='client_list'),
]
