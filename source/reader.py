# Read in user defined data for what campsites to check
import json
import datetime
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
        dates = []
        for date in avail['dates']:
            parts = date.split("/");
            dates.append(datetime.datetime(2000 + int(parts[2]), int(parts[0]), int(parts[1])))
            
        dates.sort()
        availabilityChecks.append(AvailabilityCheck(avail['name'], avail['campsiteIds'], dates, int(avail['occupants'])))

    return availabilityChecks
