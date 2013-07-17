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

gameMenu = ConsoleMenu('Configuration.xml','UserDefaultSettings.xml')
gameMenu.mainOptionsMenu()