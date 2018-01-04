#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import time
import gettext
import unittest
import pyautogui
from lib import runTest
from lib import Launcher
from lib import Dock
from lib import utils

result = True
casename = 'all-5345:发送应用到任务栏'

class Launcher_AddToDock(unittest.TestCase):
    caseid = '191631'
    @classmethod
    def setUpClass(cls):
        cls.dock = Dock()
        cls.launcher = Launcher()
        cls.dockname = 'google-chrome'
        cls.dockApps = cls.dock.getAllDockApps()

    @classmethod
    def tearDownClass(cls):
        cls.launcher.exitLauncher()

    def testMenuDock(self):
        if self.dockname in self.dockApps:
            appCoor = self.dock.getAppCoor(self.dock.string_Google_Chrome)
            screen = pyautogui.size()
            screen_center = (screen[0]/2,screen[1]/2)
            #pyautogui.mouseDown(appCoor)
            #pyautogui.dragTo(screen_center, duration=2)
            utils.mouseDrag(appCoor, (appCoor[0], appCoor[1] - 100))
            time.sleep(2)

        dockApps = self.dock.getAllDockApps()
        self.assertNotIn(self.dockname, dockApps)
        self.launcher.menuDock(self.dock.string_Google_Chrome)
        dockApps = self.dock.getAllDockApps()
        self.assertIn(self.dockname, dockApps)


    def suite():
        suite = unittest.TestSuite()
        suite.addTest(Launcher_AddToDock('testMenuDock'))
        return suite


if __name__ == "__main__":
    unittest.installHandler()
    LOCALE_DIR = os.path.abspath("./lib/locale")
    gettext.install('dsystem', LOCALE_DIR)
    runTest(Launcher_AddToDock)
