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
        add_equipment_type(equip["type_name"])

    print("after equipment type")
    # opens the location list file, reads in the json object and loops through it to add the locations
    with open('locationlist.txt') as locationfile:
        location = json.load(locationfile)
        for loc in location:
            add_location(loc['building'], loc['room'])
    locationfile.close()
    print("after location")

    with open('equipmentlist.txt') as equipmentfile:
        equipment = json.load(equipmentfile)
        for i in equipment:
            add_equipment(i['serial_no'], i['equipment_model'],
                i['equipment_type'], i['count'], i['manufacturer'],
                i['service_tag'], i['smsu_tag'], i['cpu'], i['optical_drive'],
                i['size'], i['memory'], i['other_connectivity'], i['hard_drive'],
                i['usb_ports'], i['video_card'], i['removable_media'],
                i['physical_address'], i['purchase_price'], i['purchase_info'])
    equipmentfile.close()
    print("after equipment")

    with open('clientlist.txt') as clientfile:
        client = json.load(clientfile)
        for c in client:
            add_client(c['name'], c['bpn'], c['note'])
    clientfile.close()
    print("after client")

    with open('checkoutlist.txt') as checkoutfile:
        checkout = json.load(checkoutfile)
        for check in checkout:
            add_checkout(check['client'], check['timestamp'], check['location'], check['equipment'])
    checkoutfile.close()
    print("after checkouts")

def add_equipment_type(equiptype):
    e = EquipmentType.objects.get_or_create(type_name=equiptype)[0]
    e.save()
    return e

def add_equipment(sn, equipment_model, equipment_type, count, manufacturer,
    service_tag, smsu_tag, cpu, optical_drive, size, memory, other_connectivity,
    hard_drive, usb_ports, video_card, removable_media, physical_address,
    purchase_price, purchase_info):

    e = Equipment.objects.get_or_create(serial_no = sn,
        equipment_model = equipment_model,
        equipment_type = EquipmentType.objects.get(type_name=equipment_type),
        count = count,
        manufacturer = manufacturer,
        service_tag = service_tag,
        smsu_tag = smsu_tag,
        cpu = cpu,
        optical_drive = optical_drive,
        size = size,
        memory = memory,
        other_connectivity = other_connectivity,
        hard_drive = hard_drive,
        usb_ports = usb_ports,
        video_card = video_card,
        removable_media = removable_media,
        physical_address = physical_address,
        purchase_price = purchase_price,
        purchase_info = purchase_info)[0]
    e.save()
    return e

def add_location(building, room):
    L = Location.objects.get_or_create(building = building, room = room)[0]
    L.save()
    return L

def add_client(name, bpn, note):
    c = Client.objects.get_or_create(name = name, bpn = bpn, note = note)[0]
    c.save()
    return c

def add_checkout(client, timestamp, location, equipment):
    c = Checkout.objects.get_or_create(
        client = Client.objects.get(name = client),
        timestamp = timestamp,
        location = Location.objects.get(building = location[0], room = location[1]),
        equipment = Equipment.objects.get(serial_no = equipment))[0]
    c.save()
    return c

if __name__ =='__main__':
    p = cProfile.Profile()
    p.enable()
    print("in main")
    populate()
    p.disable()
    ps = pstats.Stats(p)
    p.print_stats()
    print("Completed")
