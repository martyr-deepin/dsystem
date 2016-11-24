#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import unittest
import time
from lib import runner,utils
from lib.launcher import *
from lib.dde_dock import *

result = True
caseid = '33837'
casename = 'all-517:从任务栏移除'

class LauncherRemoveFromDock(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.startTime = time.time()
        cls.menuObj = root.application(appName='deepin-menu', description='/usr/lib/deepin-menu')
        cls.googleName = 'Google Chrome'
        cls.dockname = 'google-chrome'
        dockApps = Dock().getAllDockApps()
        if cls.dockname not in dockApps:
            launcher.menuDock(cls.googleName)


    @classmethod
    def tearDownClass(cls):
        seconds = "%.3f" % (time.time() - cls.startTime)
        minutes = utils.convertToMinutes(float(seconds))
        global result
        utils.commitresult(caseid, result, minutes)
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

    class MyTestResult(runner.MyTextTestResult):
        def addError(self, test, err):
            super(LauncherRemoveFromDock.MyTestResult, self).addError(test, err)
            global result
            result = result and False

        def addFailure(self, test, err):
            super(LauncherRemoveFromDock.MyTestResult, self).addFailure(test, err)
            global result
            result = result and False

if __name__ == "__main__":
    unittest.TextTestRunner(resultclass=LauncherRemoveFromDock.MyTestResult).run(LauncherRemoveFromDock.suite())
