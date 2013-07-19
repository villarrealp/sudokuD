"""
Author: Alvaro Avila
Date: 07/04/2013
Modified:   07/19/2013    by: Alvaro Avila
                Comments: None.
Revised by: 07/18/2013    by: Alvaro Avila
"""

from ConfigurationXML import ConfigurationXML

class Settings:
    """
    Class Name: Settings
    Description: The Settings class will hold the Sudoku Game Settings that will
                obtain from a XML file at the beginning and also will be able to
                change and save current settings into the corresponding files.
    """

    def __init__(self, fileName, defaultSettingsFile):
        """
        This is the Settings Constructor method where it is initialized required
        values by default and it gets the information from the Configuration.xml
        file uses the ConfigurationXML class in order to read the stored values.

        Keyword arguments:
        fileName -- This is a String value of the XML settings File Name which
                    contains the user settings and the options that could be
                    used(i.e. "Configuration.xml").

        defaultSettingsFile --  This is a String value of the XML settings File
                                Name which contains the default settings used to
                                rollback any posible changes that sudoku game
                                user could do (i.e. "UserDefaultSettings.xml").
        """
        self._sudokuSettingsXMLHandler = ConfigurationXML(fileName)
        self.defaultSettingsFile = defaultSettingsFile
        self._sudokuGameType = self._sudokuSettingsXMLHandler.\
                                                    getUserSudokuGameOption()
        self._sudokuDifficultyLevel = self._sudokuSettingsXMLHandler.\
                                                    getUserDifficultyLevel()
        self._sudokuCustomLevel = ""
        self._sudokuAlgorithmOption = self._sudokuSettingsXMLHandler.\
                                                    getUserAlgorithmOption()
        self._sudokuOutputFormat = self._sudokuSettingsXMLHandler.\
                                                    getUserOutputFormat()
        self._sudokuPathFile = self._sudokuSettingsXMLHandler.\
                                                    getUserFilePath()
        self._sudokuFileName = self._sudokuSettingsXMLHandler.\
                                                    getUserFileName()
        self._sudokuMatrixDimension = self._sudokuSettingsXMLHandler.\
                                                    getUserMatrixDimension()
    def getSudokuGameTypeOptions(self):
        """
        Returns a list of string values with the options of game types(i.e
        "Solve", "Generate")
        """
        return self._sudokuSettingsXMLHandler.getSudokuGameOptions()

    def getSudokuDifficultyLevelOptions(self):
        """
        Returns a list of string values with the options of level types(i.e
        Level(50, 65, "Easy"), Level(40, 49, "Medium"))
        """
        return self._sudokuSettingsXMLHandler.getSudokuDifficultyLevels()

    def getSudokuAlgorithmSolutionOptions(self):
        """
        Returns a list of string values with the options of algorithm types(i.e
        "Backtracking", "Peter Norving"..)
        """
        return self._sudokuSettingsXMLHandler.getSudokuAlgorithmOptions()

    def getSudokuOutputFormatOptions(self):
        """
        Returns a list of string values with the output format options of game
        types(i.e ("Console", "File"))
        """
        return self._sudokuSettingsXMLHandler.getSudokuOutputFormat()


    def getSudokuGameType(self):
        """ Returns a string value of current game type i.e("Solve" or
        "Generate")"""
        return self._sudokuGameType

    def getSudokuDifficultyLevel(self):
        """
        Returns a Level object value of the current Level of sudoku game
        dificulty Level.
        """
        return self._sudokuDifficultyLevel

    def getSudokuAlgorithmOption(self):
        """
        Return the string value of wich algorithm has been choosed to resolve a
        sudoku game.
        """
        return self._sudokuAlgorithmOption

    def getSudokuOutputFormat(self):
        """
        Returns the string value of current output format to display or get the
        results for a sudoku game i.e "File" or "Console".
        """
        return self._sudokuOutputFormat

    def getSudokuPathFile(self):
        """
        Returns the string value of the file path where the output will be
        stored i.e. "..\\Results\\" .
        """
        return self._sudokuPathFile

    def getSudokuFileName(self):
        """
        Returns the string value of the file name where results will be
        solved/generated, i.e. "SudokuGame.txt".
        """
        return self._sudokuFileName

    def getSudokuMatrixDimension(self):
        """
        Returns an integer value of what dimension should have the sudoku matrix
        this is only for internal use, i.e. 9.
        """
        return self._sudokuMatrixDimension

    def setSudokuGameType(self, gameType):
        """
        This method allows set a new value of sudoku game type, posibles values
        are "Solve" or "Generate".

        Keyword arguments:
        gameType -- This is a String value for the new value of
                    self._sudokuGameType i.e. "Solve".
        """
        self._sudokuGameType = gameType

    def setSudokuDifficultyLevel(self, difficultyLevel):
        """
        This method allows set a new Level type value of sudoku difficulty level
        i.e. Level(50, 65, "Easy")

        Keyword arguments:
        difficultyLevel -- This is a Level type value for the new
                            self._difficultyLevel value i.e. Level(50, 65,
                            "Hard").
        """
        self._sudokuDifficultyLevel = difficultyLevel

    def setSudokuAlgorithmOption(self, algorithmOption):
        """
        This method allows set a new value of algorithm to be used to resolve a
        sudoku game.

        Keyword arguments:
        algorithmOption -- This is a String value for the new value of
                            self._algorithmOption i.e."BackTracking".
        """
        self._sudokuAlgorithmOption = algorithmOption

    def setSudokuOutputFormat(self, outputFormat):
        """
        This method allows set a new value of the output format that will be
        used to display the game results.

        Keyword arguments:
        outputFormat -- This is a String value for the new value of
                            self._sudokuOutputFormat i.e."File"
        """
        self._sudokuOutputFormat = outputFormat

    def setSudokuPathFile(self, pathFile):
        """
        This method allows set a new path file value where will be stored the
        sudoku game results.

        Keyword arguments:
        pathFile -- This is a String value for the new value of
                    self._sudokuPathFile i.e."..\\Solution\\"
        """
        self._sudokuPathFile = pathFile

    def setSudokuFileName(self, fileName):
        """
        This method allows set a new value of the filename where will be
        stored the sudoku game results/generation.

        Keyword arguments:
        fileName -- This is a String value for the new value of
                    self._sudokuFileName i.e."MyFile.txt"
        """
        self._sudokuFileName = fileName

    def setSudokuMatrixDimension(self, matrixDimension):
        """
        This method allows set a new value of matrix dimension that should have
        the sudoku game that will be used to solve or generate, this is only for
        internal validation.

        Keyword arguments:
        matrixDimension -- This is a integer value for the new value of
                    self._sudokuMatrixDimension i.e. 9
        """
        self._sudokuMatrixDimension = matrixDimension

    def restoreDefaultSettings(self):
        """
        This method allows restore user saved/current settings to the default
        settings stored at UserDefaultSettings.xml file(Default user settings
        XML), does not return anything.
        """
        sudokuDefaultSettingsXMLHandler = ConfigurationXML\
                                            (self.defaultSettingsFile)
        self._sudokuGameType = sudokuDefaultSettingsXMLHandler.\
                                                getUserSudokuGameOption()
        self._sudokuDifficultyLevel = sudokuDefaultSettingsXMLHandler.\
                                                getUserDifficultyLevel()
        self._sudokuAlgorithmOption = sudokuDefaultSettingsXMLHandler.\
                                                getUserAlgorithmOption()
        self._sudokuOutputFormat = sudokuDefaultSettingsXMLHandler.\
                                                getUserOutputFormat()
        self._sudokuPathFile = sudokuDefaultSettingsXMLHandler.\
                                                getUserFilePath()
        self._sudokuMatrixDimension = sudokuDefaultSettingsXMLHandler.\
                                                getUserMatrixDimension()
        self._sudokuFileName = sudokuDefaultSettingsXMLHandler.\
                                                getUserFileName()
        self.saveCurrentSettings()

    def saveCurrentSettings(self):
        """
        This method allows save the current User setting values of the
        corresponding Settings into the XML file hold on
        self._sudokuSettingsXMLHandler(Configuration.xml), does not return
        anything.
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
                        writeSudokuFilePath(self._sudokuPathFile)
        self._sudokuSettingsXMLHandler.\
                        writeSudokuMatrixDimension(self._sudokuMatrixDimension)
        self._sudokuSettingsXMLHandler.\
                        writeSudokuFileName(self._sudokuFileName)

    def areDefaultSettingsSet(self):
        """
        This method returns True value after review if all of the current
        setting values are the default ones defined into UserDefaultSettings.xml
        file, False otherwise.
        """
        sudokuDefaultSettingsXMLHandler = ConfigurationXML(
                                            self.defaultSettingsFile)
        sudokuGameType = sudokuDefaultSettingsXMLHandler.\
                                                getUserSudokuGameOption()
        sudokuDifficultyLevel = sudokuDefaultSettingsXMLHandler.\
                                                getUserDifficultyLevel()
        sudokuAlgorithmOption = sudokuDefaultSettingsXMLHandler.\
                                                getUserAlgorithmOption()
        sudokuOutputFormat = sudokuDefaultSettingsXMLHandler.\
                                                getUserOutputFormat()
        sudokuPathFile = sudokuDefaultSettingsXMLHandler.getUserFilePath()
        sudokuMatrixDimension = sudokuDefaultSettingsXMLHandler.\
                                                getUserMatrixDimension()
        sudokuFileName = sudokuDefaultSettingsXMLHandler.getUserFileName()
        if(self._sudokuGameType == sudokuGameType and
           self._sudokuDifficultyLevel == sudokuDifficultyLevel and
           self._sudokuAlgorithmOption == sudokuAlgorithmOption and
           self._sudokuOutputFormat == sudokuOutputFormat and
           self._sudokuPathFile == sudokuPathFile and
           self._sudokuMatrixDimension == sudokuMatrixDimension and
           self._sudokuFileName == sudokuFileName):
            return True
        else:
            return False