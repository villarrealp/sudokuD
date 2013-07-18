"""
Author: Miguel Haruki Yamaguchi
Date created: 10/13/2009
Description: Sudoku Puzzle Solver
Modified: 07/08/2013 by Pilar Villarreal
                Comments:
                    Use bactracking algorithm from the original file
                    SudokuSolver.py, the code was adapted for the
                    final project.
          07/15/2013 by Pilar Villarreal
                Comments:
                    Removed unused code and comments from original algorithm

Revised by: -

"""
import os
import sys
import copy
import time
from Algorithm import Algorithm
from Queue import PriorityQueue
from Queue import Queue

class BacktrackingAlgorithm(Algorithm):

    def __init__(self, grids):
        """
        Constructor method for the BacktrackingAlgorithm child class.

        Keyword arguments:
        grids -- String which contains the unsolved game, it should have 81
        characters, all of them digits 0-9, for example:
        "008009320000080040900500007000040090000708000060020000600001008050030000072900100"

        Class attributes:
        puzzle -- Matrix of integers, will contain the values of the solved game.
        blanks -- Array of tuples, it contains position of the blank spots
        in follow format: (rowIndex, colIndex)
        runningTime -- Float to store the time taken during algorithm execution.
        """
        Algorithm.__init__(self, grids)

        self.puzzle = []
        self.blanks = []
        self.runningTime = 0

    def solveSudoku(self):
        """
        This method calls the methods to solve the Sudoku game using
        BackTracking Algorithm
        """
        matrixSudoku = self.convertStringToMatrix(self.grids)
        self.puzzle = matrixSudoku
        self.blanks = self.getEmptyCells(self.puzzle)
        self.solve(self.puzzle)

    def solve(self, puzzleArray):
        """
        Solve the Sudoku puzzle using the selected algorithm.

        Keyword arguments:
        puzzleArray -- Matrix of integers with the puzzle unsolved.

        Return:
        This method returns the puzzle solved using BackTracking algorithm.
        """
        print "Solving with backtracking."
        self.runningTime = time.clock()
        self.backTrack(0)
        return self.puzzle

    def backTrack(self, index):
        """
        This method solves the Sudoku puzzle using a recursive algorithm to try
        each value 1-9 in each blank square, backtracking when it was not able
        to put in any value into the square.

        Keyword arguments:
        index -- Integer to access an element in the tuples array of blank spots
        stored at self.blanks attribute.
        """
        if index > len(self.blanks) - 1:
            self.endAlgorithm()

        row = self.blanks[index][0]
        col = self.blanks[index][1]

        for num in range(1, 10):
            if self.puzzleValid(row, col, num):
                self.puzzle[row][col] = num
                self.backTrack(index + 1)

        index -= 1
        self.puzzle[row][col] = 0

    def puzzleValid(self, row, col ,num):
        """
        This method checks if the current puzzle is legal after placing num in
        (row, col).

        Keyword arguments:
        row -- Row number position in the matrix to place num.
        col -- Column number position in the matrix to place num.
        num -- Value to be validated in specified row and column.

        Return:
        This method returns True if row, column, and box have no violations
        to meet Sudoku game rules, false otherwise.
        """
        valid = False
        if num == 0:
            valid = True
        else:
            rowValid = self.checkRow(row, num)
            colValid = self.checkColumn(col, num)
            boxValid = self.checkBox(row, col, num)
            valid = (rowValid & colValid & boxValid)
        return valid

    def checkRow(self, row, num ):
        """
        This method checks if num is a legal value for the given row.

        Keyword arguments:
        row -- Row number position in the matrix to place num.
        num -- Value to be validated in specified row.

        Return:
        This method returns True if num placed in row specified is a legal
        value, false otherwise.
        """
        for col in range(9):
            currentValue = self.puzzle[row][col]
            if num == currentValue:
                return False
        return True

    def checkColumn(self, col, num):
        """
        This method checks if num is a legal value for the given column.

        Keyword arguments:
        col -- Column number position in the matrix to place num.
        num -- Value to be validated in specified column.

        Return:
        This method returns True if num placed in column specified is a
        legal value, false otherwise.
        """
        for row in range(9):
            currentValue = self.puzzle[row][col]
            if num == currentValue:
                return False
        return True

    def checkBox(self, row, col, num):
        """
        This method checks if num is a legal value for the box (one of 9 boxes
        of the matrix) containing given row and column.

        Keyword arguments:
        row -- Row number position in the matrix to place num.
        col -- Column number position in the matrix to place num.
        num -- Value to be validated in specified row and column.

        Return:
        This method returns True if num placed in row and column specified
        is a legal value in the box where belongs, false otherwise.
        """
        row = (row / 3) * 3
        col = (col / 3) * 3

        for rowIndex in range(3):
            for colIndex in range(3):
                if self.puzzle[row + rowIndex][col + colIndex] == num:
                    return False
        return True

    def endAlgorithm(self):
        """
        Method to end the algorithm in process, calculate the running
        time and exit.
        """
        self.runningTime = time.clock() - self.runningTime
        sys.exit(0)

    def getEmptyCells(self, puzzle):
        """
        This method searchs for the empty places in the matrix (the places with
        0 as value) and store its position (row, column) in the emptyCells array.

        Keyword arguments:
        puzzle -- Matrix of integers which contains unsolved game.

        Return:
        This method returns an array of tuples with the positios of empty
        places of the unsolved matrix.
        i.e.: [(row, colum)]  = [(3, 2)]
        """
        emptyCells = []
        for row in range(9):
            for column in range(9):
                if self.puzzle[row][column] == 0:
                    emptyCells.append((row, column))
        return emptyCells

    def initPuzzleArray(self):
        """
        This method constructs the blank puzzle array to have 0 0 0 0 0...
        for all rows and columns
        """
        del self.puzzle[:]
        for row in range(9):
            self.puzzle.append([])
            for col in range(9):
                self.puzzle[row].append([])
                self.puzzle[row][col] = 0