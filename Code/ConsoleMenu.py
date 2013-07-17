"""
Author: Pilar Villarreal
Date created:   07/03/2013
Modified:       07/04/2013 by Pilar Villarreal
                Comments: Working on refactoring methods.
                07/15/2013 by Pilar Villarreal
                Comments: Updated due to last changes to Settings class,
                added comments to methods to display the solved matrix.
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

Description: This clase displays the menu options for the game extracted from
             the XML file.
"""

class ConsoleMenu:

    def __init__(self, userSettings, defaultSettings):
        """ Constructor method for the ConsoleMenu class. """
        self.settingsSudoku = Settings(userSettings, defaultSettings)

    def getAStringLine(self, charDraw, length):
        """
        This method returns a string simulating a line using specified char in
        parameters.
        """
        line = charDraw
        for index in range(length):
            line = line + charDraw
        return line

    def drawMenuOptions(self, title, listOfOptions):
        """
        This method draws in console the Menu for a list of options extracted
        from the XML file.
        """
        print self.getAStringLine("=", 50)
        print self.getAStringLine(" ", 20) + title
        print self.getAStringLine("=", 50)
        print("         Please select an option:")
        index = 1
        for option in listOfOptions:
            print("                 " + str(index) + ". " + option
                  + "                ")
            index = index + 1

    def getUserInput(self):
        """ This method returns a string with the value entered by the user. """
        userInput = raw_input("Enter the number of the  option: ")
        return userInput

    def validateUserInput(self, optionSelected, numberOptions):
        """
        This method returns a boolean value, validating the value entered by
        the user against the number of options allowed.
        """
        res = False
        try:
            option = int(optionSelected)
            if(option <= numberOptions and option > 0):
                res = True
        except ValueError, e :
            print("'%s' is not a valid number of option."
                  % e.args[0].split(": ")[1])
        return res

    def mainOptionsMenu(self):
        """
        This method displays the complete Menu of options for the
        SUDOKU
        """
        gameOptions = self.settingsSudoku.getSudokuGameTypeOptions()
        self.drawMenuOptions("Sudoku", gameOptions)
        optionSelected = self.getUserInput()
        while not self.validateUserInput(optionSelected, len(gameOptions)):
            print("*****The option selected is not valid****")
            optionSelected = self.getUserInput()
        if(optionSelected == "1"):
            print("The game will be solved ")
            self.displayOptionsSelected()
            optionSolveSettings = raw_input("\
            Do you want to change the settings before solve the game? (Yes/No):")
            if (optionSolveSettings == "Yes" or optionSolveSettings == "yes"):
                self.outputFormatOptionsMenu()
                self.algorithmOptionsMenu()
                self.settingsSudoku.saveCurrentSettings()
                self.displayOptionsSelected()
                self.solveSudokuGame(self.settingsSudoku.getSudokuAlgorithmOption())
            elif (optionSolveSettings == "No" or optionSolveSettings == "no"):
                self.solveSudokuGame(self.settingsSudoku.getSudokuAlgorithmOption())
        elif(optionSelected == "2"):
            print("The game will be generated ")
            self.settingsSudoku.setSudokuGameType("Generate")
        elif(optionSelected == "3"):
            print("Restoring to options by default...")
            self.settingsSudoku.restoreDefaultSettings()
            self.displayOptionsSelected()
        elif(optionSelected == "4"):
            print("Exit")
        else:
            print("Option unknown")

    def difficultyLevelOptionsMenu(self):
        """ This method displays the Menu options for Difficulty Levels. """
        difficultyLevelOptions = self.settingsSudoku.\
                                 getSudokuDifficultyLevelOptions()
        self.drawMenuOptions("Change settings options", difficultyLevelOptions)
        optionSelected = self.getUserInput()
        while not self.validateUserInput(optionSelected,
                                         len(difficultyLevelOptions)):
            print("*****The option selected is not valid****")
            optionSelected2 = self.getUserInput()
        if(optionSelected == "1"):
            print("Easy")
            self.settingsSudoku.setSudokuDifficultyLevel("Easy")
        elif(optionSelected == "2"):
            print("Medium")
            self.settingsSudoku.setSudokuDifficultyLevel("Medium")
        elif(optionSelected == "3"):
            print("Hard")
            self.settingsSudoku.setSudokuDifficultyLevel("Hard")

    def outputFormatOptionsMenu(self):
        """ This method displays the Menu options for Output formats. """
        outputFormatOptions = self.settingsSudoku.\
                              getSudokuOutputFormatOptions()
        self.drawMenuOptions("Change input type format", outputFormatOptions)
        optionSelected = self.getUserInput()
        while not self.validateUserInput(optionSelected,
                                         len(outputFormatOptions)):
            print("*****The option selected is not valid****")
            optionSelected = self.getUserInput()
        if(optionSelected == "1"):
            print("Console")
            self.settingsSudoku.setSudokuOutputFormat("Console")
        elif (optionSelected == "2"):
            print("File")
            self.settingsSudoku.setSudokuOutputFormat("File")

    def algorithmOptionsMenu(self):
        """
        This method displays the Menu options for Algorithms available.
        """
        algorithmOptions = self.settingsSudoku.\
                           getSudokuAlgorithmSolutionOptions()
        self.drawMenuOptions("Change algorithm used", algorithmOptions)
        optionSelected = self.getUserInput()
        while not self.validateUserInput(optionSelected,
                                         len(algorithmOptions)):
            print("*****The option selected is not valid****")
            optionSelected = self.getUserInput()
        if(optionSelected == "1"):
            print("BackTracking")
            self.settingsSudoku.setSudokuAlgorithmOption("BackTracking")
        elif (optionSelected == "2"):
            print("Peter Norvig")
            self.settingsSudoku.setSudokuAlgorithmOption("Peter Norvig")
        elif (optionSelected == "3"):
            print("Exact")
            self.settingsSudoku.setSudokuAlgorithmOption("Exact")

    def displayOptionsSelected(self):
        """ This method displays options selected by the user """
        print self.getAStringLine("=", 50)
        print("These are the game settings selected: ")
        print self.getAStringLine("=", 50)
        print self.settingsSudoku.getSudokuGameType()
        print self.settingsSudoku.getSudokuOutputFormat()
        print self.settingsSudoku.getSudokuAlgorithmOption()

    def displayOptionsSelectedByDefault(self):
        """ This method displays options selected by default """
        print self.getAStringLine("=", 50)
        print("These are the game settings by default: ")
        print self.getAStringLine("=", 50)
        print self.settingsSudoku.getSudokuGameType()
        print self.settingsSudoku.getSudokuOutputFormat()
        print self.settingsSudoku.getSudokuAlgorithmOption()

    def solveSudokuGame(self, option):
        """
        This method call to the respective class algorithm to solve a Sudoku
        game depending on the option selected.
        """
        if option == "BackTracking":
            self.solveUsingBackTrackingAlgorithm()
        if option == "Peter Norvig" :
            self.solveUsingPeterNorvigAlgorithm()
        if option == "Exact":
            self.solveUsingQuickHackupAlgorithm()

    def solveUsingBackTrackingAlgorithm(self):
        """
        This method create a instance of BackTracking algorithm class and
        solve the game by the string entered.
        """
        backtrackInstance = BacktrackingAlgorithm(self.getSudokuString())
        try:
            backtrackInstance.solveSudoku()
        except:
            self.printSudokuSolved(backtrackInstance.puzzle,
                                backtrackInstance.runningTime)

    def solveUsingPeterNorvigAlgorithm(self):
        """
        This method create a instance of Peter Norvig algorithm class and
        solve the game by the string entered.
        """
        peterInstance = PeterNorvigAlgorithm(self.getSudokuString())
        peterInstance.solveSudoku()
        self.printSudokuSolved(peterInstance.solution, peterInstance.runningTime)

    def solveUsingQuickHackupAlgorithm(self):
        """
        This method create a instance of ForwardCheck algorithm class and
        solve the game by the string entered.
        """
        quickInstance = ForwardCheck(self.getSudokuString())
        try:
            quickInstance.solveSudoku()
        except:
            self.printSudokuSolved(quickInstance.puzzle, 20)

    def getSudokuString(self):
        """
        This method ask to the user for the Sudoku game to be solved depending
        of the InputFormat selected from settings.
        """
        option = self.settingsSudoku.getSudokuOutputFormat()
        if option == "Console":
            return raw_input("Enter the SUDOKU to be solved in a string line")
        if option == "File":
            sudokufile = SudokuTXTReader(raw_input("Please enter file name with extension"),
                              self.settingsSudoku.getSudokuMatrixDimension())
            if(sudokufile.isTXTContentValid()):
                return sudokufile.readSudokuFromTXTFile()
            else:
                print("The format of the file name introduced is not valid.")

    def printSudokuSolved(self, matrixSolved, runningTime):
        """
        Prints the puzzle as a visual representation.
        """
        print self.getAStringLine("=", 50)
        print("      GAME SOLUTION       ")
        print self.getAStringLine("=", 50)
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
        Return a string with '|'s inserted every 3 digits; format one row
        for printing the puzzle neatly
        """
        formattedString = ""
        for i in range(0, len(rowString), 3):
            for j in range(0, 3):
                formattedString += rowString[i + j]
            formattedString += "|"
        return formattedString

    def validateInputStringGame(self, toValidateString):
        """ This method validates the user entry for matrix to be solved. """
        resValidate = False
        if len(toValidateString) == 81 and toValidateString.isdigit():
            resValidate = True
        return resValidate