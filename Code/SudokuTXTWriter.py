"""
Author: Pilar Villarreal
Date created: 07/18/2013
Description: This class creates a .txt file with a generated unsolved game.

Modified:
                Comments:
Revised by:

"""

import datetime

"""
Class Name: SudokuTXTWriter

Description: This class creates a .txt file with a generated unsolved game.

Attributes:

matrixGenerated -- Matrix of chars to be stored in a .txt file
"""
class SudokuTXTWriter:

    def __init__(self, matrix):
        """
        This method initialize the SudokuTXTWriter class.

        Keyword string:
        matrix -- Matrix of chars which contains a generated Sudoku Game
        """
        self.matrixGenerated = matrix

    def writeToTXTFile(self):
        """
        This method writes the generated matrix to a .txt file using a generated
        name for the file.
        """
        nameGenerated = self.generateNameForFile()
        outFile = open(nameGenerated, 'w')
        for i in range(9):
            rowString = ""
            for j in range(9):
                rowString += str(self.matrixGenerated[i][j])+" "
            outFile.write(rowString+'\n')
        outFile.close()
        print("File named: %s was created." %nameGenerated)

    def generateNameForFile(self):
        """
        This method will generate a name for the file which contains generated
        Sudoku game.
        The name generated will be based on datetime to avoid duplicates.

        Return:
        String of the file name generated.
        """
        basename = "Generated"
        suffix = datetime.datetime.now().strftime("%y-%m-%d_%H%M%S")
        fileName = "_".join([basename, suffix])
        return fileName