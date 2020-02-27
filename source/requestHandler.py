import datetime
from AvailabilityCheck import AvailabilityCheck


linkFormat = "https://www.recreation.gov/api/camps/availability/campground/{id}/month?start_date={date}T00%3A00%3A00.000Z"
def generateRequestUrls(check):
    dates = generateRequestDates(check.dates)
    urls = []
    for campsiteId in check.campsiteIds:
        for date in dates:
            urls.append(linkFormat.format(id = campsiteId, date = date.isoformat()))

    return urls

def generateRequestDates(dates):
    requestDates = set()
    for date in dates:
        requestDates.add(datetime.datetime(date.year, date.month, 1))
    return requestDates