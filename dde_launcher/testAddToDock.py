#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import unittest
from lib import executeTestCase
import time
from lib import runner,utils
from lib.launcher import *
from lib.dde_dock import *

result = True
casename = 'all-518:添加到任务栏'

class LauncherAddToDock(unittest.TestCase):
    caseid = '33840'
    @classmethod
    def setUpClass(cls):
        cls.menuObj = root.application(appName='deepin-menu', description='/usr/lib/deepin-menu')
        cls.googleName = 'Google Chrome'
        cls.dockname = 'google-chrome'
        dockApps = Dock().getAllDockApps()
        if cls.dockname in dockApps:
            appCoor = Dock().getAppCoor(cls.googleName)
            screen = pyautogui.size()
            screen_center = (screen[0]/2,screen[1]/2)
            pyautogui.mouseDown(appCoor)
            pyautogui.dragTo(screen_center, duration=2)
        launcher.freeMode()

    @classmethod
    def tearDownClass(cls):
        launcher.exitLauncher()

    def testMenuDock(self):
    	launcher.menuDock(self.googleName)
    	dockApps = Dock().getAllDockApps()
    	self.assertIn(self.dockname,dockApps)


    def suite():
        suite = unittest.TestSuite()
        suite.addTest(LauncherAddToDock('testMenuDock'))
        return suite


if __name__ == "__main__":
    executeTestCase.runTest(LauncherAddToDock)
