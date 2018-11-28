from django.contrib import admin

from rim import models

class CheckoutInline(admin.TabularInline):
    model = models.Checkout
    extra = 1
    autocomplete_fields = ['location']

class EquipmentAdmin(admin.ModelAdmin):
    list_display = ['serial_no', 'equipment_type', 'manufacturer', 'equipment_model', 'count']
    search_fields = ['service_tag', 'smsu_tag', 'serial_no', 'equipment_model', 'equipment_type__type_name', 'manufacturer']
    inlines = [CheckoutInline]

class EquipmentTypeAdmin(admin.ModelAdmin):
    list_display = ['type_name']
    search_fields = ['type_name']

class LocationAdmin(admin.ModelAdmin):
    list_display = ['building', 'room']
    search_fields = ['building', 'room']

class CheckoutAdmin(admin.ModelAdmin):
    list_display = ['equipment', 'location', 'client', 'timestamp']
    search_fields = ['equipment__equipment_model', 'location__building', 'location__room', 'client']
    autocomplete_fields = ['location', 'equipment']
    list_filter = ['timestamp']


class NoteAdmin(admin.ModelAdmin):
    list_display = ['equipment', 'content', 'author', 'timestamp']
    search_fields = ['equipment__equipment_model', 'content', 'author__username', 'author__first_name', 'author__last_name']
    list_filter = ['timestamp']

admin.site.register(models.Equipment, EquipmentAdmin)
admin.site.register(models.EquipmentType, EquipmentTypeAdmin)
admin.site.register(models.Checkout, CheckoutAdmin)
admin.site.register(models.Location, LocationAdmin)
admin.site.register(models.Note, NoteAdmin)
admin.site.register(models.Client)
admin.site.register(models.Group)
