import unittest
import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../source")
from AvailabilityCheck import AvailabilityCheck
import datetime

class TestReader(unittest.TestCase):

    def testGenerateMonthsOne(self):
        check = AvailabilityCheck("Test", ["1", "2"], [datetime.datetime(2020, 6, 22)], 2)
        months = check.generateMonths()
        self.assertEqual(1, len(months))
        self.assertTrue(6 in months)
    
    
    def testGenerateMonthsOneWithDuplicate(self):
        check = AvailabilityCheck("Test", ["1", "2"], [datetime.datetime(2020, 6, 22), datetime.datetime(2020, 6, 30)], 2)
        months = check.generateMonths()
        self.assertEqual(1, len(months))
        self.assertTrue(6 in months)
    
    
    def testGenerateMultipleMonths(self):
        check = AvailabilityCheck("Test", ["1", "2"], [datetime.datetime(2020, 6, 22), datetime.datetime(2020, 9, 30), 
                datetime.datetime(2020, 9, 30), datetime.datetime(2020, 2, 20)], 2)
        months = check.generateMonths()
        self.assertEqual(3, len(months))
        self.assertTrue(9 in months)
        self.assertTrue(2 in months)
        self.assertTrue(6 in months)

    def testGenerateUrlsOneCamp(self):
        check = AvailabilityCheck("Test", ["1"], [datetime.datetime(2020, 6, 22), datetime.datetime(2020, 9, 30)], 2)
        urls = check.generateUrls()

        self.assertEquals(2, len(urls))
        self.assertTrue("https://www.recreation.gov/api/camps/availability/campground/1/month?start_date=2020-06-01T00%3A00%3A00.000Z" in urls)


    def testGenerateUrlsMultipleCamps(self):
        return
    
    def testGenerateUrlsMultipleYears(self):
        return


if __name__ == '__main__':
    unittest.main()