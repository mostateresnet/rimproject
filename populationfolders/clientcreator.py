"""
author: Tim McCoy
purpose: Generate client list for test data from files of names and numbers
restrictions: name and number files need to be the same length
"""
import json


def ClientCreator():
    # file names of the client names and the numbers for bpn
    namelist = 'namelist300.txt'
    numlist = 'numberlist300.txt'

    # open the files
    namef = open(namelist, 'r')
    numf = open(numlist, 'r')
    savef = open('clientlist.txt', 'w')

    # create list to hold names, numbers, and client list
    names = []
    nums = []
    clientlist = []

    # add the name to the name and number list
    for name in namef:
        name = name.rstrip()
        names.append(name)
    for num in numf:
        num = num.rstrip()
        nums.append('M99' + num)
    # print("names: ", names)
    # print("numbers: ", nums)

    # variable to hold the note for the clientlist
    note = "Test Account"

    # get length of the name list
    namelen = len(names)

    # create the dictionary to hold the client purchase_info
    for i in range(namelen):
        clientdict = {'name': names[i], 'bpn': nums[i], 'note': note}
        clientlist.append(clientdict)
    # print("clientlist: ", clientlist)
    # print("len: ", len(clientlist))

    # write the list to the file using json dumps
    savef.write(json.dumps(clientlist))

    # close the files
    namef.close()
    numf.close()
    savef.close()


if __name__ == '__main__':
    print("Starting")
    ClientCreator()
    print("Complete")
