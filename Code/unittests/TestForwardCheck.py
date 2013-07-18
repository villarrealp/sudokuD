"""
Author: Alvaro Avila
Date created: 07/15/2013
Description: Unit tests for the sudokuSolver
Modified:
                Comments:

Revised by: -

"""

import unittest
import os, sys
lib_path = os.path.abspath('../')
sys.path.append(lib_path)

from ForwardCheck import ForwardCheck

class TestForwardCheck(unittest.TestCase):

    def setUp(self):
        self.matrixSolved = [[4,8,3,9,2,1,6,5,7],
                            [9,6,7,3,4,5,8,2,1],
                            [2,5,1,8,7,6,4,9,3],
                            [5,4,8,1,3,2,9,7,6],
                            [7,2,9,5,6,4,1,3,8],
                            [1,3,6,7,9,8,2,4,5],
                            [3,7,2,6,8,9,5,1,4],
                            [8,1,4,2,5,3,7,6,9],
                            [6,9,5,4,1,7,3,8,2]]

        self.solveSudoku = ForwardCheck("0030206009003050010018064000081029007"
                            + "00000008006708200002609500800203009005010300")

    def testSolutionMatrixUsingForwardCheckAlgorithm(self):
        try:
            self.solveSudoku.solveSudoku()
        except:
            self.assertEqual(self.matrixSolved, self.solveSudoku.puzzle)

    def testCheckRowReturnFalseForAExistentNumber(self):
        self.assertFalse(self.solveSudoku.checkRow(4,7))

    def testCheckRowReturnTrueForANonExistentNumber(self):
        self.assertTrue(self.solveSudoku.checkRow(4,3))

    def testCheckColReturnFalseForAExistentNumber(self):
        self.assertFalse(self.solveSudoku.checkColumn(2,3))

    def testCheckColReturnTrueForANonExistentNumber(self):
        self.assertTrue(self.solveSudoku.checkColumn(2,4))

    def testCheckBoxReturnFalseForAExistentNumber(self):
        self.assertFalse(self.solveSudoku.checkBox(2,2,1))

    def testCheckBoxReturnTrueForANonExistentNumber(self):
        self.assertTrue(self.solveSudoku.checkBox(2,2,4))

    def testGetEmptyCellReturnTrueForAEmptyCell(self):
        listOfEmptySpacesForMatrix = [(0, 0),(0, 1),(0, 3),(0, 5),(0, 7),
                                      (0, 8), (1, 1), (1, 2), (1, 4), (1, 6),
                                      (1, 7), (2, 0), (2, 1), (2, 4), (2, 7),
                                      (2, 8), (3, 0), (3, 1), (3, 4), (3, 7),
                                      (3, 8), (4, 1), (4, 2), (4, 3), (4, 4),
                                      (4, 5), (4, 6), (4, 7), (5, 0), (5, 1),
                                      (5, 4), (5, 7), (5, 8), (6, 0), (6, 1),
                                      (6, 4), (6, 7), (6, 8), (7, 1), (7, 2),
                                      (7, 4), (7, 6), (7, 7), (8, 0), (8, 1),
                                      (8, 3), (8, 5), (8, 7), (8, 8)]
        listOfEmptySpaces = self.solveSudoku.getEmptyCells(self.solveSudoku.puzzle)
        self.assertEqual(listOfEmptySpacesForMatrix, listOfEmptySpaces)


    def testInitPuzzleShouldHaveOnlyZeros(self):
        matrixInitialized = [[0,0,0,0,0,0,0,0,0],
                            [0,0,0,0,0,0,0,0,0],
                            [0,0,0,0,0,0,0,0,0],
                            [0,0,0,0,0,0,0,0,0],
                            [0,0,0,0,0,0,0,0,0],
                            [0,0,0,0,0,0,0,0,0],
                            [0,0,0,0,0,0,0,0,0],
                            [0,0,0,0,0,0,0,0,0],
                            [0,0,0,0,0,0,0,0,0]]
        self.solveSudoku.initPuzzleArray()

        self.assertEqual(matrixInitialized, self.solveSudoku.puzzle)

if __name__ == '__main__':
    unittest.main()



