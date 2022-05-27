from django.contrib import admin
from rimapi import models

# Register your models here.
admin.site.register(models.ApiError, admin.ModelAdmin)