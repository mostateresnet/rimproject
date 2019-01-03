"""
author: Tim McCoy
purpose: Generate checkout list for test data from files of buildings and rooms
restrictions:
"""

import json
import random
import pytz
from datetime import datetime
from random import shuffle

"""
need to get the:
    client name from clientlist.txt
    location building and room from locationlist.txt
    equipment serial_no from equipmentlist.txt
    create timestamp
"""

def CheckoutCreator():

    # clientlist = []
    # with open('clientlist.txt') as clientfile:
    #     client = json.load(clientfile)
    #     for c in client:
    #         checkoutlist.append(c['name'])
    # clientfile.close()
    # print("clientlist: ", clientlist)

    # get file names
    clientlist = "clientlist.txt"
    locationlist = "locationlist.txt"
    equipmentlist = "equipmentlist.txt"
    checkoutlist = "checkoutlist.txt"

    # open the files to read and write from/to
    clientf = open(clientlist, 'r')
    locationf = open(locationlist, 'r')
    equipmentf = open(equipmentlist, 'r')
    savef = open(checkoutlist, 'w')

    # create the lists to hold the variables
    clients = []  # grab the names of clients
    locations = []  # grab the building and room
    equipments = []  # grab the serialnumber
    checkoutlist = []  # stores all the dictonary rows to be placed in the file

    # grab the individual elements needed from the different files
    client = json.load(clientf)
    for c in client:
        clients.append(c['name'])

    location = json.load(locationf)
    for loc in location:
        locations.append([loc['building'],loc['room']])
    shuffle(locations)  # This will allow us to get a random shuffled list of locations so we don't have all the same buildings
    # print("locations", locations)

    equipment = json.load(equipmentf)
    for  e in equipment:
        equipments.append(e['serial_no'])

    # runs through and appends all the different lists to the main checkoutlist
    for i in range(300):
        random.seed(datetime.now())
        checkoutdict = {'client':clients[i],
        'timestamp':"%04d-%02d-%02d %02d:%02d:%02d+06:00"%(random.randint(2010,2018),
            random.randint(1,12),
            random.randint(1,28),
            random.randint(0,23),
            random.randint(0,59),
            random.randint(0,59)),
        'location':locations[i], 'equipment':equipments[i]}
        checkoutlist.append(checkoutdict)

    # save the list to the file
    savef.write(json.dumps(checkoutlist))

    # close all the files that were opened
    clientf.close()
    locationf.close()
    equipmentf.close()
    savef.close()


if __name__ == '__main__':
    print("starting")
    CheckoutCreator()
    print("Complete")
