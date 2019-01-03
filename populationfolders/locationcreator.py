"""
author: Tim McCoy
purpose: Generate location list for test data from files of buildings and rooms
restrictions:
"""

import json
import random
from datetime import datetime

def LocationCreator():

    #open the file to save the list
    savef = open('locationlist.txt', 'w')

    # create list to hold names, numbers, and client list
    buildings = ["Blair", "Shannon", "Freudenberger", "Hammons", "Hutchens", "Kentwood", "Scholars", "Wells", "Woods", "Monroe", "Sunvilla"]
    nums = []
    locationlist = []

    # add the name to the name and number list
    for i in range(100):
        random.seed(datetime.now())
        nums.append(random.randint(100,500))
    # print("numbers: ", nums)

    # get length of the name list
    looplen = len(nums)

    # create the dictionary to hold the locations
    for j in range(len(buildings)):
        for i in range(looplen):
            locationdict = {'building':buildings[j], 'room':nums[i]}
            locationlist.append(locationdict)
    # print("location list: ", locationlist)

    # write the list to the file using json dumps
    savef.write(json.dumps(locationlist))

    #close the file
    savef.close()

if __name__ == '__main__':
    print("Starting")
    LocationCreator()
    print("Complete")
