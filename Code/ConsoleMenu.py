"""
Author: Pilar Villarreal
Date created:   07/03/2013
Modified:       07/04/2013 by Pilar Villarreal
                Comments: Working on refactoring methods.
                07/15/2013 by Pilar Villarreal
                Comments: Updated due to last changes to Settings class,
                added comments to methods to display the solved matrix.
                07/18/2013 by Pilar Villarreal
                Comments: Code refactoring and added more documentation.
Revised by: -

"""

import sys
import time
from Settings import Settings
from PeterNorvigAlgorithm import PeterNorvigAlgorithm
from ForwardCheck import ForwardCheck
from BacktrackingAlgorithm import BacktrackingAlgorithm
from SudokuTXTReader import SudokuTXTReader


"""
Class Name: ConsoleMenu

Description: This class uses the Settings extracted from the XML files and
             displays the menu options for the game in the console.
"""

class ConsoleMenu:

    def __init__(self, userSettings, defaultSettings):
        """
        Constructor method for the ConsoleMenu class.

        Keyword arguments:
        userSettings - Filename of the XML with the user settings.
        defaultSettings - Filename of the XML with the default settings.
        """
        self.settingsSudoku = Settings(userSettings, defaultSettings)

    def printLine(self, charSelected, length):
        """
        This method prints a line in console using the specified char.

        Keyword arguments:
        charSelected -- Char user to print the line
        length -- Integer value to determinate the length for the line.
        """
        line = charSelected
        for index in range(length):
            line = line + charSelected
        print line

    def displayMenuOptions(self, title, listOfOptions):
        """
        This method displays in console a menu list enumareted with options
        extracted from the XML file.

        Keyword arguments:
        title -- String with description of the menu to be displayed.
        i.e: "Sudoku" , "Change input type format"
        listOfOptions -- List of strings with the available options to be
        displayed extracted from the XMLfile.
        i.e: 1. Solve
             2. Generate
             3. Change Settings
             4. Exit
        """
        self.printLine("=", 50)
        print("                  ") + title
        self.printLine("=", 50)
        print("         Please select an option:")
        index = 1
        for option in listOfOptions:
            print("                 " + str(index) + ". " + option
                  + "                ")
            index = index + 1

    def getUserInput(self, textDescription):
        """
        This method uses raw_input function to store the option selected by the
        user.

        Keyword arguments:
        textDescription -- Description to be displayed to describe required
        input, i.e.: 'Enter the number of the  option:'

        Return:
        This method returns a string with the value entered by the user.
        """
        userInput = raw_input(textDescription)
        return userInput

    def isValidSelectedNumberOption(self, optionSelected, numberOptions):
        """
        This method casts the input user from a string to an integer and
        validates that it is in the range of numberOptions allowed.

        Keyword arguments:
        optionSelected -- String with the value entered by the user.
        numberOptions -- Maximum number of the options allowed.

        Return:
        The value returned is True in case that option entered is valid, False
        otherwise.
        """
        res = False
        try:
            option = int(optionSelected)
            if(option > 0 and option <= numberOptions):
                res = True
        except ValueError, e :
            print("'%s' is not a valid number of option."
                  % e.args[0].split(": ")[1])
        return res

    def difficultyLevelOptionsMenu(self):
        """
        This method displays in console the menu options for Difficulty Levels
        extracted from Configuration XML file.
        """
        difficultyLevelOptions = self.settingsSudoku.\
                                 getSudokuDifficultyLevelOptions()
        self.displayMenuOptions("Change difficulty level option", difficultyLevelOptions)
        optionValidated = self.askForValueUntilIsValid(difficultyLevelOptions)
        if(optionValidated == "1"):
            print("Easy")
            self.settingsSudoku.setSudokuDifficultyLevel("Easy")
        elif(optionValidated == "2"):
            print("Medium")
            self.settingsSudoku.setSudokuDifficultyLevel("Medium")
        elif(optionValidated == "3"):
            print("Hard")
            self.settingsSudoku.setSudokuDifficultyLevel("Hard")

    def outputFormatOptionsMenu(self):
        """
        This method displays in console the menu options for Output formats
        extracted from Configuration XML file.
        """
        outputFormatOptions = self.settingsSudoku.\
                              getSudokuOutputFormatOptions()
        self.displayMenuOptions("Change input type format", outputFormatOptions)
        optionValidated = self.askForValueUntilIsValid(outputFormatOptions)
        if(optionValidated == "1"):
            print("Console")
            self.settingsSudoku.setSudokuOutputFormat("Console")
        elif (optionValidated == "2"):
            print("File")
            self.settingsSudoku.setSudokuOutputFormat("File")

    def algorithmOptionsMenu(self):
        """
        This method displays in console the Menu options for Algorithms available
        extracted from Configuration XML file.
        """
        algorithmOptions = self.settingsSudoku.\
                           getSudokuAlgorithmSolutionOptions()
        self.displayMenuOptions("Change algorithm used", algorithmOptions)
        optionValidated = self.askForValueUntilIsValid(algorithmOptions)
        if(optionValidated == "1"):
            print("BackTracking")
            self.settingsSudoku.setSudokuAlgorithmOption("BackTracking")
        elif (optionValidated == "2"):
            print("Peter Norvig")
            self.settingsSudoku.setSudokuAlgorithmOption("Peter Norvig")
        elif (optionValidated == "3"):
            print("Quick Hackup")
            self.settingsSudoku.setSudokuAlgorithmOption("Quick Hackup")

    def displayOptionsSelected(self):
        """ This method displays in console the options selected by the user """
        self.printLine("=", 50)
        print("These are the game settings selected: ")
        self.printLine("=", 50)
        print self.settingsSudoku.getSudokuGameType()
        print self.settingsSudoku.getSudokuOutputFormat()
        print self.settingsSudoku.getSudokuAlgorithmOption()

    def displayOptionsSelectedByDefault(self):
        """ This method displays in console options selected by default """
        self.printLine("=", 50)
        print("These are the game settings by default: ")
        self.printLine("=", 50)
        print self.settingsSudoku.getSudokuGameType()
        print self.settingsSudoku.getSudokuOutputFormat()
        print self.settingsSudoku.getSudokuAlgorithmOption()

    def solveSudokuGame(self, optionAlgorithm):
        """
        This method solves the Sudoku game with selected algorithm by the user.
        """
        if optionAlgorithm == "BackTracking":
            self.solveUsingBackTrackingAlgorithm()
        if optionAlgorithm == "Peter Norvig" :
            self.solveUsingPeterNorvigAlgorithm()
        if optionAlgorithm == "Quick Hackup":
            self.solveUsingQuickHackupAlgorithm()

    def solveUsingBackTrackingAlgorithm(self):
        """
        This method creates an instance of BackTracking algorithm child class
        and solves the game by the string entered.
        """
        backtrackInstance = BacktrackingAlgorithm(self.getSudokuString())
        try:
            backtrackInstance.solveSudoku()
        except:
            self.printSudokuSolved(backtrackInstance.puzzle,
                                backtrackInstance.runningTime)

    def solveUsingPeterNorvigAlgorithm(self):
        """
        This method creates an instance of Peter Norvig algorithm child class
        and solves the game by the string entered.
        """
        peterInstance = PeterNorvigAlgorithm(self.getSudokuString())
        peterInstance.solveSudoku()
        self.printSudokuSolved(peterInstance.solution, peterInstance.runningTime)

    def solveUsingQuickHackupAlgorithm(self):
        """
        This method creates an instance of ForwardCheck algorithm child class
        and solves the game by the string entered.
        """
        forwardInstance = ForwardCheck(self.getSudokuString())
        try:
            forwardInstance.solveSudoku()
        except:
            self.printSudokuSolved(forwardInstance.puzzle, 1)

    def getSudokuString(self):
        """
        This method asks to the user for the Sudoku game to be solved.

        If the option selected is Console, the input expected is a string with
        the matrix unsolved:
        '001093000000100004020060370700000005080504060400000008092080010100009000000340600'

        If the option selected is File, the input expected is the filename
        which contains the matrix unsolved in .txt or .csv format.
        i.e: 'SodukuGame.txt'
        """
        option = self.settingsSudoku.getSudokuOutputFormat()
        if option == "Console":
            return self.getUserInput("Enter the SUDOKU to be solved in a string line")
        if option == "File":
            sudokuFile = SudokuTXTReader(self.getUserInput("Please enter file name with extension"),
                              self.settingsSudoku.getSudokuMatrixDimension())
            if(sudokuFile.isTXTContentValid()):
                return sudokuFile.readSudokuFromTXTFile()
            else:
                print("The format of the file name introduced is not valid.")

    def printSudokuSolved(self, matrixSolved, runningTime):
        """
        This method prints in console the Sudoku solved.

        Keyword arguments:
        matrixSolved -- Matrix array which contains the values of solved game.
        runningTime -- Time spent to solve the game
        """
        self.printLine("=", 50)
        print("      GAME SOLUTION       ")
        self.printLine("=", 50)
        rowStrings = []
        for i in range(9):
            rowString = []
            for j in range(9):
                rowString.append(str(matrixSolved[i][j]) + " ")
            rowStrings.append(self.formatRow(rowString))
        for i in range(0, len(rowStrings), 3):
            for j in range(0, 3):
                print rowStrings[i + j]
            print "--------------------"
        print  "Solution Time: %s" % runningTime

    def formatRow(self, rowString):
        """
        Keyword arguments:
        rowString -- String of the values of a row in the matrix.

        Return:
        String with '|'s inserted every 3 digits; format one row for printing
        the puzzle neatly
        """
        formattedString = ""
        for i in range(0, len(rowString), 3):
            for j in range(0, 3):
                formattedString += rowString[i + j]
            formattedString += "|"
        return formattedString

    def validateInputStringGame(self, toValidateString):
        """
        This method validates the user entry for matrix to be solved.

        Keyword arguments:
        toValidateString -- String with values of the matrix unsolved.

        Return:
        The validation returns True if all the values of the matrix unsolved are
        digits (0-9) and they should be 81 numbers.
        """
        resValidate = False
        if len(toValidateString) == 81 and toValidateString.isdigit():
            resValidate = True
        return resValidate

    def solveGameWithChangedSettings(self):
        """
        This method calls the methods to change the following settings:
        - OutputFormat
        - AlgorithmOption
        Save the changes in the Configuration.xml file and solve the game
        with latest changes.
        """
        self.outputFormatOptionsMenu()
        self.algorithmOptionsMenu()
        self.settingsSudoku.saveCurrentSettings()
        self.displayOptionsSelected()
        self.solveSudokuGame(self.settingsSudoku.getSudokuAlgorithmOption())

    def askForValueUntilIsValid(self, gameOptions):
        """
        This method ensure that user enter a valid value for the number option.

        Keyword arguments:
        gameOptions - List of strings with the list of options for a specific
        setting readed from the .xml file

        Return:
        Value returned is a valid number option.

        """
        optionValid = self.getUserInput("Enter the number of the  option: ")
        while not self.isValidSelectedNumberOption(optionValid, len(gameOptions)):
            print("*****The option selected is not valid****")
            optionValid = self.getUserInput("Enter the number of the  option: ")
        return optionValid

    def displayOptionsToSolveGame(self):
        """
        This method displays the user settings currently stored to 'Solve'
        the Sudoku game in UserConfiguration.xml file or if the user prefers
        change current settings.
        """
        self.displayOptionsSelected()
        optionSolveSettings = self.getUserInput("\
        Do you want to change the settings before solve the game? (Yes/No):")
        if (optionSolveSettings == "Yes" or optionSolveSettings == "yes"):
            self.solveGameWithChangedSettings()
        elif (optionSolveSettings == "No" or optionSolveSettings == "no"):
            self.solveSudokuGame(self.settingsSudoku.getSudokuAlgorithmOption())

    def mainOptionsMenu(self):
        """
        This method displays the main Menu with options for the SUDOKU
        game in console.
        """
        gameOptions = self.settingsSudoku.getSudokuGameTypeOptions()
        self.displayMenuOptions("Sudoku", gameOptions)
        optionValidated = self.askForValueUntilIsValid(gameOptions)
        if(optionValidated == "1"):
            print("The game will be solved ")
            self.displayOptionsToSolveGame()
        elif(optionValidated == "2"):
            print("The game will be generated ")
            self.settingsSudoku.setSudokuGameType("Generate")
        elif(optionValidated == "3"):
            print("Restoring to options by default...")
            self.settingsSudoku.restoreDefaultSettings()
            self.displayOptionsSelected()
        elif(optionValidated == "4"):
            print("Exit")
        else:
            print("Option unknown")