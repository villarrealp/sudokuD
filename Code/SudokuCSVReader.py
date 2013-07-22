"""
Author: Alvaro Avila
Date created: 07/19/2013
Description: CSV Reader to get sudoku string line.
Modified: 07/19/2013 by Alvaro avila
                Comments: None.
Revised by: -
"""
import csv

class SudokuCSVReader():
    """
    Class Name: SudokuCSVReader
    Description: The SudokuCSVReader class will help to read the content
                required to form a string line supported by the Sudoku Algorithm
                solvers, also performs different validations to the content in
                order to check if csv content is valid.
    """
    rowSeparator = ','

    def __init__(self, txtFileName, sizeSudoku):
        """
        Constructs a CSV reader to get the sudoku board into a string line
        supported by the Sudoku Algorithm solvers.

        Keyword arguments:
        txtFileName -- Is a string value of the name of CSV file (i.e.
                        "newCSVFile.csv".
        sizeSudoku -- integer value of the expected size of the sudoku(i.e. 9).
        """
        self._csvFileName = txtFileName
        self._sizeSudoku = sizeSudoku
        self.lisOfSudokuLines = []
        self.sudokuString = ""
        self.readCSVContent()

    def readCSVContent(self):
        """
        This method open and read the CSV file content, sets all the lines in
        the CSV in a list called self.lisOfSudokuLines, does not return anything.
        """
        with open(self._csvFileName, 'rb') as csvFile:
            content = csv.reader(csvFile, delimiter = self.rowSeparator,
                        quoting = csv.QUOTE_NONE)
            for row in content:
                self.lisOfSudokuLines = row
        for Line in self.lisOfSudokuLines:
            self.sudokuString = self.sudokuString + Line.strip()

    def getSudokuString(self):
        """
        This method returns the sudoku board in a string format.
        i.e. "001700600090043000007000810003050900002600075..."
        """
        return self.sudokuString

    def _countRowsSizeEntries(self):
        """
        This method returns True if each row in the CSV file is complaint with
        the size of the sudoku, False otherwise
        """
        for eachRow in self.lisOfSudokuLines:
            if (len(eachRow.strip()) != self._sizeSudoku):
                return False
        return True

    def isSizeAccurate(self):
        """
        This method returns True if whole sudoku string is complaint with
        the size of the sudoku, False otherwise
        """
        if(len(self.sudokuString) == (self._sizeSudoku * self._sizeSudoku)):
            return True
        else:
            return False

    def setFileName(self, filename):
        """
        This method sets a new value for the File Name of the corresponding
        SudokuCSVReader object, does not return anything.

        Keyword arguments:
        filename -- Is a string value of the name for the new CSV file  (i.e.
                    "newCSVFile.csv".
        """
        self._csvFileName = filename

    def isDimensionAccurate(self):
        """
        This method returns True if whole sudoku dimension is complaint with
        the size of the sudoku, False otherwise
        """
        if(len(self.lisOfSudokuLines) == (self._sizeSudoku)):
            return True
        else:
            return False

    def isCSVContentValid(self):
        """
        This method returns True if after perform validations of each Row size
        provided, dimension, review if csv content are only digits allowed and
        final Sudoku string size is the expected one, returns False otherwise.
        """
        if(self._countRowsSizeEntries() and self.areOnlyAllowedNumbers() and
            self.isDimensionAccurate() and self.isSizeAccurate()):
            return True
        else:
            return False

    def areOnlyAllowedNumbers(self):
        """
        This method returns True if content of the CSV are only digits allowed,
        False otherwise.
        """
        for eachDigit in self.sudokuString:
            if(not eachDigit.isdigit()):
                return False
        return True