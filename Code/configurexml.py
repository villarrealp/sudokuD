"""
Author: Debbie Rios
Date: 07/04/2013
Modified:   ..........    by: 
                Comments: None.
Revised by:               by: 

"""
import xml.etree.ElementTree as et
import xml.etree.cElementTree as ET

"""
Class Name:Class ConfigurationXML
Description:parse an xml file for reading and writing.
"""
class ConfigurationXML:
    def __init__(self, filename):
        """ Constructor of the class. """
        self.filename = filename        
        self.xmlfile = et.parse(filename)
                   
    def getNodes(self, path):
        """ This method read an xml file by elements. """
        elem = self.xmlfile.findall(path)
        Options = []
        for e in elem:
            Options.append(e.attrib["name"])
        return Options
    
    def getSudokuGameOptions(self):
        """ This method return into a list the game options set
        in the xml file. """
        return self.getNodes('./Settings/GameOption/')

    def getSudokuDifficultyLevels(self):
        """ This method return into a list the dificuly levels set
        in xml file. """
        return self.getNodes('./Settings/DifficultyLevel/')

    def getSudokuAlgorithmOptions(self):
        """ 
        This method return into a list the algorithm options set
        in xml file. 
        """
        return self.getNodes('./Settings/AlgorithmOption/')

    def getSudokuOutputFormat(self):
        """ This method return into a list the output format set
        in xml file. """
        return self.getNodes('./Settings/OutputFormat/')
    
    def getSudokuFilePath(self):
        """ This method return into a list the file path where the
        game will save, set in xml file. """
        return self.getNodes('./Settings/FilePath/')
        
    def getSudokuMatrixDimension(self):
        """ This method return into a list the dimensions of the matrix
        set in xml file. """
        return self.getNodes('./Settings/MatrixDimension/')

    def WriteXML(self, node, value):
        """ This method write an xml file by elements. """
        root = self.xmlfile.find(node)
        items = list(root.iter('item'))
        for item in items:
            item.attrib['name'] = value
        self.xmlfile.write(self.filename)
        
    def writeSudokuGameOptions(self, optionGameOptionSelected):
        """ This method write the option selected by the user. """
        self.WriteXML('./UserSettings/GameOption/', optionGameOptionSelected)
    
    def writeSudokuDifficultyLevels(self, optionGameOptionSelected):
        """ This method write dificuly level of the game selected
        by the user. """
        self.WriteXML('./UserSettings/DifficultyLevel/',\
                      optionGameOptionSelected)

    def writeSudokuAlgorithmOptions(self, optionGameOptionSelected):
        """ This method write algorithm option selected by the user. """
        self.WriteXML('./UserSettings/AlgorithmOption/',\
                     optionGameOptionSelected)

    def writeSudokuOutputFormat(self, optionGameOptionSelected):
        """ This method write the output format selected by the user. """
        self.WriteXML('./UserSettings/OutputFormat/', optionGameOptionSelected)

    def writeSudokuOutputPathFile(self, optionGameOptionSelected):
        """ This method write the path file selected by the user
        where the game will save. """
        self.WriteXML('./UserSettings/FilePath/', optionGameOptionSelected)

    def writeSudokuMatrixDimension(self, optionGameOptionSelected):
        """ This method write the matrix dimension of the game. """
        self.WriteXML('./UserSettings/MatrixDimension/', \
                        str(optionGameOptionSelected))

    def getUserSudokuGameOption(self):
        """ This method update the xml file with the option selected
        by the user. """
        return self.getNodes('./UserSettings/GameOption/')[0]

    def getUserDifficultyLevel(self):
        """ This method update the xml file with the option selected
        by the user. """
        return self.getNodes('./UserSettings/DifficultyLevel/')[0]

    def getUserAlgorithmOption(self):
        """ This method update the xml file with the option selected
        by the user. """
        return self.getNodes('./UserSettings/AlgorithmOption/')[0]

    def getUserOutputFormat(self):
        """ This method update the xml file with the option selected
        by the user. """
        return self.getNodes('./UserSettings/OutputFormat/')[0]

    def getUserFilePath(self):
        """ This method update the xml file with the option selected
        by the user. """
        return self.getNodes('./UserSettings/FilePath/')[0]

    def getUserMatrixDimension(self):
        """ This method update the xml file with the option selected
        by the user. """
        return int(self.getNodes('./UserSettings/MatrixDimension/')[0])


