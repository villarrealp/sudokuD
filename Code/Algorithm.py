"""
Author: Debbie Rios
Date: 07/04/2013
Modified:  07/16/2013    by: Debbie Rios
                Comments: Changes into domentation, follow stardars.
Revised by:               by:

"""
"""
Class Name: Algorithm
Description:
"""

class Algorithm():

    def __init__(self, grids):
        """
        Constructor fo the class Algorthm
        Grid is the sudoku puzzle  without resolve.
        """
        self.grids = grids

    @staticmethod
    def fromFile(filename):
        """
        Static method using to read a file, return the file parsed into a
        string.
        """
        parsedString = file(filename).read()
        return parsedString

    def convertStringToMatrix(self, grids):
        lisOfValues =[]
        matrix = [[0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0],\
                 [0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0], \
                 [0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0]]
        for n in grids:
            lisOfValues.append(int(n))
        contador = 0

        for x in range(9):
            for y in range(9):
                matrix[x][y] = lisOfValues[contador]
                contador  = contador +1
        return matrix
