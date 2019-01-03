import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rimproject.settings')

import json
import datetime
import pytz
import django
import cProfile
import pstats
django.setup()
from rim.models import Equipment, Checkout, EquipmentType, Location, Client

def populate():
    equipment_type = [
        {'type_name':'Laptop'},
        {'type_name':'Tablet'},
        {'type_name':'Desktop'}
    ]

    for equip in equipment_type:
        # TODO make bulk create
        EquipmentType.objects.get_or_create(type_name=equip['type_name'])

    print("after equipment type")
    # opens the location list file, reads in the json object and loops through it to add the locations
    with open('locationlist.txt') as locationfile:
        location = json.load(locationfile)
        location_objects = []
        for loc in location:
            location_object = Location(building = loc['building'], room = loc['room'])
            location_objects.append(location_object)
        Location.objects.bulk_create(location_objects)
    print("after location")

    with open('equipmentlist.txt') as equipmentfile:
        equipment = json.load(equipmentfile)
        equipment_objects = []
        for i in equipment:
            equipment_object = Equipment(
                serial_no = i['serial_no'],
                equipment_model = i['equipment_model'],
                # TODO make all of these get requests at once
                equipment_type = EquipmentType.objects.get(type_name=i['equipment_type']),
                count = i['count'],
                manufacturer = i['manufacturer'],
                service_tag = i['service_tag'],
                smsu_tag = i['smsu_tag'],
                cpu = i['cpu'],
                optical_drive = i['optical_drive'],
                size = i['size'],
                memory = i['memory'],
                other_connectivity = i['other_connectivity'],
                hard_drive = i['hard_drive'],
                usb_ports = i['usb_ports'],
                video_card = i['video_card'],
                removable_media = i['removable_media'],
                physical_address = i['physical_address'],
                purchase_price = i['purchase_price'],
                purchase_info = i['purchase_info']
            )
            equipment_objects.append(equipment_object)
        Equipment.objects.bulk_create(equipment_objects)
    print("after equipment")

    with open('clientlist.txt') as clientfile:
        client = json.load(clientfile)
        client_objects = []
        for c in client:
            client_object = Client(name = c['name'], bpn = c['bpn'], note = c['note'])
            client_objects.append(client_object)
        Client.objects.bulk_create(client_objects)
    print("after client")

    with open('checkoutlist.txt') as checkoutfile:
        checkout = json.load(checkoutfile)
        checkoutfile_objects = []
        for check in checkout:
            # TODO fetch all of these at once and remove duplicates
            checkout_location = Location.objects.filter(building = check['location'][0], room = check['location'][1])[0]
            checkout_object = Checkout(
                # TODO fetch all at once
                client = Client.objects.get(name=check['client']),
                timestamp = check['timestamp'],
                location = checkout_location,
                # TODO fetch all at once
                equipment = Equipment.objects.get(serial_no = check['equipment'])
            )
            checkoutfile_objects.append(checkout_object)
        Checkout.objects.bulk_create(checkoutfile_objects)
    print("after checkouts")

if __name__ =='__main__':
    p = cProfile.Profile()
    p.enable()
    print("in main")
    populate()
    p.disable()
    ps = pstats.Stats(p)
    p.print_stats()
    print("Completed")
