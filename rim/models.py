from django.db import models
from django.conf import settings
from django.utils.timezone import now
from django.conf import settings
from django.core.validators import RegexValidator, MinValueValidator
from django.utils.translation import ugettext_lazy as _

class Equipment(models.Model):
    serial_no = models.CharField(max_length=100, verbose_name='Serial number', unique=True)
    hostname = models.CharField(max_length=100, blank=True)
    equipment_model = models.CharField(max_length=30)
    equipment_type = models.ForeignKey('EquipmentType', on_delete=models.CASCADE, blank=True, null=True)
    count = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(0)])
    manufacturer = models.CharField(max_length=30, blank=True)
    service_tag = models.CharField(max_length=30, blank=True)
    smsu_tag = models.CharField(max_length=30, blank=True, verbose_name='SMSU tag')
    cpu = models.CharField(max_length=64, blank=True, verbose_name='CPU')
    optical_drive = models.CharField(max_length=30, blank=True)
    size = models.CharField(max_length=10, blank=True)
    memory = models.CharField(max_length=10, blank=True)
    other_connectivity = models.CharField(max_length=30, blank=True)
    storage = models.JSONField(blank=True, default=list)
    usb_ports = models.IntegerField(blank=True, null=True, verbose_name='USB ports', validators=[MinValueValidator(0)])
    GPU = models.JSONField(blank=True, default=list)
    network_cards = models.JSONField(blank=True, default=list)
    displays = models.JSONField(blank=True, default=list)
    users_info = models.JSONField(blank=True, default=list)
    removable_media = models.CharField(max_length=30, blank=True)
    mac_address = models.CharField(max_length=30, blank=True, verbose_name='MAC address')
    purchase_price = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True, validators=[MinValueValidator(0)])
    purchase_info = models.CharField(max_length=100, blank=True)
    latest_checkout = models.ForeignKey('Checkout', blank=True, null=True, on_delete=models.SET_NULL, related_name='+')

    def __str__(self):
        return '%s' % (self.equipment_model)

class EquipmentType(models.Model):
    type_name = models.CharField(max_length=30, verbose_name='Equipment Type',)

    def __str__(self):
        return '%s' % (self.type_name)

class Checkout(models.Model):
    client = models.ForeignKey('Client', on_delete=models.CASCADE)
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


class Client(models.Model):
    name = models.CharField(max_length=50, verbose_name='Client Name')
    bpn_validator = RegexValidator(r'[mM8]\d{8}', _("Bearpass number must start with an 'M,' 'm,' or '8,' and followed by eight digits."))
    bpn = models.CharField(max_length=9, validators=[bpn_validator], blank=True, verbose_name='Client M-number')
    note = models.TextField(blank=True)

    def __str__(self):
        return '%s' % (self.name)
