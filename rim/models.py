from django.db import models
from django.conf import settings
from django.utils.timezone import now
from django.conf import settings

class Equipment(models.Model):
    serial_no = models.CharField(max_length=100, help_text='Serial No.')
    equipment_model = models.CharField(max_length=30, help_text='Equipment Model')
    equipment_type = models.ForeignKey('EquipmentType', on_delete=models.CASCADE, help_text='Equipment Type')
    count = models.IntegerField(help_text='Count')

    def __str__(self):
        return self.equipment_model

class EquipmentType(models.Model):
    type_name = models.CharField(max_length=30)

    def __str__(self):
        return self.type_name

class Checkout(models.Model):
    client = models.CharField(max_length=50)
    timestamp = models.DateTimeField(default=now, blank=True)
    location = models.ForeignKey('Location', blank=True, null=True, on_delete=models.SET_NULL)
    equipment = models.ForeignKey('Equipment', on_delete=models.CASCADE)

class Location(models.Model):
    building = models.CharField(max_length=50)
    room = models.CharField(max_length=50, blank=True)


class Note(models.Model):
    equipment = models.ForeignKey('Equipment', on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(default=now, blank=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
