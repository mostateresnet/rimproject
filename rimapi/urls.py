from django.urls import path
from django.conf.urls import url, include

from rimapi import views

urlpatterns = [
    path('item/ingest', views.EquipmentCreateOrUpdate.as_view(), name="item_add_or_update"),
    path('error/add', views.AddApiError.as_view(), name="error_add")
]
