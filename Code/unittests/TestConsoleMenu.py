"""
Author: Pilar Villarreal
Date: 07/04/2013
Modified: None.
Revised by: None
"""

import unittest

import os, sys
lib_path = os.path.abspath('../')
sys.path.append(lib_path)

from ConsoleMenu import ConsoleMenu

class TestConsoleMenu(unittest.TestCase):
    def setUp(self):
        self.optionOutRangeNumber = 123
        self.optionInRangeNumber = 3
        self.optionChar = 'x'
        self.inputExpected = "5"
        self.myMenu = ConsoleMenu('../Configuration.xml',
                                  '../UserDefaultSettings.xml')

    def testValidateUserInputWithOptionInRange(self):
        numberOptions = 4
        self.assertTrue(self.myMenu.isValidSelectedNumberOption(self.optionInRangeNumber,
                                                        numberOptions))

    def testValidateUserInputWithOptionNotInRange(self):
        numberOptions = 4
        self.assertFalse(self.myMenu.isValidSelectedNumberOption(self.optionOutRangeNumber,
                                                         numberOptions))

    def testValidateUserInputWithOptionAsChar(self):
        numberOptions = 4
        self.assertFalse(self.myMenu.isValidSelectedNumberOption(self.optionChar,
                                                         numberOptions))

if __name__=='__main__':
        unittest.main()