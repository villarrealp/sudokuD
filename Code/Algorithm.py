"""
Author: Debbie Rios
Date: 07/04/2013
Modified:  07/18/2013    by: Debbie Rios
Comments: Changes in the methods, follows standards.
"""
"""
Class Name: Algorithm
Description: receive string with the grid to solve the sudoku
"""

class Algorithm():

    def __init__(self, grids):
        """
        Constructor fo the class Algorithm.

        Keyword arguments:
        grids -- string with grid of the sudoku to resolve, 81 non-blank
        chars e.g "00302060...."
        """
        self.grids = grids

    @staticmethod
    def fileToString(filename):
        """
        Static method used to read a file.

        Keyword arguments:
        filename: name of file e.g 'sudoku.txt'.

        Return:
        the file parsed into a string e.g. {012008900\n236100789\n.....}
        """
        parsedString = file(filename).read()
        return parsedString

    def convertStringToMatrix(self, grids):
        """
        This method receive the grid into a string.

        Keyword arguments:
        grid -- the grid of the sudoku  to resolve. e.g "00302060...."

        Return:
        the grid into a matrix e.g [ [0,0,3,0,2,0,6,0,8], [1,0,0,4,5,6,0,8,,], ...., []]
        """
        lisOfValues = []
        matrix = [[0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0]]

        for grid in grids:
            lisOfValues.append(int(grid))
        count = 0
        for row in range(9):
            for col in range(9):
                matrix[row][col] = lisOfValues[count]
                count  = count + 1
        return matrix

