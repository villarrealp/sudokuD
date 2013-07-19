"""
Author: Debbie Rios
Date: 07/04/2013
Modified:   07/16/2013   by: Debbie Rios
Comments: Changes following standard, and comments from Edson Gonzales

"""
import unittest

import os, sys
lib_path = os.path.abspath('../')
sys.path.append(lib_path)

from Algorithm import Algorithm
from PeterNorvigAlgorithm import PeterNorvigAlgorithm

class PeterNorvigAlgorithm(unittest.TestCase):

    def setUp(self):
        grid  = '0030206009003050010018064000081029007000000080067082000026095\
                 00800203009005010300'
        self.sudoku = PeterNorvigAlgorithm(grid)
        self.digits   = '123456789'
        self.rows     = 'ABCDEFGHI'
        self.cols     = self.digits

    def testCrossMethodReturnSquareOf81Characters(self):
       square = self.sudoku.cross(self.rows, self.cols)
       expectedResults = ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9',
                          'B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'B9',
                          'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9',
                          'D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9',
                          'E1', 'E2', 'E3', 'E4', 'E5', 'E6', 'E7', 'E8', 'E9',
                          'F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'F9',
                          'G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'G7', 'G8', 'G9',
                          'H1', 'H2', 'H3', 'H4', 'H5', 'H6', 'H7', 'H8', 'H9',
                          'I1', 'I2', 'I3', 'I4', 'I5', 'I6', 'I7', 'I8', 'I9']
       self.assertEqual (expectedResults, square)

    def testGridHas81Leng(self):
        lenSquare = len(self.sudoku.squares)
        self.assertEqual(lenSquare, 81)

    def testUnitlistHas27Peers(self):
        lenUnitlist = len(self.sudoku.unitlist)
        self.assertEqual( lenUnitlist, 27)


    def testIfAllUnitsHaveOneRowColsandSquareAsPeer(self):
        expectedResults = [['A2', 'B2', 'C2', 'D2', 'E2', 'F2', 'G2', 'H2', 'I2'],
                           ['C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9'],
                           ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']]

        self.assertEqual(self.sudoku.units['C2'], expectedResults)

    def testIfAnyUnitHas20Peers(self):
        expectedResults = set(['A2', 'B2', 'D2', 'E2', 'F2', 'G2', 'H2', 'I2',
                               'C1', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9',
                               'A1', 'A3', 'B1', 'B3'])
        self.assertEqual(self.sudoku.peers['C2'], expectedResults)

    def testIfParseGridMethodReturnADictionary(self):
        grid  = '0030206009003050010018064000081029007000000080067082000026095\
                 00800203009005010300'
        sudoku = self.sudoku.parseGrid(grid)
        expectedResults = {'I6': '7', 'H9': '9', 'I2': '9', 'E8': '3', 'H3': '4',
                           'H7': '7', 'I7': '3', 'I4': '4', 'H5': '5', 'F9': '5',
                           'G7': '5', 'G6': '9', 'G5': '8', 'E1': '7', 'G3': '2',
                           'G2': '7', 'G1': '3', 'I1': '6', 'C8': '9', 'I3': '5',
                           'E5': '6', 'I5': '1', 'C9': '3', 'G9': '4', 'G8': '1',
                           'A1': '4', 'A3': '3', 'A2': '8', 'A5': '2', 'A4': '9',
                            'A7': '6', 'A6': '1','C3': '1', 'C2': '5', 'C1': '2',
                           'E6': '4', 'C7': '4', 'C6': '6', 'C5': '7', 'C4': '8',
                            'I9': '2', 'D8': '7', 'I8': '8', 'E4': '5', 'D9': '6',
                            'H8': '6', 'F6': '8', 'A9': '7', 'G4': '6', 'A8': '5',
                            'E7': '1', 'E3': '9', 'F1': '1', 'F2': '3', 'F3': '6',
                            'F4': '7', 'F5': '9', 'E2': '2', 'F7': '2', 'F8': '4',
                            'D2': '4', 'H1': '8', 'H6': '3', 'H2': '1', 'H4': '2',
                            'D3': '8', 'B4': '3', 'B5': '4', 'B6': '5', 'B7': '8',
                            'E9': '8', 'B1': '9','B2': '6', 'B3': '7', 'D6': '2',
                            'D7': '9', 'D4': '1', 'D5': '3', 'B8': '2', 'B9': '1',
                            'D1': '5'}
        self.assertDictEqual (expectedResults, sudoku)

    def testIfGridValuesMethodReturnGridMapaAsDic(self):
        grid = '0030206009003050010018064000081029007000000080067082000026095\
                00800203009005010300'
        sudoku = self.sudoku.gridValues(grid)
        expectedResults =   {'I6': '0', 'H9': '9', 'I2': '0', 'E8': '0', 'H3': '0',
                             'H7': '0', 'I7': '3', 'I4': '0', 'H5': '0','F9': '0',
                             'G7': '5', 'G6': '9', 'G5': '0', 'E1': '7', 'G3': '2',
                             'G2': '0', 'G1': '0', 'I1': '0', 'C8': '0', 'I3': '5',
                             'E5': '0', 'I5': '1', 'C9': '0', 'G9': '0', 'G8': '0',
                             'A1': '0', 'A3': '3', 'A2': '0', 'A5': '2', 'A4': '0',
                             'A7': '6', 'A6': '0', 'C3': '1', 'C2': '0', 'C1': '0',
                             'E6': '0', 'C7': '4', 'C6': '6', 'C5': '0', 'C4': '8',
                             'I9': '0', 'D8': '0', 'I8': '0', 'E4': '0', 'D9': '0',
                             'H8': '0', 'F6': '8', 'A9': '0', 'G4': '6', 'A8': '0',
                             'E7': '0', 'E3': '0', 'F1': '0', 'F2': '0','F3': '6',
                             'F4': '7', 'F5': '0', 'E2': '0', 'F7': '2', 'F8': '0',
                             'D2': '0', 'H1': '8', 'H6': '3', 'H2': '0', 'H4': '2',
                             'D3': '8', 'B4': '3', 'B5': '0', 'B6': '5', 'B7': '0',
                             'E9': '8', 'B1': '9','B2': '0', 'B3': '0', 'D6': '2',
                             'D7': '9', 'D4': '1', 'D5': '0', 'B8': '0', 'B9': '1',
                             'D1': '0'}
        self.assertEqual (expectedResults, sudoku)

    def testIfSolveSudokuMethosReturnSudokuResolved(self):
         grid = '0030206009003050010018064000081029007000000080067082000026095\
                 00800203009005010300'
         sudoku = self.sudoku.solve(grid)
         expectedResults = {'I6': '7', 'H9': '9', 'I2': '9', 'E8': '3', 'H3': '4',
                            'H7': '7', 'I7': '3', 'I4': '4', 'H5': '5','F9': '5',
                            'G7': '5', 'G6': '9', 'G5': '8', 'E1': '7', 'G3': '2',
                            'G2': '7', 'G1': '3', 'I1': '6', 'C8': '9', 'I3': '5',
                            'E5': '6', 'I5': '1', 'C9': '3', 'G9': '4', 'G8': '1',
                            'A1': '4', 'A3': '3', 'A2': '8', 'A5': '2', 'A4': '9',
                            'A7': '6', 'A6': '1', 'C3': '1', 'C2': '5', 'C1': '2',
                            'E6': '4','C7': '4', 'C6': '6', 'C5': '7', 'C4': '8',
                            'I9': '2', 'D8': '7', 'I8': '8', 'E4': '5', 'D9': '6',
                            'H8': '6', 'F6': '8', 'A9': '7', 'G4': '6', 'A8': '5',
                            'E7': '1', 'E3': '9', 'F1': '1', 'F2': '3','F3': '6',
                            'F4': '7', 'F5': '9', 'E2': '2', 'F7': '2', 'F8': '4',
                            'D2': '4', 'H1': '8', 'H6': '3', 'H2': '1', 'H4': '2',
                            'D3': '8', 'B4': '3', 'B5': '4', 'B6': '5', 'B7': '8',
                            'E9': '8', 'B1': '9', 'B2': '6', 'B3': '7', 'D6': '2',
                            'D7': '9', 'D4': '1', 'D5': '3', 'B8': '2', 'B9': '1',
                            'D1': '5'}

         self.assertDictEqual(sudoku, expectedResults)

if __name__ == '__main__':
	unittest.main()
