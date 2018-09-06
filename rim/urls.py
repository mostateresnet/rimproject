from django.urls import path
from django.conf.urls import url, include

from rim import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('add/', views.AddView.as_view(), name='add'),
    path('group/', views.ListGroupView.as_view(), name='group'),
    path('group/add', views.AddGroupView.as_view(), name='addgroup'),
    path('group/edit/<int:pk>', views.EditGroupView.as_view(), name='editgroup')
]
