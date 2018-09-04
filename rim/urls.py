from django.urls import path

from rim import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('add/', views.AddView.as_view(), name='add'),
]
