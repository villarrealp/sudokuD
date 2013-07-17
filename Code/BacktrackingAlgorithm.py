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
                    Removed unncesary code, comments from original algorithm

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
        This method initializes the BacktrackingAlgorithm.

        Attributes:

        puzzle - Matrix which contains the values of the solved game.
        blanks - Array which contain blank spots
        runningTime - Store the time taken during algorithm execution

        """
        Algorithm.__init__(self,grids)

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
        """ Solve the Sudoku puzzle using the selected algorithm. """
        print "Solving with backtracking."
        self.runningTime = time.clock()
        self.backTrack(0)
        return self.puzzle

    def backTrack(self, index):
        """
        Solve Sudoku using plain backtracking
        Uses a recursive algorithm to try each value 1-9 in each blank square,
        backtracking when it was not able to put in any value into the square.
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
        Check if the current puzzle is legal after placing num in (row, col)
        The "heur" option is to bypass the constraint check increment
        when using this method for a heuristic, in which case the
        heuristic usage shouldn't count toward the constraint checks.
        """
        valid = False
        if num == 0:
            return True
        else:
            #Return true if row, column, and box have no violations
            rowValid = self.checkRow(row, num)
            colValid = self.checkColumn(col, num)
            boxValid = self.checkBox(row, col, num)
            valid = (rowValid & colValid & boxValid)
        return valid

    def checkRow(self, row, num ):
        """ Check if num is a legal value for the given row. """
        for col in range(9):
            currentValue = self.puzzle[row][col]
            if num == currentValue:
                return False
        return True

    def checkColumn(self, col, num ):
        """ Check if num is a legal value for the given column. """
        for row in range(9):
            currentValue = self.puzzle[row][col]
            if num == currentValue:
                return False
        return True

    def checkBox(self, row, col, num):
        """
        Check if num is a legal value for the box (one of 9 boxes)
        containing given row/col
        """
        row = (row/3) * 3
        col = (col/3) * 3

        for r in range(3):
            for c in range(3):
                if self.puzzle[row + r][col + c] == num:
                    return False
        return True

    def endAlgorithm(self):
        """
        Generic method to end the algorithm in process, calculate the running
        time, output the solution file, print the metrics and exit.
        """
        self.runningTime = time.clock() - self.runningTime
        sys.exit(0)

    def getEmptyCells(self, puzzle):
        """
        Get all the empty cells in the puzzle.
        """
        emptyCells = []
        for i in range(9):
            for j in range(9):
                if self.puzzle[i][j] == 0:
                    emptyCells.append((i, j))
        return emptyCells

    def initPuzzleArray(self):
        """
        Constructs the blank puzzle array to have 0 0 0 0 0...for all rows
        and columns
        """
        del self.puzzle[:]
        for i in range(9):
            self.puzzle.append([])
            for j in range(9):
                self.puzzle[i].append([])
                self.puzzle[i][j] = 0