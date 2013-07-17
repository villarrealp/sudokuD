"""
Author: Debbie Rios
Date: 07/04/2013
Modified:  07/17/2013    by: Debbie Rios
Comments: Changes in the methods, follows standards.
"""
"""
Class Name: Algorithm
Description: receive a grid to solve the sudoku
"""

class Algorithm():

    def __init__(self, grids):
        """
        Constructor fo the class Algorthm
        grids: is the sudoku puzzle  without resolve.
        """
        self.grids = grids

    @staticmethod
    def fromFile(filename):
        """
        Static method used to read a file, return the file parsed into a
        string.
        filename: name of the xml file.
        """
        parsedString = file(filename).read()
        return parsedString

    def convertStringToMatrix(self, grids):
        """
        This method receive the grid into a string and return the grid into
        a matrix.
        grids: is the sudoku puzzle  without resolve.
        """
        lisOfValues = []
        matrix = [[0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0],\
                 [0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0], \
                 [0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0]]

        for grid in grids:
            lisOfValues.append(int(grid))
        count = 0
        for x in range(9):
            for y in range(9):
                matrix[x][y] = lisOfValues[count]
                count  = count + 1
        return matrix

