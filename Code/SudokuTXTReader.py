"""
Author: Alvaro Avila
Date: 07/19/2013
Modified: 07/19/2013
        Notes: Updated Documentation for code.
Revised by: None
"""

class SudokuTXTReader():
    """
    Class Name: SudokuTXTReader
    Description: The SudokuTXTReader class reads the content from a
                TXT file required to form a string line supported by the Sudoku
                Algorithm solvers, also performs different validations to the
                content in order to check if csv content is valid.
    """

    def __init__(self, txtFileName, sizeSudoku):
        """
        Constructs a TXT reader to get the sudoku board into a string line
        supported by the Sudoku Algorithm solvers.

        TXT file content format should be as follow:
                001700600
                090043000
                007000810
                003050900
                002600075
                080000020
                040009002
                605021008
                000800040

        Keyword arguments:
        txtFileName -- Is a string value of the name of TXT file (i.e.
                        "sudokuFile.txt".
        sizeSudoku -- integer value of the expected size of the sudoku(i.e. 9).
        """
        self._txtFileName = txtFileName
        self._sizeSudoku = sizeSudoku
        fileRead = open(self._txtFileName, "r")
        self._content = fileRead.read().strip()

    def readSudokuFromTXTFile(self):
        """
        This method reads the TXT file content, modifies the string got to have
        a string supported by the Sudoku Solvers.

        Return:
        A string value supported by the Sudoku Solvers i.e. "001700600090043..."
        """
        stringFormated = self._content.replace("\n", "")
        return stringFormated

    def setTXTFileName(self, fileName):
        """
        This method sets a new value for the File Name of the corresponding
        SudokuTXTReader object, does not return anything.

        Keyword arguments:
        filename -- Is a string value of the name for the new TXT file  (i.e.
                    "newTXTFile.txt".
        """
        self._txtFileName = fileName

    def isTXTContentValid(self):
        """
        This method returns True if after perform validations of each Row size
        provided, dimension, review if txt content are only digits allowed and
        final Sudoku string size is the expected one, returns False otherwise.
        """
        if(self.isSizeAccurate() and self.areOnlyAllowedNumbers() and
            self.isDimensionAccurate() and self._countRowsSizeEntries()):
            return True
        else:
            return False

    def isSizeAccurate(self):
        """
        This method returns True if whole sudoku string is complaint with
        the size of the sudoku, False otherwise
        """
        if(len(self.readSudokuFromTXTFile()) ==
                                        (self._sizeSudoku * self._sizeSudoku)):
            return True
        else:
            return False

    def isDimensionAccurate(self):
        """
        This method returns True if whole sudoku dimension is complaint with
        the size of the sudoku, False otherwise
        """
        countEnters = self._content.count("\n")
        if(countEnters == (self._sizeSudoku - 1)):
            return True
        else:
            return False

    def _countRowsSizeEntries(self):
        """
        This method returns True if each row in the CSV file is complaint with
        the size of the sudoku, False otherwise
        """
        fileRead = open(self._txtFileName, "r")
        text = fileRead.readlines()
        for line in text:
            line = line.replace("\n", "").strip()
            if (not len(line) == self._sizeSudoku):
                return False
        return True

    def areOnlyAllowedNumbers(self):
        """
        This method returns True if content of the txt are only digits allowed,
        False otherwise. i.e. Digits allowed are 1, 2, 3,...,8,9
        """
        sudokuMatrix = self.readSudokuFromTXTFile()
        validChars = True
        for eachDigit in sudokuMatrix:
            if(not eachDigit.isdigit()):
                return False
        return validChars