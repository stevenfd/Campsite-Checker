import unittest
import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../source")
import reader

class TestReader(unittest.TestCase):

    def testEmptyFile(self):
        self.assertEqual(len(reader.readFile("tests/testFiles/empty.json")), 0)
    
    def testOneAvailability(self):
        availabilityChecks = reader.readFile("tests/testFiles/one.json")
        self.assertEqual(len(availabilityChecks), 1)

        yos = availabilityChecks[0]
        self.assertEqual(yos.name, "Yosemite - Hodgdon")
        self.assertEqual(yos.campsiteIds[0], "232451")
        self.assertEqual(yos.dates[0].strftime("%x"), "06/22/20")
        self.assertEqual(yos.dates[1].strftime("%x"), "06/20/20")
        self.assertEqual(yos.occupants, 2)


if __name__ == '__main__':
    unittest.main()