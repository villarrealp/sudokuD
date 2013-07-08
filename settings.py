
#from configureXML import ConfigurationXML

from configurexml import ConfigurationXML

class Settings:


    def __init__(self):


        self._sudokuSettingsXMLHandler = ConfigurationXML("Configuration.xml")
        
        self._sudokuGameType = self._sudokuSettingsXMLHandler.getUserSudokuGameOption()
        self._sudokuDifficultyLevel = self._sudokuSettingsXMLHandler.getUserDifficultyLevel()
        self._sudokuAlgorithmOption= self._sudokuSettingsXMLHandler.getUserAlgorithmOption()

        self._sudokuOutputFormat = self._sudokuSettingsXMLHandler.getUserOutputFormat()
        
        self._sudokuOutputPathFile = self._sudokuSettingsXMLHandler.getUserFilePath()
        self._sudokuMatrixDimension = self._sudokuSettingsXMLHandler.getUserMatrixDimension()

        

    def getSudokuGameType(self):
        return self._sudokuGameType
    
    def getSudokuDifficultyLevel(self):
        return self._sudokuDifficultyLevel
    
    def getSudokuAlgorithmOption(self):
        return self._sudokuAlgorithmOption

    def getSudokuOutputFormat(self):
        return self._sudokuOutputFormat

    def getSudokuOutputPathFile(self):
        return self._sudokuOutputPathFile

    def getSudokuMatrixDimension(self):
        return self._sudokuMatrixDimension



    def setSudokuGameType(self, gameType):
        self._sudokuGameType = gameType
    
    def setSudokuDifficultyLevel(self, difficultyLevel):
        self._sudokuDifficultyLevel = difficultyLevel
    
    def setSudokuAlgorithmOption(self, algorithmOption):
        self._sudokuAlgorithmOption = algorithmOption

    def setSudokuOutputFormat(self, outputFormat):
        self._sudokuOutputFormat = outputFormat 

    def setSudokuOutputPathFile(self, outputPathFile):
        self._sudokuOutputPathFile = outputPathFile

    def setSudokuMatrixDimension(self, matrixDimension):
        self._sudokuMatrixDimension = matrixDimension

    def restoreDefaultSettings(self):
        
        sudokuDefaultSettingsXMLHandler = ConfigurationXML("UserDefaultSettings.xml")
        self._sudokuGameType = sudokuDefaultSettingsXMLHandler.getUserSudokuGameOption()
        self._sudokuDifficultyLevel = sudokuDefaultSettingsXMLHandler.getUserDifficultyLevel()
        self._sudokuAlgorithmOption= sudokuDefaultSettingsXMLHandler.getUserAlgorithmOption()
        self._sudokuOutputFormat = sudokuDefaultSettingsXMLHandler.getUserOutputFormat()
        self._sudokuOutputPathFile = sudokuDefaultSettingsXMLHandler.getUserFilePath()
        self._sudokuMatrixDimension = sudokuDefaultSettingsXMLHandler.getUserMatrixDimension()

        self.saveCurrentSettings()

    def saveCurrentSettings(self):
        
        self._sudokuSettingsXMLHandler.WriteSudokuGameOptions(self._sudokuGameType)
        self._sudokuSettingsXMLHandler.WriteSudokuDifficultyLevels(self._sudokuDifficultyLevel)
        self._sudokuSettingsXMLHandler.WriteSudokuAlgorithmOptions(self._sudokuAlgorithmOption)
        self._sudokuSettingsXMLHandler.WriteSudokuOutputFormat(self._sudokuOutputFormat)
        self._sudokuSettingsXMLHandler.WriteSudokuOutputPathFile(self._sudokuOutputPathFile)
        self._sudokuSettingsXMLHandler.WriteSudokuMatrixDimension(self._sudokuMatrixDimension)

    def areDefaultSettingsSet(self):
        return True