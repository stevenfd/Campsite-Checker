class AvailabilityCheck:
    def __init__(self, name, campsiteIds, dates, occupants):
        self.name = name
        self.campsiteIds = campsiteIds
        self.dates = dates
        self.occupants = occupants
        
        self.months = self.generateMonths()

    def generateMonths(self):
        months = set()
        for date in self.dates:
            months.add(date.month)
        return months

    #I don't know if this should hold it but I'm putting it here for now
    def generateUrls(self):
        linkFormat = "https://www.recreation.gov/api/camps/availability/campground/{id}/month?start_date={date}T00%3A00%3A00.000Z"
        urls = []
        for campsiteId in self.campsiteIds:
            for month in self.months:
                urls.append(linkFormat.format(id = campsiteId, date = "2020-0{}-01".format(month))) #TODO: Check for month and year
        return urls
