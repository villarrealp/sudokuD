"""
Author: Miguel Haruki Yamaguchi
Date created: 10/13/2009
Description: Sudoku Puzzle Solver
Modified: 07/08/2013 by Alvaro avila
                Comments:
                    Use forward check algorithm from this code adapted for the
                    final project.

Revised by: -

"""
import os
import sys
import copy
import time

from Algorithm import Algorithm
from Queue import PriorityQueue
from Queue import Queue

class ForwardCheck(Algorithm):

    def __init__(self, grids):
        """
        Constructs a Forward Check algorithm structure containing the elements
        necesary to perform solution of a sudoku board.

        Keyword arguments:
        grids -- String line(grids), with this parameter value initializes
                     the sudoku board and built the sudoku matrix board in the
                     puzzle(i.e. "00302060090030500100180640....").
        """
        self.grids = grids
        self.puzzle = []
        self.blanks = []
        self.initPuzzleArray()
        self.blankValues = {}
        self.currentPathLength = 0
        self.constraintChecks = 0
        self.runningTime = 0
        matrixSudoku = self.convertStringToMatrix(self.grids)
        self.puzzle = matrixSudoku

    def solveSudoku(self):
        """
        Solves the Sudoku board/matrix using Forward Check algorithm, does not
        return anything but will modify the values in the puzzle attribute,
        which will hold the matrix solution.

        This will initialize the sudoku board with empty values then will start
        the pre process of the variables to perform the algorithm then the
        method forward Check is called to iterate until find the solution of the
        sudoku board provided.
        """

        self.blanks = self.getEmptyCells(self.puzzle)
        self.runningTime = time.clock()
        self.processVariablesF()
        self.forwardCheck(0)

    def getSolvedSudoku(self):
        """
        This method returns the matrix of the sudoku solved.
        i.e. [[4,8,3,9,2,1,6,5,7], [9,6,7,3,4,5,8,2,1], [2,5,1,8,7,6,4,9,3]....
        """
        return self.puzzle

    def forwardCheck(self, index):
        """
        Implementation of Forward checking algorithm method, this method
        iterates until complete solution of the sudoku, receives the index where
        it starts and then varies by recursive calls by adding 1 each time.

        This method does not return anything, only will iterate until find a
        solution, will modify the self.puzzle variable which contains the sudoku
        solution.

        Keyword arguments:
        index -- integer value of the index sudoku always starts with 0 and will
                 increment by one by recursive calls to this same method(i.e. 0)
        """
        if index > len(self.blanks) - 1:
            self.endAlgorithm()
        blank = self.blanks[index]
        row = blank[0]
        column = blank[1]

        blankDomain = copy.deepcopy(self.blankValues[blank])
        for numberValue in blankDomain:
            tempDomain = copy.deepcopy(self.blankValues)
            consistent = self.pruneInvalid(blank, numberValue)
            if (consistent == True):
                self.puzzle[row][column] = numberValue
                self.currentPathLength += 1
                result = self.forwardCheck(index + 1)
                if result != None:
                    return
            self.blankValues = tempDomain
        self.puzzle[row][column] = 0
        self.currentPathLength -= 1
        index -= 1

    def pruneInvalid(self, blank, numberValue):
        """
        Removes the number value from the domain for all constraint-neighbors
        of (row, column).

        Keyword arguments:
        blank -- Receives the index values where cell is blank to review i.e.
                 (row, column) - (1, 5).
        numberValue --  the posible number integer value in the cell blank
                        (i.e 8).
        Return:
        True if set of this value in is possible, False otherwise.
        """
        neighbors = self.getNeighborBlanks(blank)
        for neighborBlank in neighbors:
            neighborDomain = self.blankValues[neighborBlank]
            if numberValue in neighborDomain:
                self.blankValues[neighborBlank].remove(numberValue)
                if len(self.blankValues[neighborBlank]) == 0:
                    return False
        return True

    def getNeighborBlanks(self, blank):
        """
        Get the blank neighbors (squares that are affected by a constraint from
        a given blank) of the square (row, col).

        Keyword arguments:
        blank -- blank cell index to be reviewed i.e (4, 5) where 4 is the row
                index and 5 is the column index in the matrix.

        Return:
        This method returns a list of cell indexes of neighbors that have 0
        as its value i.e. ----- ((2, 3), (4, 6), ...).
        """
        row = blank[0]
        col = blank[1]

        neighbors = []
        associatedBlanks = self.getRowBlanks(row) + self.getColumnBlanks(col) \
                            + self.getBoxBlanks(row, col)
        for blank in associatedBlanks:
            if blank not in neighbors and blank!=(row, col):
                neighbors.append(blank)
        return neighbors

    def getBoxBlanks(self, rowToReview, columnToReview):
        """
        Get all neighboring cells in box group that have a 0 as its value.

        Keyword arguments:
        rowToReview -- index of the row in the sudoku.
        columnToReview -- index of the column in the sudoku.

        Return:
        This method returns a list of cells indexes that have 0 as its value
        i.e. ((2, 3), (4, 6), ...).
        """
        cells = []
        rowToReview = (rowToReview / 3) * 3
        columnToReview = (columnToReview / 3) * 3

        for row in range(3):
            for column in range(3):
                if self.puzzle[rowToReview + row][columnToReview + column] == 0:
                    cells.append((rowToReview + row, columnToReview + column))

        return cells

    def getRowBlanks(self, rowToReview):
        """
        Get all neighboring cells in the row group that have a 0 as its value.

        Keyword arguments:
        rowToReview --  Integer value of the row index to review if it contains
                        0 as value (i.e. 8).
        Return:
        This method returns a list of cells indexes where it has 0 as its value
        in the row provided.
        """
        cells = []
        for column in range(9):
            if self.puzzle[rowToReview][column] == 0:
                cells.append((rowToReview, column))
        return cells

    def getColumnBlanks(self, columnToReview):
        """
        Get all neighboring cells in the column group that have a 0 as its
        value.

        Keyword arguments:
        columnToReview -- Integer value of the column index to review (i.e. 8).

        Return:
        This method returns a list of cells indexes where it has 0 as its value
        in the column provided.
        """
        cells = []
        for row in range(9):
            if self.puzzle[row][columnToReview] == 0:
                cells.append((row, columnToReview))

        return cells

    def isPuzzleValid(self, row, column, numberValue, heuristic):
        """
        Check if the current puzzle/sudoku board is legal after placing a
        numberValue in a specified (row, column).

        Keyword arguments:
        row -- Integer value of the row index to review (i.e. 8).
        column -- Integer value of the column index to review (i.e. 5).
        numberValue -- The integer value for the cell to be reviewed if is valid
                        i.e. 5
        heuristic -- boolean value to bypass the constraint check increment when
                     using this method for a heuristic, in which case the
                     heuristic usage shouldn't count toward the constraint
                     checks(i.e. False).
        Return:
        Returns True if based on the review the value being check is valid
        after its usage, False otherwise.
        """
        if heuristic == False:
            self.constraintChecks += 1
        valid = False
        if numberValue == 0:
            return True
        else:
            rowValid = self.checkRow(row, numberValue)
            colValid = self.checkColumn(column, numberValue)
            boxValid = self.checkBox(row, column, numberValue)
            valid = (rowValid & colValid & boxValid)

        return valid

    def checkRow(self, row, numberValue):
        """
        Check if numberValue is a legal value for the given row.

        Keyword arguments:
        row -- Integer value of the row index to review (i.e. 8).
        numberValue -- The integer value for the cell to be reviewed if is valid
                        i.e. 5
        Return:
        Return True if set the number value is doable in the Row specified,
        False otherwise.
        """
        for col in range(9):
            currentValue = self.puzzle[row][col]
            if numberValue == currentValue:
                return False
        return True

    def checkColumn(self, columnToReview, numberValue):
        """
        Check if numberValue is a legal value for the given column.

        Keyword arguments:
        columnToReview -- Integer value of the column index to review (i.e. 8).
        numberValue -- The integer value for the cell to be reviewed if is valid
                        i.e. 5
        Return:
        Return True if set the number value is doable in the column specified,
        False otherwise.
        """
        for row in range(9):
            currentValue = self.puzzle[row][columnToReview]
            if numberValue == currentValue:
                return False
        return True

    def checkBox(self, rowToReview, columnToReview, numberValue):
        """
        Check if numberValue is a legal value for the box (one of 9 boxes)
        containing given rowToReview/columnToReview, returns the boolean value
        based in the review.

        Keyword arguments:
        rowToReview -- Integer value of the row index to review (i.e. 8).
        columnToReview -- Integer value of the column index to review (i.e. 8).
        numberValue -- The integer value for the cell to be reviewed if is valid
                        i.e. 5
        Return:
        Return True if set the number value is doable in the row and column
        specified, False otherwise.
        """
        rowToReview = (rowToReview / 3) * 3
        columnToReview = (columnToReview / 3) * 3

        for r in range(3):
            for c in range(3):
                if self.puzzle[rowToReview + r][columnToReview + c] == numberValue:
                    return False
        return True

    def endAlgorithm(self):
        """
        Method to end the algorithm in the process after complete the sudoku
        solution, also it takes the final time that took to solve the sudoku,
        this one does not return anything.
        """
        self.runningTime = time.clock() - self.runningTime
        sys.exit(0)

    def getEmptyCells(self, puzzle):
        """
        This method returns a list of all the empty cells (positions in the
        sudoku matrix/board).

        Keyword arguments:
        puzzle -- Is the sudoku matrix/board where will look for empty cells
                  (i.e. [[1], [0], [5], [6].....].
        Return:
        A list of positions where the value is 0 ((1,7), (2,4),...)
        """
        emptyCells = []
        for i in range(9):
            for j in range(9):
                if self.puzzle[i][j] == 0:
                    emptyCells.append((i, j))
        return emptyCells

    def processVariablesF(self):
        """
        Preprocessing for forward checking by the Construct of dictionary, this
        method does not return anything but modifies the self.blankValues so the
        cells have all the posible values based on its neighbor cells.
        """
        for blank in self.blanks:
            possibleValues = self.getPossibleValues(blank, False)
            self.blankValues[blank] = possibleValues

    def getPossibleValues(self, cellToReview, heuristic):
        """
        Get all legal values for a cell, receives the heuristic which is a
        boolean value, receives as a parameter also the reference of a cell to
        look for cell values and check if they are valid, based on this returns
        all posible Values for the cell.

        Keyword arguments:
        cellToReview -- This is a list of index position in the row and column
                        to get all posible values for it i.e. (5, 8).
        heuristic -- This is a boolean value of the heuristic applied (True).
        Return:
        A list of all posible values allowed for a specific cell i.e. (1, 5, 8,
        9).
        """
        row = cellToReview[0]
        columnToReview = cellToReview[1]
        allowed = []
        for i in range(1, 10):
            if (self.isPuzzleValid(row, columnToReview, i, heuristic) is True):
                allowed.append(i)
        return allowed

    def initPuzzleArray(self):
        """
        Constructs the blank puzzle/sudoku board to have ceros as values
        [[0, 0, 0, 0, 0, 0 ...], [0, 0, 0, 0, 0, 0 ...],
        [0, 0, 0, 0, 0, 0 ...]...]for all rows and columns.
        """
        del self.puzzle[:]
        for i in range(9):
            self.puzzle.append([])
            for j in range(9):
                self.puzzle[i].append([])
                self.puzzle[i][j] = 0