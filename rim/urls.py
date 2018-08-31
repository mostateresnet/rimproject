from django.urls import path

from rim import views

urlpatterns = [
    path('', views.BaseView.as_view(), name='base'),
    path('group/', views.ListGroupView.as_view(), name='group'),
    path('group/add', views.AddGroupView.as_view(), name='addgroup'),
    path('group/edit/<int:pk>', views.EditGroupView.as_view(), name='editgroup')
]
