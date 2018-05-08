from django.db import models
from django.utils.timezone import now

class Equipment(models.Model):
    serial_no = models.CharField(max_length=15)
    equipment_model = models.CharField()
    equipment_type = models.ForeignKey(EquipmentType)
    count = models.IntegerField()

class EquipmentType(models.Model):
    type_name = models.charField(max_length=30)

class Checkout(models.Model):
    client = models.CharField(max_length=50)
    timestamp = models.DateTimeField(default=now)
    returned_timestamp = models.DateTimeField(null=True)
    location = models.ForeignKey(Location)
    comment = models.TextField()
    equipment = models.ForeignKey(Equipment)

class Location(models.Model):
    building = models.CharField(max_length=50)
    room = models.CharField(max_length=50, blank=True)

class Note(models.Model):
