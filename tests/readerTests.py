import unittest
import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../source")
import reader

class TestReader(unittest.TestCase):

    def testEmptyFile(self):
        self.assertEqual(0, len(reader.readFile("tests/testFiles/empty.json")))
    
    def testOneAvailability(self):
        availabilityChecks = reader.readFile("tests/testFiles/one.json")
        self.assertEqual(1, len(availabilityChecks))

        yos = availabilityChecks[0]
        self.assertEqual("Yosemite - Hodgdon", yos.name)
        self.assertEqual("232451", yos.campsiteIds[0])
        self.assertEqual("06/20/20", yos.dates[0].strftime("%x"))
        self.assertEqual("06/22/20", yos.dates[1].strftime("%x"))
        self.assertEqual(2, yos.occupants)


if __name__ == '__main__':
    unittest.main()