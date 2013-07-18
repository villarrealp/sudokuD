"""
Author: Debbie Rios
Date: 07/04/2013
Modified:   07/17/2013   by: Debbie Rios
Comments: Changes following standard, and comments from Edson Gonzales
Revised by:

"""
import time, random
from Algorithm import Algorithm

"""
Class Name: PeterNorvigAlgorithm
Description: resolve sudoku puzzle, using constraint propagation
and search methods.
Throughout this program we have:
   square, e.g. 'A3'
   digit,  e.g. '9'
   u is a unit,   e.g. ['A1','B1','C1','D1','E1','F1','G1','H1','I1']
   grid is a grid,e.g. 81 non-blank chars, e.g. starting with '.18...7...
   values is a dict of possible values, e.g. {'A1':'12349', 'A2':'8', ...}
"""

class PeterNorvigAlgorithm(Algorithm):
    def cross(self, Rows, Cols):
        """
        This method return the cross product of elements in
        A and elements in B.

        Keyword arguments:
        Rows -- elements of a row e.g. 'A'
        Cols -- elements of a cols e.g. '2'
        """
        return [row + col for row in Rows for col in Cols]

    def __init__(self, grids, sep='\n'):
        """ Constructor of the class

        Keyword arguments:
        grids -- the string data of the sudoku without resoved.e.g "00302060...."
        sep -- each file of 9 should be sep for '\n'
        """
        self.digits   = '123456789' # Valid digits of sudoku grid will contain.
        self.rows     = 'ABCDEFGHI' # Each row of the sudoku grid will contain.
        self.cols     = self.digits # Each col of sudoku grid will contain.

        # Each square of sudoku grid, 9 squares per sudoku e.g 'A3'
        self.squares  = self.cross(self.rows, self.cols)

        # List of units in  the sudoku
        self.unitlist = ([self.cross(self.rows, col) for col in self.cols] +
                    [self.cross(row, self.cols) for row in self.rows] +
                    [self.cross(rs, cs) for rs in ('ABC', 'DEF', 'GHI')\
                     for cs in ('123', '456', '789')])

        # Each unit of sudoku into a dictionary e.g ['A1','B1',...,'I1']
        self.units = dict((square, [unit for unit in self.unitlist if square in unit])\
                        for square in self.squares)

        # Each square has 20 peers
        self.peers = dict((square, set(sum(self.units[square], []))\
                            -set([square])) for square in self.squares)

        # Constructor of the class algorithm
        Algorithm.__init__(self, grids.strip().split(sep))

    def parseGrid(self, grid):
        """
        This method convert a grid to a dict of possible values,
        and return:{square: digits}, or return False if a contradiction is detected.

        Keyword arguments:
        grid -- the grid of the sudoku  to resolve. e.g "00302060...."
        """
        # To start, every square can be any digit; then assign values from the grid.
        values = dict((square, self.digits) for square in self.squares)
        for square, digit in self.getGridValues(grid).items():
            if digit in self.digits and not self.assign(values, square, digit):
                return False # (Fail if we can't assign digit to square square.)
        return values

    def getGridValues(self, grid):
        """
        This method convert a grid into a dict and return:{square: char}
        with '0' or '.' for empties.

        Keyword arguments:
        grid -- the grid of the sudoku  to resolve. e.g "00302060...."
        """
        chars = [c for c in grid if c in self.digits or c in '0.']
        assert len(chars) == 81
        return dict(zip(self.squares, chars))

    def assign(self, values, square, digit):
        """
        Constraint Propagation method:
        Eliminate all the other values (except digit) from values[square]
        and propagate.
        Return values, except return False if a contradiction is detected.

        Keyword arguments:
        value -- dict of possible values to resolve the sudoku
        e.g. {'A1':'12349', 'A2':'8', ...}
        square -- each unit of the matriz of the sudoku e.g. I9
        digit -- each possible digit to resolve the sudoku e.g '8'
        """
        other_values = values[square].replace(digit, '')
        if all(self.eliminate(values, square, nextDigit)\
                             for nextDigit in other_values):
            return values
        else:
            return False

    def eliminate(self, values, square, digit):
        """
        This method eliminate digit from values[square]; propagate when
        values or places <= 2.
        Return values, except return False if a contradiction is detected.

        Keyword arguments:
        values -- dict of possible values to resolve the sudoku
        e.g. {'A1':'12349', 'A2':'8', ...}
        square -- each element of the matriz of the sudoku e.g 'H1'
        digit -- each possible digit to resolve the sudoku. e.g '5'
        """
        if digit not in values[square]:
            return values
        values[square] = values[square].replace(digit, '')
        if (self.reviewNextDigit(values, square) != True):
            return False
        return self.reviewUnit(values, square, digit)

    def reviewNextDigit(self, values, square):
        """
        This method eliminate nextDigit from the peers if a square s is reduced
        to one value nextDigit.
        Return True, except return False if a contradiction is detected.

        Keyword arguments:
        values -- dict of possible values to resolve the sudoku,
        e.g. {'A1':'12349', 'A2':'8', ...}
        square -- each element of the matriz of the sudoku e.g 'H1'
        """
        if len(values[square]) == 0:
            return False                     # Contradiction: removed last value
        elif len(values[square]) == 1:
            nextDigit = values[square]
            if not all(self.eliminate(values, nextSquare, nextDigit)\
                         for nextSquare in self.peers[square]):
                return False
        return True

    def reviewUnit(self, values, square, digit):
        """
        This method puts a value digit if a unit 'unit' is reduced to only
        one place for a value digit.
        Return values, except return False if a contradiction is detected.

        Keyword arguments:
        values -- dict of possible values to resolve the sudoku,
        e.g. {'A1':'12349', 'A2':'8', ...}
        square -- each element of the matriz of the sudoku, e.g 'H1'
        digit -- each possible digit to resolve the sudoku, e.g. '9'
        """
        for unit in self.units[square]:
            dplaces = [square for square in unit if digit in values[square]]
            if len(dplaces) == 0:
                return False            # Contradiction: no place for this value
            elif len(dplaces) == 1:
                # digit can only be in one place in unit; assign it there
                if not self.assign(values, dplaces[0], digit):
                    return False
        return values


    def search(self, values):
        """
        This method use depth-first search and propagation, recursively
        try all possible values, return the sudoku solved to solve method.

        Keyword arguments:
        values -- dict of possible values to resolve the sudoku,
        e.g. {'A1':'12349', 'A2':'8', ...}
        """
        if values is False:
            return False                                        # Failed earlier
        if all(len(values[square]) == 1 for square in self.squares):
            return values                                              # Solved!
        # Chose the unfilled square square with the fewest possibilities
        n, square = min((len(values[square]), square) for square in self.squares \
                                        if len(values[square]) > 1)
        return self.validValues(self.search(self.assign(values.copy(), \
                        square, digit)) for digit in values[square])

    def validValues(self, seq):
        """This method return the valid values of seq that is true.

        Keyword arguments:
        seq -- the sequence of values to verify for a true value e.g '1234...'
        """
        for e in seq:
            if e:
                return e
        return False

    def shuffled(seq):
        """
        This method return a randomly shuffled copy of the input sequence.

        Keyword arguments:
        seq -- the sequence of values to verify for a true value e.g '1234...'
        """
        seq = list(seq)
        random.shuffle(seq)
        return seq

    def getMatrix(self, values):
        """ This method return the sudoku resolve into a matrix.

        Keyword arguments:
        values -- dict of possible values to resolve the sudoku,
        e.g. {'A1':'12349', 'A2':'8', ...}
        """
        dictList = []
        matrix = sorted(dict.items(values))
        for key, value in matrix:
            temp = [key, value]
            dictList.append(value)
        self.solution = self.convertStringToMatrix(dictList)

    def solve(self, grid):
        """Search method, call to search and parseGrid methods,
        and return the grid resolved.

        Keyword arguments:
        grid -- the grid of the sudoku  to resolve. e.g "00302060...."
        """
        return self.search(self.parseGrid(grid))

    def solveSudoku(self ):
        """
        Attempt to solve a sequence of grids. Report results.
        """
        def time_solve(grid):
            """
            This method displays the time that its take to solve any sudoku.

            Keyword arguments:
            grid -- the grid of the sudoku  to resolve. e.g "00302060...."
            """
            start = time.clock()
            values = self.solve(grid)
            self.runningTime = time.clock() - start
            self.getMatrix(values)
            return (self.runningTime, self.solved(values))
        times, results = zip( * [time_solve(grid) for grid in self.grids])

    def display(self, values):
        """
        This method display these values as a 2-D grid, return in console the
        sudoku resolved.

        Keyword arguments:
        values -- dict of possible values to resolve the sudoku,
        e.g. {'A1':'12349', 'A2':'8', ...}
        """

        width = 1 + max(len(values[square]) for square in self.squares)
        line = '+'.join(['-' * (width * 3)] * 3)
        for row in self.rows:
            print ''.join(values[row + col].center(width) + ('|' if col in '36' else '')
                          for col in self.cols)
            if row in 'CF': print line

