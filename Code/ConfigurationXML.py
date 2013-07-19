"""
Author: Debbie Rios
Date: 07/04/2013
Modified:   ..........    by:
                Comments: None.
Revised by:               by:

"""
import xml.etree.ElementTree as et
import xml.etree.cElementTree as ET
from Level import Level

"""
Class Name:Class ConfigurationXML
Description:parse an xml file for reading and writing.
"""
class ConfigurationXML:
    def __init__(self, filename):
        """ Constructor of the class.

        Keyword arguments:
        filename -- the xml file with the grid of the sudoku to be solved e.g.
        'Configure.xml'
        """
        self.filename = filename
        self.xmlfile = et.parse(filename)

    def getNodes(self, path):
        """ This method read an xml file by elements.

        Keyword arguments:
        path -- a string that contains each element of the xml file e.g.
        './Settings/GameOption/'

        Return:
        A list with all the options set in the xml file by nodes
        e.g. ['Solve', 'Generate']
        """
        elem = self.xmlfile.findall(path)
        Options = []
        for e in elem:
            Options.append(e.attrib["name"])
        return Options

    def getSudokuGameOptions(self):
        """
        This method return into a list the game options set
        in the xml file.
        """
        return self.getNodes('./Settings/GameOption/')

    def getSudokuDifficultyLevels(self):
        """
        This method return into a list the game difficult level also de botton
        and top levef of difficulty set in the xml file.
        """
        elemforDifficult = self.xmlfile.findall('./Settings/DifficultyLevel/')

        listDificultyLevels = []
        for e in elemforDifficult:
            newLevel = Level(int(e.attrib["bottonLimits"]), int(e.attrib["topLimits"]), e.attrib["name"])
            listDificultyLevels.append(newLevel)
        return listDificultyLevels

    def getSudokuAlgorithmOptions(self):
        """
        This method return into a list of string the algorithm
        options set in xml file.
        """
        return self.getNodes('./Settings/AlgorithmOption/')

    def getSudokuOutputFormat(self):
        """
        This method return into a list of strings the output
        format set in xml file.
        """
        return self.getNodes('./Settings/OutputFormat/')

    def WriteXML(self, node, value):
        """ This method write an xml file by elements.

        Keyword arguments:
        node -- a string that contains each element on the xml file e.g. 'OutputFormat'
        value -- a string that contains the item name inside of ech node
        e.g. 'name'.
        """
        root = self.xmlfile.find(node)
        items = list(root.iter('item'))
        for item in items:
            item.attrib['name'] = value
        self.xmlfile.write(self.filename)

    def writeSudokuGameOptions(self, optionGameOptionSelected):
        """ This method write the option selected by the user.

        Keyword arguments:
        optionGameOptionSelected -- a string that contains the option selected
        to write in the xml file e.g. 'Solve'
        """
        self.WriteXML('./UserSettings/GameOption/', optionGameOptionSelected)

    def writeSudokuDifficultyLevels(self, optionGameOptionSelected):
        """
        This method write dificuly level of the game selected
        by the user.

        Keyword arguments:
        optionGameOptionSelected -- a string that contains the option selected
        to write in the xml file e.g. 'Easy'
        """
        self.WriteXMLDificultyLevel('./UserSettings/DifficultyLevel/',\
                      optionGameOptionSelected)

    def saveXMLDificultyLevel(self, node, newLevel):
        """ This method write an xml file by elements.

        Keyword arguments:
        node -- string that contains
        newLevel -- integer with the level of difficulty of the gamee e.g. 25
        """
        root = self.xmlfile.find(node)
        items = list(root.iter('item'))
        for item in items:
            item.attrib['name'] = newLevel.getNameLevel()
            item.attrib['bottonLimits'] = str(newLevel.getBottomLimit())
            item.attrib['topLimits'] = str(newLevel.getTopLimit())
        self.xmlfile.write(self.filename)

    def writeSudokuAlgorithmOptions(self, optionGameOptionSelected):
        """ This method write algorithm option selected by the user.

        Keyword arguments:
        optionGameOptionSelected -- a string that contains the option selected
        to write in the xml file e.g. 'Peter Norvig'
        """
        self.WriteXML('./UserSettings/AlgorithmOption/',\
                     optionGameOptionSelected)

    def writeSudokuOutputFormat(self, optionGameOptionSelected):
        """ This method write the output format selected by the user.

        Keyword arguments:
        optionGameOptionSelected -- a string that contains the option selected
        to write in the xml file e.g. 'File'
        """
        self.WriteXML('./UserSettings/OutputFormat/', optionGameOptionSelected)

    def writeSudokuFilePath(self, optionGameOptionSelected):
        """
        This method write the path file selected by the user
        where the game will save.

        Keyword arguments:
        optionGameOptionSelected -- a string that contains the option selected
        to write in the xml file e.g. '..\Sudoku\'
        """
        self.WriteXML('./UserSettings/FilePath/', optionGameOptionSelected)

    def writeSudokuFileName(self, newFileName):
        """
        This method writes the name file selected by the user
        where the game will saved.

        Keyword arguments:
        optionGameOptionSelected -- a string that contains the option selected
        to write in the xml file e.g. 'SudokuFile.txt'
        """
        self.WriteXML('./UserSettings/FileName/', newFileName)

    def writeSudokuMatrixDimension(self, optionGameOptionSelected):
        """ This method write the matrix dimension of the game.

        Keyword arguments:
        optionGameOptionSelected -- an integer with the dimention of the matrix.
        """
        self.WriteXML('./UserSettings/MatrixDimension/', \
                        str(optionGameOptionSelected))

    def getUserSudokuGameOption(self):
        """
        This method update the xml file with the option selected
        by the user.
        """
        return self.getNodes('./UserSettings/GameOption/')[0]

    def getUserDifficultyLevel(self):
        """
        This method update the xml file with the option selected
        by the user.
        """
        elemforDifficult = self.xmlfile.findall('./UserSettings/DifficultyLevel/')
        userLevel = Level(int(elemforDifficult[0].attrib["bottonLimits"]),
                        int(elemforDifficult[0].attrib["topLimits"]),
                        elemforDifficult[0].attrib["name"])
        return userLevel

    def getUserAlgorithmOption(self):
        """
        This method update the xml file with the option selected
        by the user.
        """
        return self.getNodes('./UserSettings/AlgorithmOption/')[0]

    def getUserOutputFormat(self):
        """
        This method update the xml file with the option selected
        by the user.
        """
        return self.getNodes('./UserSettings/OutputFormat/')[0]

    def getUserFilePath(self):
        """
        This method return the file path where the file will saved.
        """
        return self.getNodes('./UserSettings/FilePath/')[0]

    def getUserFileName(self):
        """
        This method returns a string with the filename set in xml file where the
        sudoku will be generated or solved.
        """
        return self.getNodes('./UserSettings/FileName/')[0]

    def getUserMatrixDimension(self):
        """
        This method gets the matrix dimension of the sudoku this will not be
        displayed to user but is for internal validation.
        """
        return int(self.getNodes('./UserSettings/MatrixDimension/')[0])


