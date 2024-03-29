from django.core.management.base import BaseCommand
from rim.models import Equipment, Checkout, EquipmentType, Location, Client
import json

class Command(BaseCommand):

    help = 'Populates the database with test data to use'

    def handle(self, *args, **options):
        self.stdout.write("starting")
        equipment_type = [
            {'type_name': 'Laptop'},
            {'type_name': 'Tablet'},
            {'type_name': 'Desktop'}
        ]
        equiptype_objects = []
        for equip in equipment_type:
            equiptype_object = EquipmentType(type_name=equip['type_name'])
            equiptype_objects.append(equiptype_object)
        EquipmentType.objects.bulk_create(equiptype_objects)

        with open('populationfolders/locationlist.txt') as locationfile:
            location = json.load(locationfile)
            location_objects = []
            for loc in location:
                location_object = Location(building=loc['building'], room=loc['room'])
                location_objects.append(location_object)
            Location.objects.bulk_create(location_objects)

        with open('populationfolders/equipmentlist.txt') as equipmentfile:
            equipment = json.load(equipmentfile)
            equipment_objects = []
            equiptype = EquipmentType.objects.all()
            for i in equipment:
                et = equiptype.filter(type_name=i['equipment_type'])[0]
                equipment_object = Equipment(
                    serial_no=i['serial_no'],
                    equipment_model=i['equipment_model'],
                    equipment_type=et,
                    count=i['count'],
                    manufacturer=i['manufacturer'],
                    service_tag=i['service_tag'],
                    smsu_tag=i['smsu_tag'],
                    cpu=i['cpu'],
                    optical_drive=i['optical_drive'],
                    size=i['size'],
                    memory=i['memory'],
                    other_connectivity=i['other_connectivity'],
                    storage= [{'Model': '', 'Size': i['hard_drive']}],
                    usb_ports=i['usb_ports'],
                    GPU=[{'Name': i['video_card']}],
                    removable_media=i['removable_media'],
                    mac_address=i['mac_address'],
                    purchase_price=i['purchase_price'],
                    purchase_info=i['purchase_info']
                )
                equipment_objects.append(equipment_object)
            Equipment.objects.bulk_create(equipment_objects)

        with open('populationfolders/clientlist.txt') as clientfile:
            client = json.load(clientfile)
            client_objects = []
            for c in client:
                client_object = Client(name=c['name'], bpn=c['bpn'], note=c['note'])
                client_objects.append(client_object)
            Client.objects.bulk_create(client_objects)

        with open('populationfolders/checkoutlist.txt') as checkoutfile:
            checkout = json.load(checkoutfile)
            for check in checkout:
                checkout_object = Checkout.objects.get_or_create(
                    client=Client.objects.get(name=check['client']),
                    timestamp=check['timestamp'],
                    location=Location.objects.get(building=check['location'][0], room=check['location'][1]),
                    equipment=Equipment.objects.get(serial_no=check['equipment']))[0]
                checkout_object.save()
        self.stdout.write("completed")
