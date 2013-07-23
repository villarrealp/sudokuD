import sys
sys.path.append('../')
from coverage import coverage

cov = coverage()
cov.start()

import unittest

from TestSudokuTXTReader import TestSudokuTXTReader
from TestForwardCheck import TestForwardCheck
from TestSettings import TestSettings
from TestConfigurationXML import TestConfigurationXML
from TestPeterNorvigAlgorithm import TestPeterNorvigAlgorithm
from TestBacktrackingAlgorithm import TestBacktrackingAlgorithm
from TestConsoleMenu import TestConsoleMenu
from TestLevel import TestLevel
from TestSudokuCSVReader import TestSudokuCSVReader

if __name__ == '__main__':

    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestConfigurationXML))
    suite.addTest(unittest.makeSuite(TestSettings))
    suite.addTest(unittest.makeSuite(TestSudokuTXTReader))
    suite.addTest(unittest.makeSuite(TestForwardCheck))
    suite.addTest(unittest.makeSuite(TestPeterNorvigAlgorithm))
    suite.addTest(unittest.makeSuite(TestBacktrackingAlgorithm))
    suite.addTest(unittest.makeSuite(TestConsoleMenu))
    suite.addTest(unittest.makeSuite(TestLevel))
    suite.addTest(unittest.makeSuite(TestSudokuCSVReader))

    unittest.TextTestRunner(verbosity=2).run(suite)
    cov.stop()
    cov.save()
    cov.html_report()