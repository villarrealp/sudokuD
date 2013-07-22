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

from Settings import Settings
from Level import Level

class TestSettings(unittest.TestCase):

    def setUp(self):
        self.testSettings = Settings('../Configuration.xml',
                            "../UserDefaultSettings.xml")
        self.testSettings.restoreDefaultSettings()

    def testSetdefaultSettings(self):
        self.testSettings.restoreDefaultSettings()
        self.assertTrue(self.testSettings.areDefaultSettingsSet())

    def testGetSudokuDifficultyLevels(self):

        listOfLevels = self.testSettings.getSudokuDifficultyLevelOptions()
        firstLevel = Level(15, 20, "Easy")
        secondLevel = Level(21, 35, "Medium")
        thirdLevel = Level(36, 55, "Hard")
        levelListComparison = (listOfLevels[0] == firstLevel and
                        listOfLevels[1] == secondLevel and
                        listOfLevels[2] == thirdLevel)
        self.assertTrue(levelListComparison)

    def testGetSudokuGameTypeMethod(self):
        expectedResult = "Solve"
        self.assertEqual(expectedResult, self.testSettings.getSudokuGameType())

    def testGetSudokuDifficultyLevelMethod(self):
        testLevel = Level(15, 20,"Easy")
        self.assertTrue(self.testSettings.\
                        getSudokuDifficultyLevel() == testLevel)

    def testGetSudokuAlgorithmOptionMethod(self):
        expectedResult = "BackTracking"
        self.assertEqual(expectedResult, self.testSettings.\
                        getSudokuAlgorithmOption())

    def testGetSudokuOutputFormatMethod(self):
        expectedResult = "Console"
        self.assertEqual(expectedResult, self.testSettings.\
                        getSudokuOutputFormat())

    def testGetSudokuOutputPathFileMethod(self):
        expectedResult = "..\\Sudoku\\"
        self.assertEqual(expectedResult, self.testSettings.getSudokuPathFile())

    def testGetSudokuFileNameMethod(self):
        expectedResult = "SudokuFile.txt"
        self.assertEqual(expectedResult, self.testSettings.getSudokuFileName())

    def testGetSudokuMatrixDimensionMethod(self):
        expectedResult = 9
        self.assertEqual(expectedResult, self.testSettings.\
                        getSudokuMatrixDimension())

    def testSetSudokuGameTypeMethod(self):
        setTestValueAtGameType = "Generate"
        expectedResult = setTestValueAtGameType
        self.testSettings.setSudokuGameType(setTestValueAtGameType)
        self.assertEqual(expectedResult, self.testSettings.getSudokuGameType())
        self.testSettings.restoreDefaultSettings()

    def testSetSudokuDifficultyLevelMethod(self):
        setTestDifficultyLevel = "Medium"
        expectedResult = setTestDifficultyLevel
        self.testSettings.setSudokuDifficultyLevel(setTestDifficultyLevel)
        self.assertEqual(expectedResult, self.testSettings.\
                        getSudokuDifficultyLevel())
        self.testSettings.restoreDefaultSettings()

    def testSetSudokuAlgorithmOptionMethod(self):
        setTestAlgorithmOption = "Peter Novig"
        expectedResult = setTestAlgorithmOption
        self.testSettings.setSudokuAlgorithmOption(setTestAlgorithmOption)
        self.assertEqual(expectedResult, self.testSettings.\
                        getSudokuAlgorithmOption())
        self.testSettings.restoreDefaultSettings()

    def testSetSudokuOutputFormatMethod(self):
        setTestOutputFormat = "Console"
        expectedResult = setTestOutputFormat
        self.testSettings.setSudokuOutputFormat(setTestOutputFormat)
        self.assertEqual(expectedResult, self.testSettings.\
                        getSudokuOutputFormat())
        self.testSettings.restoreDefaultSettings()

    def testSetSudokuPathFileMethod(self):
        setTestPathFile = "..\\Sudoku\\"
        expectedResult = setTestPathFile
        self.testSettings.setSudokuPathFile(setTestPathFile)
        self.assertEqual(expectedResult, self.testSettings.getSudokuPathFile())
        self.testSettings.restoreDefaultSettings()

    def testSetSudokuMatrixDimensionMethod(self):
        setTestMatrixDimension = 27
        expectedResult = setTestMatrixDimension
        self.testSettings.setSudokuMatrixDimension(setTestMatrixDimension)
        self.assertEqual(expectedResult, self.testSettings.\
                        getSudokuMatrixDimension())
        self.testSettings.restoreDefaultSettings()

if __name__ == '__main__':
	unittest.main()