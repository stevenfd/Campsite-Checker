# Read in user defined data for what campsites to check
import json
from AvailabilityCheck import AvailabilityCheck

def readFile(fileName):
    file = open(fileName, "r")

    if file.mode != "r":
        #TODO: Error handling
        return

    data = json.load(file)
    file.close()

    return createAvailabilities(data)

def createAvailabilities(data):
    availabilityChecks = []
    for avail in data['availabilities']:
        availabilityChecks.append(AvailabilityCheck(avail['name'], avail['campsiteIds'], avail['dates'], int(avail['occupants'])))

    return availabilityChecks
