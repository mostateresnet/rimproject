from django.urls import path

from rim import views

urlpatterns = [
    path('', views.BaseView.as_view(), name='base'),
]
