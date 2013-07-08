"""
Author: Alvaro Avila
Date: 07/04/2013
Modified:   07/04/2013    by: Alvaro Avila
                Comments: None.
Revised by: 07/04/2013    by: Alvaro Avila
"""

from configurexml import ConfigurationXML

"""
Class Name: Settings
Description: The Settings class will hold the Sudoku Game Settings that will 
             obtain from a XML file from the beginning and also will be able to
             change and save them into the corresponding files.
"""
class Settings:

    def __init__(self, fileName):
        """
        This is the Settings Constructor method where it is initialized all 
        values by default and it gets the information from the Configuration.xml
        file uses the ConfigurationXML class in order to read the stored values.
        """
        self._sudokuSettingsXMLHandler = ConfigurationXML(fileName)
        
        self._sudokuGameType = self._sudokuSettingsXMLHandler.\
                                                    getUserSudokuGameOption()
        self._sudokuDifficultyLevel = self._sudokuSettingsXMLHandler.\
                                                    getUserDifficultyLevel()

        self._sudokuAlgorithmOption = self._sudokuSettingsXMLHandler.\
                                                    getUserAlgorithmOption()
        self._sudokuOutputFormat = self._sudokuSettingsXMLHandler.\
                                                    getUserOutputFormat()        
        self._sudokuOutputPathFile = self._sudokuSettingsXMLHandler.\
                                                    getUserFilePath()
        self._sudokuMatrixDimension = self._sudokuSettingsXMLHandler.\
                                                    getUserMatrixDimension()
    def getSudokuGameTypeOptions(self):
        """
        Return a list of string values of sudoku game types like Solve or 
        Generate
        """
        return self._sudokuSettingsXMLHandler.getSudokuGameOptions()

    def getSudokuDifficultyLevelOptions(self):
        """
        Return a list of string values of sudoku Difficulty levels 
        """
        return self._sudokuSettingsXMLHandler.getSudokuDifficultyLevels()

    def getSudokuAlgorithmSolutionOptions(self):
        """
        Return a list of string values of wich algorithm has been choosed to 
        resolve a sudoku game.
        """
        return self._sudokuSettingsXMLHandler.getSudokuAlgorithmOptions()

    def getSudokuOutputFormatOptions(self):
        """
        Return a list of string values of wich output format the user has 
        choosed to display or get the results for a sudoku game like File or 
        Console.
        """
        return self._sudokuSettingsXMLHandler.getSudokuOutputFormat()


    def getSudokuGameType(self):
        """ Return a string value of sudoku game type like Solve or Generate"""
        return self._sudokuGameType
    
    def getSudokuDifficultyLevel(self):
        """Return the string value of sudoku game dificulty Level"""
        return self._sudokuDifficultyLevel
    
    def getSudokuAlgorithmOption(self):
        """
        Return the string value of wich algorithm has been choosed to resolve a 
        sudoku game.
        """
        return self._sudokuAlgorithmOption

    def getSudokuOutputFormat(self):
        """
        Return the string value of wich output format the user has choosed to 
        display or get the results for a sudoku game like File or Console.
        """
        return self._sudokuOutputFormat

    def getSudokuOutputPathFile(self):
        """
        Return the string value of the Full file path where the output will be 
        stored.
        """
        return self._sudokuOutputPathFile

    def getSudokuMatrixDimension(self):
        """
        Return an integer value of what dimension should have the sudoku matrix
        this is only for internal use, this value should not be displayed to 
        end game user.
        """
        return self._sudokuMatrixDimension

    def setSudokuGameType(self, gameType):
        """
        This method allows set value of sudoku game type, posibles values are 
        Solve or Generate.
        """
        self._sudokuGameType = gameType
    
    def setSudokuDifficultyLevel(self, difficultyLevel):
        """
        This method allows set value of sudoku difficulty level, as Easy, Medium
        and Hard.
        """
        self._sudokuDifficultyLevel = difficultyLevel
    
    def setSudokuAlgorithmOption(self, algorithmOption):
        """
        This method allows set value of algorithm to be used for resolve or 
        Generate a sudoku game.
        """
        self._sudokuAlgorithmOption = algorithmOption

    def setSudokuOutputFormat(self, outputFormat):
        """
        This method allows set value of the output format that will be used to 
        display the game user the results of the sudoku game.
        """
        self._sudokuOutputFormat = outputFormat 

    def setSudokuOutputPathFile(self, outputPathFile):
        """
        This method allows set value of the output full path file where will be 
        stored the  sudoku game results.
        """
        self._sudokuOutputPathFile = outputPathFile

    def setSudokuMatrixDimension(self, matrixDimension):
        """
        This method allows set value of the matrix dimension that should have 
        the sudoku game that will be used to solve or generate, this is only for
        internal use, this value should not be displayed to end game user.
        """
        self._sudokuMatrixDimension = matrixDimension

    def restoreDefaultSettings(self):
        """
        This method allows restore user saved/current settings to the default 
        settings stored at UserDefaultSettings.xml file.
        """
        sudokuDefaultSettingsXMLHandler = ConfigurationXML\
                                                ("../UserDefaultSettings.xml")
        self._sudokuGameType = sudokuDefaultSettingsXMLHandler.\
                                                getUserSudokuGameOption()
        self._sudokuDifficultyLevel = sudokuDefaultSettingsXMLHandler.\
                                                getUserDifficultyLevel()
        self._sudokuAlgorithmOption = sudokuDefaultSettingsXMLHandler.\
                                                getUserAlgorithmOption()
        self._sudokuOutputFormat = sudokuDefaultSettingsXMLHandler.\
                                                getUserOutputFormat()
        self._sudokuOutputPathFile = sudokuDefaultSettingsXMLHandler.\
                                                getUserFilePath()
        self._sudokuMatrixDimension = sudokuDefaultSettingsXMLHandler.\
                                                getUserMatrixDimension()

        self.saveCurrentSettings()

    def saveCurrentSettings(self):
        """
        This method allows save the current User setting values of this class 
        into the User settings setion into XML file (Configuration.xml).
        """
        self._sudokuSettingsXMLHandler.\
                        writeSudokuGameOptions(self._sudokuGameType)
        self._sudokuSettingsXMLHandler.\
                        writeSudokuDifficultyLevels(self._sudokuDifficultyLevel)
        self._sudokuSettingsXMLHandler.\
                        writeSudokuAlgorithmOptions(self._sudokuAlgorithmOption)
        self._sudokuSettingsXMLHandler.\
                        writeSudokuOutputFormat(self._sudokuOutputFormat)
        self._sudokuSettingsXMLHandler.\
                        writeSudokuOutputPathFile(self._sudokuOutputPathFile)
        self._sudokuSettingsXMLHandler.\
                        writeSudokuMatrixDimension(self._sudokuMatrixDimension)

    def areDefaultSettingsSet(self):
        """
        This method returns a boolean value after review if all of the current 
        setting values are the default ones defined into UserDefaultSettings.xml
        file.
        """
        sudokuDefaultSettingsXMLHandler = ConfigurationXML\
                                                ("../UserDefaultSettings.xml")
        sudokuGameType = sudokuDefaultSettingsXMLHandler.\
                                                getUserSudokuGameOption()
        sudokuDifficultyLevel = sudokuDefaultSettingsXMLHandler.\
                                                getUserDifficultyLevel()
        sudokuAlgorithmOption = sudokuDefaultSettingsXMLHandler.\
                                                getUserAlgorithmOption()
        sudokuOutputFormat = sudokuDefaultSettingsXMLHandler.\
                                                getUserOutputFormat()
        sudokuOutputPathFile = sudokuDefaultSettingsXMLHandler.\
                                                getUserFilePath()
        sudokuMatrixDimension = sudokuDefaultSettingsXMLHandler.\
                                                getUserMatrixDimension()
        if(self._sudokuGameType == sudokuGameType 
           and self._sudokuDifficultyLevel == sudokuDifficultyLevel and
           self._sudokuAlgorithmOption == sudokuAlgorithmOption and
           self._sudokuOutputFormat == sudokuOutputFormat and 
           self._sudokuOutputPathFile == sudokuOutputPathFile and 
           self._sudokuMatrixDimension == sudokuMatrixDimension
           ):
            return True
        else:
            return False