"""
author: Tim McCoy
purpose: Generate equipment list for test data from files of equipment stuff
restrictions: all equipment section files need to be the same length
"""
import json
import random
from datetime import datetime


def EquipmentCreator():

    #file names of files to read
    serialfile = "300_unique_codes.txt"
    modelfile = "modelnames.txt"
    manufacturerfile = "manufacturer.txt"
    servicetagfile = 'servicetag.txt'
    smsufile = 'smsutag.txt'
    physicaladdrssfile = 'physicaladdress.txt'
    purchasepricefile = 'purchaseprice.txt'

    #open the files
    serialf = open(serialfile, 'r')
    modelf = open(modelfile, 'r')
    manf = open(manufacturerfile, 'r')
    servtagf = open(servicetagfile, 'r')
    smsutagf = open(smsufile, 'r')
    physicalf = open(physicaladdrssfile, 'r')
    purchasef = open(purchasepricefile, 'r')
    savef = open('equipmentlist.txt', 'w')

    # create lists to hold the various sections of the equipment dict.
    serials = []
    models = []
    types = ["Desktop", "Laptop", "Tablet"]
    count = 1
    manufacturers = []
    servicetags = []
    smsutag = []
    cpu = ["i9", "i7", "i5", "i3", "ryzen7", "ryzen5", "ryzen3", "pentiumG45", "athlon36", "IBM2030"]
    opticaldrive = ["NONE", "DVD-RW"]
    sizes = ["11.8in", "13.3in", "15.6in"]
    memory = ["4GB", "8GB", "16GB"]
    otherconn = ["Bluetooth Wifi", "Wifi"]
    harddrives = ["128GB", "256GB", "512GB"]
    usbports = [2, 4, 8]
    videocards = ["Integrated", "1050", "1070"]
    removablemedia = ["NONE", "SD"]
    physicaladdress = []
    purchaseprice = []
    purchaseinfo = ["Bookstore", "GovConnections", "Computer Services"]
    equipmentlist = []

    # section to create the lists to populate the individual dictionary rows
    for serial in serialf:
        serial = serial.rstrip('\"\r\n')
        serial = serial.lstrip('\"')
        serials.append(serial)

    for model in modelf:
        model = model.rstrip()
        models.append(model)

    for manufacturer in manf:
        manufacturer = manufacturer.rstrip()
        manufacturers.append(manufacturer)

    for servicetag in servtagf:
        servicetag = servicetag.rstrip()
        servicetags.append(servicetag+"-"+str(random.randint(0,9)))

    for smsut in smsutagf:
        smsut = smsut.rstrip()
        smsutag.append("M"+smsut+"-"+str(random.randint(0,9)))

    for mac in physicalf:
        mac = mac.rstrip()
        physicaladdress.append(mac)

    for pp in purchasef:
        pp = pp[:6]
        purchaseprice.append(pp)

    # get the length for the for loop to loop through
    looplen = len(serials)

    # create the dictionary rows in the equipmentlist
    for i in range(looplen):
        equipdict = {
            "serial_no":serials[i],
            'equipment_model':models[i],
            'equipment_type':types[random.randint(0,2)],
            'count':count,
            'manufacturer':manufacturers[i],
            'service_tag':servicetags[i],
            'smsu_tag':smsutag[i],
            'cpu':cpu[random.randint(0,9)],
            'optical_drive':opticaldrive[random.randint(0,1)],
            'size':sizes[random.randint(0,2)],
            'memory':memory[random.randint(0,2)],
            'other_connectivity':otherconn[random.randint(0,1)],
            'hard_drive':harddrives[random.randint(0,2)],
            'usb_ports':usbports[random.randint(0,2)],
            'video_card':videocards[random.randint(0,2)],
            'removable_media':removablemedia[random.randint(0,1)],
            'physical_address':physicaladdress[i],
            'purchase_price':purchaseprice[i],
            'purchase_info':purchaseinfo[random.randint(0,2)]
        }
        equipmentlist.append(equipdict)
    print("equipmentlist: ", equipmentlist)

    # write the list to the file using json dumps
    savef.write(json.dumps(equipmentlist))

    #close the files
    serialf.close()
    modelf.close()
    manf.close()
    servtagf.close()
    smsutagf.close()
    physicalf.close()
    purchasef.close()
    savef.close()

if __name__ == '__main__':
    random.seed(datetime.now())
    print("Starting")
    EquipmentCreator()
    print("Complete")
