"""
Author: Alvaro Avila
Date: 07/17/2013
Modified:   07/17/2013    by: Alvaro Avila
                Comments: None.
Revised by: 07/17/2013    by: Alvaro Avila
"""

class Level:
    """
    Class Name: Level
    Description: The Level class will hold the values of a Sudoku that will be used
             by the Settings class.
    """

    def __init__(self, bottonLimit, topLimit, nameLevel):
        """
        Constructs a new Level according to the given bottom, top limits and the
        name value for the corresponding Level.

        Keyword arguments:
        bottonLimit -- This an integer value of how many cells values should be
                    displayed as minimum for this level(i.e. 36).
        topLimit -- This an integer value of how many cells values should be
                    displayed as much for this level(i.e. 50).
        nameLevel -- This is a string type value of the Name of the Sudoku Level
                     i.e. "Hard".
        """
        self.topLimit = topLimit
        self.bottonLimit = bottonLimit
        self.nameLevel = nameLevel

    def getTopLimit(self):
        """
        Returns the integer value of how many cells values should be displayed
        as much for this level.
        """
        return self.topLimit

    def getBottomLimit(self):
        """
        Returns the integer value of how many cells values should be displayed
        as minimum for this level
        """
        return self.bottonLimit

    def getNameLevel(self):
        """
        Returns the string name value of this level.
        """
        return self.nameLevel

    def setTopLimit(self, newTopLimit):
        """
        This method modifies the current top limit value for a new one.

        Keyword arguments:
        newTopLimit -- This is a new integer value of how many cells values
                    should be displayed as maximum for this level(i.e. 50).
        """
        self.topLimit = newTopLimit

    def setBottomLimit(self, newBottomLimit):
        """
        This method modifies the current bottom limit value for a new one of the
        corresponding Level.

        Keyword arguments:
        newBottomLimit -- This is a new integer value of how many cells values
                    should be displayed as minimum for this level(i.e. 26).
        """
        self.bottonLimit = newBottomLimit

    def setNameLevel(self, newNameLevel):
        """
        This method modifies the current name of the corresponding Level by a
        new one provided.

        Keyword arguments:
        newNameLevel -- This is a new string value that will replace the current
                        Name of the corresponding Level(i.e. "Really Hard").
        """
        self.nameLevel = newNameLevel

    def __eq__(self, anotherLevel):
        """
        This is an overload method that will compare two Level objects, based on
        its attribute values, if all of them contain the same values then will
        return True, False otherwise.

        Keyword arguments:
        anotherLevel -- This is a Level object which the current level will
                        compare against (i.e. Cell( 26, 40, "Hard")).
        """
        if(self.topLimit == anotherLevel.getTopLimit() and
                self.bottonLimit == anotherLevel.getBottomLimit() and
                self.nameLevel == anotherLevel.getNameLevel()):
            return True
        else:
            return False

