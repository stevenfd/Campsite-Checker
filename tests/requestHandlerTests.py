import unittest
import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../source")
from AvailabilityCheck import AvailabilityCheck
import requestHandler
import datetime

class requestHandlerTests(unittest.TestCase):
    
    def testPerformRequests(self):
        check = AvailabilityCheck("Test", ["232451"], [datetime.datetime(2020, 6, 22)], 2)
        requestHandler.performRequests(check)

    def testGenerateRequestUrls_SingleCamp(self): 
        check = AvailabilityCheck("Test", ["1"], [datetime.datetime(2020, 1, 22), datetime.datetime(2020, 10, 29), datetime.datetime(2021, 1, 22)], 2)
        result = requestHandler.generateRequestUrls(check)
        self.assertEqual(3, len(result))
        self.assertTrue('https://www.recreation.gov/api/camps/availability/campground/1/month?start_date=2020-01-01T00%3A00%3A00.000Z' in result)
        self.assertTrue('https://www.recreation.gov/api/camps/availability/campground/1/month?start_date=2021-01-01T00%3A00%3A00.000Z' in result)
        self.assertTrue('https://www.recreation.gov/api/camps/availability/campground/1/month?start_date=2020-10-01T00%3A00%3A00.000Z' in result)
    
    def testGenerateRequestUrls_MultipleCamp(self): 
        check = AvailabilityCheck("Test", ["1", "2"], [datetime.datetime(2020, 1, 22), datetime.datetime(2020, 10, 29)], 2)
        result = requestHandler.generateRequestUrls(check)
        self.assertEqual(4, len(result))
        self.assertTrue('https://www.recreation.gov/api/camps/availability/campground/1/month?start_date=2020-01-01T00%3A00%3A00.000Z' in result)
        self.assertTrue('https://www.recreation.gov/api/camps/availability/campground/1/month?start_date=2020-10-01T00%3A00%3A00.000Z' in result)
        self.assertTrue('https://www.recreation.gov/api/camps/availability/campground/2/month?start_date=2020-01-01T00%3A00%3A00.000Z' in result)
        self.assertTrue('https://www.recreation.gov/api/camps/availability/campground/2/month?start_date=2020-10-01T00%3A00%3A00.000Z' in result)




    def testGenerateRequestDates_OneMonth(self): 
        check = AvailabilityCheck("Test", ["1", "2"], [datetime.datetime(2020, 6, 22)], 2)
        result = requestHandler.generateRequestDates(check.dates)
        self.assertEqual(1, len(result))
        self.assertTrue(datetime.datetime(2020, 6, 1) in result)
    
    def testGenerateRequestDates_OneMonthDuplicates(self): 
        check = AvailabilityCheck("Test", ["1", "2"], [datetime.datetime(2020, 6, 22), datetime.datetime(2020, 6, 29)], 2)
        result = requestHandler.generateRequestDates(check.dates)
        self.assertEqual(1, len(result))
        self.assertTrue(datetime.datetime(2020, 6, 1) in result)
    
    def testGenerateRequestDates_MultipleMonths(self): 
        check = AvailabilityCheck("Test", ["1", "2"], [datetime.datetime(2020, 6, 22), datetime.datetime(2020, 7, 22)], 2)
        result = requestHandler.generateRequestDates(check.dates)
        self.assertEqual(2, len(result))
        self.assertTrue(datetime.datetime(2020, 6, 1) in result)
        self.assertTrue(datetime.datetime(2020, 7, 1) in result)
        
    def testGenerateRequestDates_MultipleYears(self): 
        check = AvailabilityCheck("Test", ["1", "2"], [datetime.datetime(2020, 6, 22), datetime.datetime(2021, 6, 22)], 2)
        result = requestHandler.generateRequestDates(check.dates)
        self.assertEqual(2, len(result))
        self.assertTrue(datetime.datetime(2020, 6, 1) in result)
        self.assertTrue(datetime.datetime(2021, 6, 1) in result)


if __name__ == '__main__':
    unittest.main()