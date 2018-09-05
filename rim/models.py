from django.db import models
from django.conf import settings
from django.utils.timezone import now
from django.conf import settings

class Equipment(models.Model):
    serial_no = models.CharField(max_length=100, help_text='Serial Number')
    equipment_model = models.CharField(max_length=30, help_text='Equipment Model')
    equipment_type = models.ForeignKey('EquipmentType', on_delete=models.CASCADE, help_text='Equipment Type')
    count = models.IntegerField(blank=True, null=True, help_text='Count')
    manufacturer = models.CharField(max_length=30, blank=True, help_text='Manufacturer')
    service_tag = models.CharField(max_length=30, blank=True, help_text='Service Tag')
    smsu_tag = models.CharField(max_length=30, blank=True, help_text='SMSU Tag')
    cpu = models.CharField(max_length=64, blank=True, help_text='CPU')
    optical_drive = models.CharField(max_length=30, blank=True, help_text='Optical Drive')
    size = models.CharField(max_length=10, blank=True, help_text='Size')
    memory = models.CharField(max_length=10, blank=True, help_text='Memory')
    other_connectivity = models.CharField(max_length=30, blank=True, help_text='Other Connectivity')
    hard_drive = models.CharField(max_length=30, blank=True, help_text='Hard Drive')
    usb_ports = models.IntegerField(blank=True, null=True, help_text='USB Ports')
    video_card = models.CharField(max_length=30, blank=True, help_text='Video Card')
    removable_media = models.CharField(max_length=30, blank=True, help_text='Removable Media')
    physical_address = models.CharField(max_length=30, blank=True, help_text='Physical Adress')
    purchase_price = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, help_text='Purchase Price')
    purchase_info = models.CharField(max_length=100, blank=True, help_text='Purchase Info')
    def latest_checkout(self):
        return self.checkout_set.order_by("-timestamp").first()
    def __str__(self):
        return '%s' % (self.equipment_model)

class EquipmentType(models.Model):
    type_name = models.CharField(max_length=30)
    def __str__(self):
        return '%s' % (self.type_name)

    def __str__(self):
        return self.type_name

class Checkout(models.Model):
    client = models.CharField(max_length=50)
    timestamp = models.DateTimeField(default=now, blank=True)
    location = models.ForeignKey('Location', blank=True, null=True, on_delete=models.SET_NULL)
    equipment = models.ForeignKey('Equipment', on_delete=models.CASCADE)
    def __str__(self):
        return '%s' % (self.client)

class Location(models.Model):
    building = models.CharField(max_length=50)
    room = models.CharField(max_length=50, blank=True)
    def __str__(self):
        return '%s %s' % (self.building, self.room)

class Note(models.Model):
    equipment = models.ForeignKey('Equipment', on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(default=now, blank=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
