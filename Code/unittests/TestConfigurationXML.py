"""
Author:  Debbie Rios
Date: 07/04/2013
Modified: None.
Revised by: None
"""
import unittest


import os, sys
lib_path = os.path.abspath('../')
sys.path.append(lib_path)

from ConfigurationXML import ConfigurationXML
from Level import Level

"""
Unit Test for class ConfigurationXML, verify if read and write methods
are working as expected.
"""

class TestConfigurationXML(unittest.TestCase):
    def setUp(self):
        self.xmlSettingsFile = ConfigurationXML('../Configuration.xml')

    def testifGameOptionsareAddedintheXmlFile(self):
        gameType = self.xmlSettingsFile.getSudokuGameOptions()
        expectedOptionsList = ['Solve', 'Generate', 'Change Settings', 'Exit']
        self.assertEqual(expectedOptionsList, gameType)

    def testifDifficultyLevelandBottomTopLevelsareaAddedintheXmlFile(self):
        listOfLevels = self.xmlSettingsFile.getSudokuDifficultyLevels()
        firstLevel = Level(15, 20, "Easy")
        secondLevel = Level(21, 35, "Medium")
        thirdLevel = Level(36, 55, "Hard")
        levelListComparison = (listOfLevels[0] == firstLevel and
                        listOfLevels[1] == secondLevel and
                        listOfLevels[2] == thirdLevel)
        self.assertTrue(levelListComparison)

    def testifAlgorithmOptionsareAddedintheXmlFile(self):
        gameType = self.xmlSettingsFile.getSudokuAlgorithmOptions()
        expecteddificultList = ['BackTracking', 'Peter Norvig', 'Exact']
        self.assertEqual(expecteddificultList, gameType)

    def testifOutputFormatareAddedinthexXmlFile(self):
        gameType = self.xmlSettingsFile.getSudokuOutputFormat()
        expecteddificultList = ['Console', 'File']
        self.assertEqual(expecteddificultList, gameType)

    # Unit tests for write XML methods

    def testifGameOptionSelectedbyUserwasUpdatedinXML(self):
        setTestWriteGameOption = "Solve"
        expectedResult = "Solve"
        self.xmlSettingsFile.writeSudokuGameOptions(setTestWriteGameOption)
        self.assertEqual(expectedResult, self.xmlSettingsFile.\
            getUserSudokuGameOption())

    def testifDifficultyLevelSelectedbyUserwasUpdatedinXML(self):
        expectedResult = Level(21, 35 ,"Medium")
        self.xmlSettingsFile.writeSudokuDifficultyLevels\
            (expectedResult)
        self.assertEqual(expectedResult, self.xmlSettingsFile.\
            getUserDifficultyLevel())

    def testifAlgorithmOptionSelectedbyUserwasUpdatedinXML(self):
        setTestWriteAlgorithmOption = "Peter Norvig"
        expectedResult = "Peter Norvig"
        self.xmlSettingsFile.writeSudokuAlgorithmOptions\
            (setTestWriteAlgorithmOption)
        self.assertEqual(expectedResult, self.xmlSettingsFile.\
            getUserAlgorithmOption())

    def testifOutputFormatSelectedbyUserwasUpdatedinXML(self):
        setTestWriteOutputFormat = "Console"
        expectedResult = "Console"
        self.xmlSettingsFile.writeSudokuOutputFormat\
            (setTestWriteOutputFormat)
        self.assertEqual(expectedResult, self.xmlSettingsFile.\
            getUserOutputFormat())

    def testifOutputPathFileSelectedbyUserwasUpdatedinXML(self):
        setTestWriteOutputPathFile = "c:\\user\\SudokuFile.txt"
        expectedResult = "c:\\user\\SudokuFile.txt"
        self.xmlSettingsFile.writeSudokuFilePath\
            (setTestWriteOutputPathFile)
        self.assertEqual(expectedResult, self.xmlSettingsFile.\
            getUserFilePath())

    def testifMatrixDimensionSelectedwasUpdatedinXML(self):
        setTestWriteMatrixDimension = 9
        expectedResult = 9
        self.xmlSettingsFile.writeSudokuMatrixDimension\
            (setTestWriteMatrixDimension)
        self.assertEqual( expectedResult, self.xmlSettingsFile.\
            getUserMatrixDimension())

    def testifGameOptionsetbyUserwasUpdatedinXmlFile(self):
        expectedResult = "Solve"
        self.assertEqual( expectedResult, self.xmlSettingsFile.\
            getUserSudokuGameOption())

    def testifUserDifficultyLevelsetbyUserwasUpdatedinXmlFile(self):
        expectedResult = Level(21, 35 ,"Medium")
        self.assertEqual( expectedResult, self.xmlSettingsFile.\
            getUserDifficultyLevel())

    def testifAlgorithmOptionsetbyUserwasUpdatedinXmlFile(self):
        expectedResult = "Peter Norvig"
        self.assertEqual( expectedResult, self.xmlSettingsFile.\
            getUserAlgorithmOption())

    def testifOutputFormatsetbyUserwasUpdatedinXmlFile(self):
        expectedResult = "Console"
        self.assertEqual( expectedResult, self.xmlSettingsFile.\
            getUserOutputFormat())

    def testifFilePathbyUserwasUpdatedinXmlFile(self):
        expectedResult = "c:\\user\\SudokuFile.txt"
        self.assertEqual( expectedResult, self.xmlSettingsFile.\
            getUserFilePath())

    def testifFilePathbyUserwasUpdatedinXmlFile(self):
        expectedResult = 9
        self.assertEqual( expectedResult, self.xmlSettingsFile.\
            getUserMatrixDimension())

if __name__ == '__main__':
    unittest.main()
