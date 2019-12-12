from django.http import HttpRequest
from django.test import TestCase, SimpleTestCase
from django.core.exceptions import ValidationError


# from django.test import Client
from rim.models import Checkout, Client, Equipment, EquipmentType, Location, Note
# from rim.views import CheckoutView, ClientView, HomeView
from django.urls import reverse
from rim import urls
from rim import views
from rim import models

import datetime



class EquipmentModelTests(TestCase):
    def setUpTestData():
        equip_type = EquipmentType.objects.create(type_name = "Tablet")


        Equipment.objects.create(serial_no = "MS2AYMA7JJrD", equipment_model = "BW-20", equipment_type = equip_type, 
            count ="1", manufacturer="Vizio", service_tag="1752217-5", smsu_tag="M88612546-7", cpu="pentiumG45", 
            optical_drive="DVD-RW", size="13.3in", memory="16GB", other_connectivity="Bluetooth Wifi", hard_drive="512GB", 
            usb_ports="2", video_card="Integrated", removable_media="NONE", physical_address="27:B5:2C:02:A8:3D",
            purchase_price="445.98", purchase_info="GovConnections")


    def test_serial_no(self):
        equip = Equipment.objects.get(id=1)
        expected_serial = f'{equip.serial_no}' 
        self.assertEquals(expected_serial, "MS2AYMA7JJrD")
    
    def test_equip_model(self):
        equip = Equipment.objects.get(id=1)
        expected_equip_model = f'{equip.equipment_model}'
        self.assertEquals(expected_equip_model, "BW-20")

    def test_equip_type(self):
        equip = Equipment.objects.get(id=1)
        expected_equip_type = f'{equip.equipment_type}'
        self.assertEquals(expected_equip_type, "Tablet")

    def test_count(self):
        equip = Equipment.objects.get(id=1)
        expected_count = f'{equip.count}'
        self.assertEquals(expected_count, "1")
        
    def test_manufacturer(self):
        equip = Equipment.objects.get(id=1)
        expected_manufacturer = f'{equip.manufacturer}'
        self.assertEquals(expected_manufacturer, "Vizio")
        
    def test_service_tag(self):
        equip = Equipment.objects.get(id=1)
        expected_service_tag = f'{equip.service_tag}'
        self.assertEquals(expected_service_tag, "1752217-5")

    def test_smsu_tag(self):
        equip = Equipment.objects.get(id=1)
        expected_tag = f'{equip.smsu_tag}'
        self.assertEquals(expected_tag, "M88612546-7")

    def test_cpu(self):
        equip = Equipment.objects.get(id=1)
        expected_cpu = f'{equip.cpu}'
        self.assertEquals(expected_cpu, "pentiumG45")

    def test_optical_drive(self):
        equip = Equipment.objects.get(id=1)
        expected_drive = f'{equip.optical_drive}'
        self.assertEquals(expected_drive, "DVD-RW")

    def test_size(self):
        equip = Equipment.objects.get(id=1)
        expected_size = f'{equip.size}'
        self.assertEquals(expected_size, "13.3in")

    def test_memory(self):
        equip = Equipment.objects.get(id=1)
        expected_mem = f'{equip.memory}'
        self.assertEquals(expected_mem, "16GB")

    def test_other_connectivity(self):
        equip = Equipment.objects.get(id=1)
        expected_other_connect = f'{equip.other_connectivity}'
        self.assertEquals(expected_other_connect, "Bluetooth Wifi")

    def test_hard_drive(self):
        equip = Equipment.objects.get(id=1)
        expected_drive = f'{equip.hard_drive}'
        self.assertEquals(expected_drive, "512GB")

    def test_usb_ports(self):
        equip = Equipment.objects.get(id=1)
        expected_usb = f'{equip.usb_ports}'
        self.assertEquals(expected_usb, "2")

    def test_video_card(self):
        equip = Equipment.objects.get(id=1)
        expected_video_card = f'{equip.video_card}'
        self.assertEquals(expected_video_card, "Integrated")

    def test_rm_media(self):
        equip = Equipment.objects.get(id=1)
        expected_rm_media = f'{equip.removable_media}'
        self.assertEquals(expected_rm_media, "NONE")

    def test_physical_address(self):
        equip = Equipment.objects.get(id=1)
        expected_address = f'{equip.physical_address}'
        self.assertEquals(expected_address, "27:B5:2C:02:A8:3D")

    def test_purchase_price(self):
        equip = Equipment.objects.get(id=1)
        expected_pur_price = f'{equip.purchase_price}'
        self.assertEquals(expected_pur_price, "445.98")

    def test_purchase_info(self):
        equip = Equipment.objects.get(id=1)
        expected_pur_info = f'{equip.purchase_info}'
        self.assertEquals(expected_pur_info, "GovConnections")

    def test_str(self):
        equip = Equipment.objects.get(id=1)
        expected_val = f'{equip}'
        expected_serial_no = f'{equip.serial_no}'

        self.assertEquals(expected_val, str(equip))
        self.assertEquals(expected_serial_no, str(equip.serial_no))



class EquipmentTypeModelTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        EquipmentType.objects.create(type_name = "Tablet")

    def test_equip_type(self):
        equip = EquipmentType.objects.get(id=1)
        expected_type= f'{equip.type_name}'
        self.assertEquals(expected_type, "Tablet")
        self.assertEquals(expected_type, str(equip.type_name))


class CheckoutModelTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        client_obj = Client.objects.create(name = "Rodney Brown", bpn = "M99456529", note = "This is a note")
        location_obj = Location.objects.create(building = "Sunvilla", room = "275")
        time_obj = datetime.date(2018,12,28)

        equip_type = EquipmentType.objects.create(type_name = "Tablet")

        equip = Equipment.objects.create(serial_no = "MS2AYMA7JJrD", equipment_model = "BW-20", equipment_type = equip_type, 
            count ="1", manufacturer="Vizio", service_tag="1752217-5", smsu_tag="M88612546-7", cpu="pentiumG45", 
            optical_drive="DVD-RW", size="13.3in", memory="16GB", other_connectivity="Bluetooth Wifi", hard_drive="512GB", 
            usb_ports="2", video_card="Integrated", removable_media="NONE", physical_address="27:B5:2C:02:A8:3D",
            purchase_price="445.98", purchase_info="GovConnections")
        
        
        Checkout.objects.create(client = client_obj , timestamp = time_obj , location = location_obj, equipment = equip)   


    def test_client(self):
        checkout = Checkout.objects.get(id=1)
        expected_client = f'{checkout.client}'
        self.assertEquals(expected_client, "Rodney Brown")

    def test_location(self):
        checkout = Checkout.objects.get(id=1)
        expected_location = f'{checkout.location}'
        self.assertEquals(expected_location, "Sunvilla" + " 275")

    def test_equipment(self):
        checkout = Checkout.objects.get(id=1)
        expected_equip = f'{checkout.equipment}'
        self.assertEquals(expected_equip, "BW-20")


class LocationModelTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        Location.objects.create(building = "Sunvilla", room = "275")

    def test_building_room(self):
        location = Location.objects.get(id=1)
        expected_location_room= f'{location}'
        self.assertEquals(expected_location_room, "Sunvilla 275")
        self.assertEquals(expected_location_room, str(location))


   
class ClientModelTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        Client.objects.create(name = "Rodney Brown", bpn = "M99278791", note = "This is a note")

    def test_client_name(self):
        client = Client.objects.get(id=1)
        expected_client = f'{client.name}' 
        # label = client._meta.get_field('name').verbose_name
        self.assertEquals(expected_client, "Rodney Brown")

    def test_bpn_validator(self):
        client = Client(name = "Rodney Brown", bpn = "M99278791", note = "This is a note")
        client.full_clean()
        client.bpn = "M9900x"
        self.assertRaises(ValidationError, client.full_clean)

    def test_bpn(self):
        client = Client.objects.get(id=1)
        expected_bpn = f'{client.bpn}'
        self.assertEquals(expected_bpn, "M99278791")

    def test_note(self):
        client = Client.objects.get(id=1)
        expected_note = f'{client.note}'
        self.assertEquals(expected_note, "This is a note")

    def test_str(self):
        client = Client.objects.get(id=1)
        expected_client = f'{client}'
        self.assertEquals(expected_client, str(client))


