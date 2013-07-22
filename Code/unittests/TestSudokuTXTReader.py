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

from SudokuTXTReader import SudokuTXTReader

class TestSudokuTXTReader(unittest.TestCase):

    def setUp(self):
        self.txtObject = SudokuTXTReader("requiredtestfiles/sudokusolve.txt", 9)

    def testReadSudokuStringFromTXTFile(self):
        expected =  "001700600090043000007000810003050900002" + \
                    "600075080000020040009002605021008000800040"
        review = self.txtObject.readSudokuFromTXTFile()
        self.assertEquals(expected, review)

    def testSizeOfSudokuStringFromTXTFile(self):
        expected = self.txtObject.isSizeAccurate()
        self.assertTrue(expected)

    def testSetTXTFileName(self):
        expected = "NewTXTFile.txt"
        self.txtObject.setTXTFileName(expected)
        self.assertEqual(expected, self.txtObject._txtFileName)

    def testAreOnlyAllowedNumbers(self):
        expected = self.txtObject.areOnlyAllowedNumbers()
        self.assertTrue(expected)

    def testProvideWrongValuesUsingAlphanumericCharsInsteadOfDigits(self):
        self.txtObject.__init__("requiredtestfiles/wrongsudokusolve.txt", 9)
        expected = self.txtObject.areOnlyAllowedNumbers()
        self.assertFalse(expected)
        self.txtObject.__init__("requiredtestfiles/sudokusolve.txt", 9)

    def testCountLinesProvidedInTXTFile(self):
        expected = self.txtObject.isDimensionAccurate()
        self.assertTrue(expected)

    def testISFileProvidedAccurate(self):
        expected = self.txtObject.isTXTContentValid()
        self.assertTrue(expected)

    def testEachRowContainsSizeEntriesWhenProvidedWrongFormat(self):
        wrongFormatTXTObject = SudokuTXTReader\
                                ("requiredtestfiles/wrongsizesolve.txt", 9)
        expected = wrongFormatTXTObject._countRowsSizeEntries()
        self.assertFalse(expected)

if  __name__ == '__main__':
    unittest.main()