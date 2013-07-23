"""
Author: Pilar Villarreal
Date created: 07/09/2013
Description: Run this file to start the game.
             The menu will be displayed to select game options.
Modified:
                Comments:
Revised by:

"""
from ConsoleMenu import ConsoleMenu
import sys

"""
This file instantiate an object of ConsoleMenu receiving following arguments:
Configuration.xml file which contains the settings selected by user.
UserDefaultSettings.xml file which contains the settings by default of the game.
"""

gameMenu = ConsoleMenu('Configuration.xml','UserDefaultSettings.xml')
gameMenu.mainOptionsMenu()
while True:
    gameMenu.mainOptionsMenu()