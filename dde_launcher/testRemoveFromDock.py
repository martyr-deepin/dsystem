#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import unittest
from lib import executeTestCase
import time
from lib import runner,utils
from lib.launcher import *
from lib.dde_dock import *

result = True
casename = 'all-517:从任务栏移除'

class LauncherRemoveFromDock(unittest.TestCase):
    caseid = '33837'
    @classmethod
    def setUpClass(cls):
        cls.menuObj = root.application(appName='deepin-menu', description='/usr/lib/deepin-menu')
        cls.googleName = 'Google Chrome'
        cls.dockname = 'google-chrome'
        dockApps = Dock().getAllDockApps()
        if cls.dockname not in dockApps:
            launcher.menuDock(cls.googleName)


    @classmethod
    def tearDownClass(cls):
        dockApps = Dock().getAllDockApps()
        if cls.dockname not in dockApps:
            launcher.menuDock(cls.googleName)
        launcher.exitLauncher()

    def testMenuUnDock(self):
    	launcher.menuUnDock(self.googleName)
    	dockApps = Dock().getAllDockApps()
    	self.assertNotIn(self.dockname,dockApps)

    def suite():
        suite = unittest.TestSuite()
        suite.addTest(LauncherRemoveFromDock('testMenuUnDock'))
        return suite


if __name__ == "__main__":
    executeTestCase.runTest(LauncherRemoveFromDock)
