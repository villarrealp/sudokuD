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

from settings import Settings

class TestSettings(unittest.TestCase):
    def setUp(self):        
        self.defaultSettings = Settings('../Configuration.xml')

    def testSetdefaultSettings(self):
        self.defaultSettings.restoreDefaultSettings()        
        self.assertTrue(self.defaultSettings.areDefaultSettingsSet())

    def testGetSudokuGameTypeMethod(self):
        expectedResult = "Solve"
        self.assertEqual(expectedResult, self.defaultSettings.getSudokuGameType())

    def testGetSudokuDifficultyLevelMethod(self):
        expectedResult = "Easy"
        self.assertEqual(expectedResult, self.defaultSettings.getSudokuDifficultyLevel())

    def testGetSudokuAlgorithmOptionMethod(self):
        expectedResult = "BackTracking"
        self.assertEqual(expectedResult, self.defaultSettings.getSudokuAlgorithmOption())

    def testGetSudokuOutputFormatMethod(self):
        expectedResult = "Console"
        self.assertEqual(expectedResult, self.defaultSettings.getSudokuOutputFormat())

    def testGetSudokuOutputPathFileMethod(self):
        expectedResult = "c:\\user\\"
        self.assertEqual(expectedResult, self.defaultSettings.getSudokuOutputPathFile())

    def testGetSudokuMatrixDimensionMethod(self):
        expectedResult = 9
        self.assertEqual(expectedResult, self.defaultSettings.getSudokuMatrixDimension())

    def testSetSudokuGameTypeMethod(self):
        setTestValueAtGameType = "Generate"
        expectedResult = setTestValueAtGameType
        self.defaultSettings.setSudokuGameType(setTestValueAtGameType)
        self.assertEqual(expectedResult, self.defaultSettings.getSudokuGameType())

    def testSetSudokuDifficultyLevelMethod(self):        
        setTestDifficultyLevel = "Medium"
        expectedResult = setTestDifficultyLevel
        self.defaultSettings.setSudokuDifficultyLevel(setTestDifficultyLevel)
        self.assertEqual(expectedResult, self.defaultSettings.getSudokuDifficultyLevel())

    def testSetSudokuAlgorithmOptionMethod(self):        
        setTestAlgorithmOption = "Peter Novig"
        expectedResult = setTestAlgorithmOption
        self.defaultSettings.setSudokuAlgorithmOption(setTestAlgorithmOption)
        self.assertEqual(expectedResult, self.defaultSettings.getSudokuAlgorithmOption())

    def testSetSudokuOutputFormatMethod(self):        
        setTestOutputFormat = "Console"
        expectedResult = setTestOutputFormat
        self.defaultSettings.setSudokuOutputFormat(setTestOutputFormat)
        self.assertEqual(expectedResult, self.defaultSettings.getSudokuOutputFormat())

    def testSetSudokuOutputPathFileMethod(self):        
        setTestOutputPathFile = "../Results/"
        expectedResult = setTestOutputPathFile
        self.defaultSettings.setSudokuOutputPathFile(setTestOutputPathFile)
        self.assertEqual(expectedResult, self.defaultSettings.getSudokuOutputPathFile())

    def testSetSudokuMatrixDimensionMethod(self):
        setTestMatrixDimension = 27
        expectedResult = setTestMatrixDimension                
        self.defaultSettings.setSudokuMatrixDimension(setTestMatrixDimension)
        self.assertEqual(expectedResult, self.defaultSettings.getSudokuMatrixDimension())
                
if __name__ == '__main__':
	unittest.main()