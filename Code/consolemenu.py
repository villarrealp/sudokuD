"""
Author: Pilar Villarreal
Date created:   07/03/2013
Modified:       07/04/2013 by Pilar Villarreal
                Comments: Working on refactoring methods.
Revised by: -

"""

import sys

from settings import Settings

"""
Class Name: ConsoleMenu

Description: This clase displays the menu options for the game extracted from
             the XML file.
"""

class ConsoleMenu:

        def __init__(self, fileName):            
                """ Constructor method for the ConsoleMenu class. """                
                self.settingsSudoku = Settings(fileName)                
        
        def getAStringLine(self, charDraw, length):
                """
                This method returns a string simulating a line using
                specified char in parameters.
                """
                line = charDraw        
                for index in range(length):
                        line = line + charDraw
                return line
        
        def drawMenuOptions(self, title, listOfOptions):
                """
                This method draws in console the Menu for a list of options
                extracted from the XML file.
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
                """
                This method returns a string with the value entered by the
                user.                
                """
                userInput = raw_input("Enter the number of the option: ")                
                return int(userInput)

        def validateUserInput(self, optionSelected, numberOptions):
                """
                This method returns a boolean value, validating the value
                entered by the user against the number of options allowed.                
                """     
                res = False
                try:
                        option = optionSelected
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
                while not self.validateUserInput(optionSelected,
                                                 len(gameOptions)):
                        print("*****The option selected is not valid****")
                        optionSelected = self.getUserInput()
                if(optionSelected == 1):                        
                        print("The game will be solved ")
                        self.settingsSudoku.setSudokuGameType("Solve")
                elif(optionSelected == 2):
                        print("The game will be generated ")
                        self.settingsSudoku.setSudokuGameType("Generate")
                elif(optionSelected == 3):
                        self.difficultyLevelOptionsMenu()
                        self.outputFormatOptionsMenu()
                        self.algorithmOptionsMenu()
                        self.settingsSudoku.saveCurrentSettings()
                elif(optionSelected == 4):
                        print("Exit")
                else:
                        print("Option unknown")
        
                        
        def difficultyLevelOptionsMenu(self):
                """
                This method displays the Menu options for Difficulty Levels 
                """
                difficultyLevelOptions = self.settingsSudoku.\
                                         getSudokuDifficultyLevelOptions()
                self.drawMenuOptions("Change settings options",
                                     difficultyLevelOptions)
                optionSelected = self.getUserInput()                
                while not self.validateUserInput(optionSelected,
                                                 len(difficultyLevelOptions)):
                        print("*****The option selected is not valid****")
                        optionSelected2 = self.getUserInput()
                if(optionSelected == 1):
                        print("Easy")
                        self.settingsSudoku.setSudokuDifficultyLevel("Easy")
                elif(optionSelected == 2):
                        print("Medium")
                        self.settingsSudoku.setSudokuDifficultyLevel("Medium")
                elif(optionSelected == 3):
                        print("Hard")
                        self.settingsSudoku.setSudokuDifficultyLevel("Hard")
                        

        def outputFormatOptionsMenu(self):
                """
                This method displays the Menu options for Output formats
                """
                outputFormatOptions = self.settingsSudoku.\
                                      getSudokuOutputFormatOptions()
                self.drawMenuOptions("Change output type format",
                                     outputFormatOptions)
                optionSelected = self.getUserInput()
                while not self.validateUserInput(optionSelected,
                                                 len(outputFormatOptions)):
                        print("*****The option selected is not valid****")
                        optionSelected = self.getUserInput()
                if(optionSelected == 1):
                        print("Console")
                        self.settingsSudoku.setSudokuOutputFormat("Console")
                elif (optionSelected == 2):                        
                        print("File")
                        self.settingsSudoku.setSudokuOutputFormat("File")
                        userInputNameFile = raw_input(\
                                "Enter a name for the outuput file: ")
                        userInputPathFile = raw_input(\
                                "Enter the specific path to store the file: ")
                                
        def algorithmOptionsMenu(self):
                """
                This method displays the Menu options for Algorithms available 
                """
                algorithmOptions = self.settingsSudoku.\
                                   getSudokuAlgorithmSolutionOptions()
                self.drawMenuOptions("Change algorithm used", algorithmOptions)
                optionSelected = self.getUserInput()
                while not self.validateUserInput(optionSelected,
                                                 len(algorithmOptions)):
                        print("*****The option selected is not valid****")
                        optionSelected = self.getUserInput()
                if(optionSelected == 1):
                        print("BackTracking")
                        self.settingsSudoku.setSudokuAlgorithmOption(\
                                "BackTracking")
                elif (optionSelected == 2):                        
                        print("Peter Norvig")
                        self.settingsSudoku.setSudokuAlgorithmOption(\
                                "Peter Norvig")
                elif (optionSelected == 3):                              
                        print("Exact")
                        self.settingsSudoku.setSudokuAlgorithmOption(\
                                "Exact")      
          
        def displayOptionsSelected(self):
                """
                This method displays options selected by the user 
                """
                
                print self.getAStringLine("=", 50)
                print("Following options were selected by the user: ")
                print self.getAStringLine("=", 50)
                print self.settingsSudoku.getSudokuGameType()                
                print self.settingsSudoku.getSudokuDifficultyLevel()                
                print self.settingsSudoku.getSudokuOutputFormat()
                print self.settingsSudoku.getSudokuAlgorithmOption()
                              
  
