from django.db import models
from django.conf import settings
from django.utils.timezone import now
from django.conf import settings

class Equipment(models.Model):
    serial_no = models.CharField(max_length=100, verbose_name='Serial Number')
    equipment_model = models.CharField(max_length=30)
    group = models.ForeignKey('Group', blank=True, null=True, on_delete=models.SET_NULL)
    equipment_type = models.ForeignKey('EquipmentType', on_delete=models.CASCADE)
    count = models.IntegerField(blank=True, null=True)
    manufacturer = models.CharField(max_length=30, blank=True)
    service_tag = models.CharField(max_length=30, blank=True)
    smsu_tag = models.CharField(max_length=30, blank=True, verbose_name='SMSU Tag')
    cpu = models.CharField(max_length=64, blank=True, verbose_name='CPU')
    optical_drive = models.CharField(max_length=30, blank=True)
    size = models.CharField(max_length=10, blank=True)
    memory = models.CharField(max_length=10, blank=True)
    other_connectivity = models.CharField(max_length=30, blank=True)
    hard_drive = models.CharField(max_length=30, blank=True)
    usb_ports = models.IntegerField(blank=True, null=True, verbose_name='USB Ports')
    video_card = models.CharField(max_length=30, blank=True)
    removable_media = models.CharField(max_length=30, blank=True)
    physical_address = models.CharField(max_length=30, blank=True)
    purchase_price = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    purchase_info = models.CharField(max_length=100, blank=True)
    latest_checkout = models.ForeignKey('Checkout', blank=True, null=True, on_delete=models.SET_NULL, related_name='+')

    def __str__(self):
        return '%s' % (self.equipment_model)

class EquipmentType(models.Model):
    type_name = models.CharField(max_length=30)

    def __str__(self):
        return '%s' % (self.type_name)

class Checkout(models.Model):
    client = models.CharField(max_length=50)
    timestamp = models.DateTimeField(default=now, blank=True)
    location = models.ForeignKey('Location', blank=True, null=True, on_delete=models.SET_NULL)
    equipment = models.ForeignKey('Equipment', on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        latest_checkout_qs = models.Subquery(Checkout.objects.filter(equipment_id=self.equipment_id).order_by('-timestamp')[:1].values('pk'))
        Equipment.objects.filter(pk=self.equipment_id).update(latest_checkout=latest_checkout_qs)

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

class Group(models.Model):
    name = models.CharField(max_length=50)
    note = models.TextField()

    def __str__(self):
        return '%s' % (self.name)
