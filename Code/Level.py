
"""
Class Name: Level
Description: The Level class will hold the Sudoku Level that will be used by the
             Settings class.
"""
class Level:

    def __init__(self, bottonLimit, topLimit, nameLevel):
        self.topLimit = topLimit
        self.bottonLimit = bottonLimit
        self.nameLevel = nameLevel

    def getTopLimit(self):
        return self.topLimit

    def getBottomLimit(self):
        return self.bottonLimit

    def getNameLevel(self):
        return self.nameLevel

    def setTopLimit(self, newTopLimit):
        self.topLimit = newTopLimit

    def setBottomLimit(self, newBottomLimit):
        self.bottonLimit = newBottomLimit

    def setNameLevel(self, newNameLevel):
        self.nameLevel = newNameLevel

    def setNameLevel(self, newNameLevel):
        self.nameLevel = newNameLevel

    def __eq__(self, anotherLevel):
        if(self.topLimit == anotherLevel.getTopLimit() and
                self.bottonLimit == anotherLevel.getBottomLimit() and
                self.nameLevel == anotherLevel.getNameLevel()):
            return True
        else:
            return False

