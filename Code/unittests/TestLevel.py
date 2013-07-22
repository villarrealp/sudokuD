"""
Author: Alvaro Avila
Date: 07/19/2013
Modified: None.
Revised by: None
"""

import unittest

import os, sys
lib_path = os.path.abspath('../')
sys.path.append(lib_path)

from Level import Level

class TestLevel(unittest.TestCase):

    def setUp(self):
        self.levelForTesting = Level(35, 49, "Medium")

    def testGetTopLimit(self):
        testTopLimit = 49
        self.assertEqual(testTopLimit, self.levelForTesting.getTopLimit())

    def testGetBottomLimit(self):
        testTopLimit = 35
        self.assertEqual(testTopLimit, self.levelForTesting.getBottomLimit())

    def testGetNameLevel(self):
        expected = "Medium"
        self.assertEqual(expected, self.levelForTesting.getNameLevel())

    def testSetTopLimit(self):
        expected = 55
        self.levelForTesting.setTopLimit(expected)
        self.assertEqual(expected, self.levelForTesting.getTopLimit())

    def testSetBottomLimit(self):
        expected = 40
        self.levelForTesting.setBottomLimit(expected)
        self.assertEqual(expected, self.levelForTesting.getBottomLimit())

    def testSetNameLevel(self):
        expected = "Hard"
        self.levelForTesting.setNameLevel(expected)
        self.assertEqual(expected, self.levelForTesting.getNameLevel())

    def testDifferenceBetweenTwoLevelsWhenTheyHaveSameValues(self):
        firstLevelForTesting = Level(35, 49, "Medium")
        secondLevelForTesting = Level(35, 49, "Medium")
        self.assertEqual(firstLevelForTesting, secondLevelForTesting)

    def testDifferenceBetweenTwoLevelsWhenTheyHaveDifferentValues(self):
        firstLevelForTesting = Level(35, 49, "Medium")
        secondLevelForTesting = Level(35, 50, "Hard")
        self.assertFalse(firstLevelForTesting == secondLevelForTesting)

if __name__ == '__main__':
        unittest.main()





























