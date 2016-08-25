#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import unittest
from lib import runner,utils
from lib.launcher import *
from lib.dde_dock import *

result = True

class LauncherRemoveFromDock(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.caseid = '33837'
        cls.casename = 'all-517:从任务栏移除'
        cls.menuObj = root.application(appName='deepin-menu', description='/usr/lib/deepin-menu')
        cls.googleName = 'Google Chrome'

    @classmethod
    def tearDownClass(cls):
        global result
        utils.commitresult(cls.caseid, result)
        launcher.exitLauncher()

    def testMenuUnDock(self):
    	launcher.menuUnDock(self.googleName)
    	dockApps = Dock().getAllDockApps()
    	self.assertNotIn('google-chrome',dockApps)

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