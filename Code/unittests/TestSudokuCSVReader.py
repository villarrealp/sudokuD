"""
Author: Alvaro Avila
Date: 07/04/2013
Modified: None.
Revised by: None
"""

import unittest

import os, sys
lib_path = os.path.abspath('../')
sys.path.append(lib_path)

from SudokuCSVReader import SudokuCSVReader

class TestSudokuCSVReader(unittest.TestCase):
    def setUp(self):
        self.csvObject = SudokuCSVReader("requiredtestfiles/SudokuTest.csv", 9)

    def testGetSudokuStringFromCSVFile(self):
        expected =  "001700600090043000007000810003050900002" + \
                    "600075080000020040009002605021008000800040"
        review = self.csvObject.getSudokuString()
        self.assertEquals(expected, review)

    def testSizeOfRowStringFromCSVFile(self):
        expected = self.csvObject._countRowsSizeEntries()
        self.assertTrue(expected)

    def testSetTXTFileName(self):
        expected = "NewTXTFile.txt"
        self.csvObject.setFileName(expected)
        self.assertEqual(expected, self.csvObject._csvFileName)

    def testAreOnlyAllowedNumbers(self):
        expected = self.csvObject.areOnlyAllowedNumbers()
        self.assertTrue(expected)

    def testIsDimensionAccurate(self):
        expected = self.csvObject.isDimensionAccurate()
        self.assertTrue(expected)

    def testIsCSVContentValid(self):
        expected = self.csvObject.isCSVContentValid()
        self.assertTrue(expected)

    def testIsSizeAccurate(self):
        expected = self.csvObject.isSizeAccurate()
        self.assertTrue(expected)

    def testProvideWrongValuesUsingAlphanumericCharsInsteadOfDigits(self):
        self.csvObject.__init__("requiredtestfiles/SudokuWrong.csv", 9)
        expected = self.csvObject.areOnlyAllowedNumbers()
        self.assertFalse(expected)
        self.csvObject.__init__("requiredtestfiles/SudokuTest.csv", 9)

    def testIsCSVContentValidWhenProvideAlphanumericCharsInsteadOfDigits(self):
        self.csvObject.__init__("requiredtestfiles/SudokuWrong.csv", 9)
        expected = self.csvObject.isCSVContentValid()
        self.assertFalse(expected)
        self.csvObject.__init__("requiredtestfiles/SudokuTest.csv", 9)

if  __name__=='__main__':
    unittest.main()