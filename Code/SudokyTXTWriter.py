"""
Author: Pilar Villarreal
Date created: 07/18/2013
Description: This class creates a .txt file with generated unsolved game.

Modified:
                Comments:
Revised by:

"""
import sys
from itertools import count

"""
Class Name: SudokuTXTWriter

Description: This class uses the Settings extracted from the XML files and
             displays the menu options for the game in the console.
"""
class SudokuTXTWriter:
    def __init__(self, matrix):
        self.writeToTXTFile("myTestGenerated.txt", matrix)


    def writeToTXTFile(self, fileName , matrixGenerated):
        """
        This method writes the generated matrix to a .txt file.

        Keyword strings:
        filename -- Name to be used to generate the game.
        matrixGenerated -- Matrix of chars to be stored in a .txt file
        """
        outFile = open(fileName, 'w')
        for i in range(9):
            rowString = ""
            for j in range(9):
                rowString += str(matrixGenerated[i][j])+" "
            outFile.write(rowString+'\n')
        outFile.close()

    def generateNameForFile(self):
        """
        This method will generate a name for the files which contains the
        generated matrix.
        """
        return " "


