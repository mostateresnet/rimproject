"""
author: Tim McCoy
purpose: Generate location list for test data from files of buildings and rooms
restrictions:
"""

import json
import random
from datetime import datetime


def LocationCreator():

    # open the file to save the list
    savef = open('locationlist.txt', 'w')

    # create list to hold names, numbers, and client list
    buildings = ["Blair", "Shannon", "Freudenberger", "Hammons", "Hutchens", "Kentwood", "Scholars", "Wells", "Woods", "Monroe", "Sunvilla"]
    nums = set()
    locationlist = []
    i = 0

    # add the name to the name and number list
    while (i < 100):
        random.seed(datetime.now())
        nums.add(random.randint(100, 700))
        i = i + 1

    # create the dictionary to hold the locations
    for j in range(len(buildings)):
        for num in nums:
            # print("nums ", num)
            locationdict = {'building': buildings[j], 'room': num}
            locationlist.append(locationdict)
    print("location list: ", nums)

    # write the list to the file using json dumps
    savef.write(json.dumps(locationlist))

    # close the file
    savef.close()


if __name__ == '__main__':
    print("Starting")
    LocationCreator()
    print("Complete")
