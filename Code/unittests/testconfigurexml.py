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

from configurexml import ConfigurationXML

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
        
    def testifDifficultyLevelareAddedintheXmlFile(self):
        gameType = self.xmlSettingsFile.getSudokuDifficultyLevels()
        expecteddificultList = ['Easy', 'Medium', 'Hard']
        self.assertEqual(expecteddificultList, gameType)

    def testifAlgorithmOptionsareAddedintheXmlFile(self):
        gameType = self.xmlSettingsFile.getSudokuAlgorithmOptions()
        expecteddificultList = ['BackTracking', 'Peter Norvig', 'Exact']
        self.assertEqual(expecteddificultList, gameType)

    def testifOutputFormatareAddedinthexXmlFile(self):
        gameType = self.xmlSettingsFile.getSudokuOutputFormat()
        expecteddificultList = ['Console', 'File']
        self.assertEqual(expecteddificultList, gameType)

    def testifFilePathisaddinXmlFile(self):
        gameType = self.xmlSettingsFile.getSudokuFilePath()
        expectedFilePath = ['c:\user\SudokuFile.txt']
        self.assertEqual(expectedFilePath, gameType)

    def testifMatrixDimensionAddedintheXmlFile(self):
        gameType = self.xmlSettingsFile.getSudokuMatrixDimension()
        expectedMatrixDimension = ['9']
        self.assertEqual(expectedMatrixDimension, gameType)

    # Unit tests for write XML methods

    def testifGameOptionSelectedbyUserwasUpdatedinXML(self):        
        setTestWriteGameOption = "Solve"
        expectedResult = "Solve"
        self.xmlSettingsFile.writeSudokuGameOptions(setTestWriteGameOption)
        self.assertEqual(expectedResult, self.xmlSettingsFile.\
            getUserSudokuGameOption())

    def testifDifficultyLevelSelectedbyUserwasUpdatedinXML(self):        
        setTestWriteDifficultyLevel = "Easy"
        expectedResult = "Easy"
        self.xmlSettingsFile.writeSudokuDifficultyLevels\
            (setTestWriteDifficultyLevel)
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
        self.xmlSettingsFile.writeSudokuOutputPathFile\
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
        expectedResult = "Easy"
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
