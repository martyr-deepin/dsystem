#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import unittest
from lib import runner,utils
from lib.launcher import *
from lib.dde_dock import *

result = True

class LauncherAddToDock(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.menuObj = root.application(appName='deepin-menu', description='/usr/lib/deepin-menu')
        cls.caseid = '33840'
        cls.casename = 'all-518:添加到任务栏'
        cls.googleName = 'Google Chrome'

    @classmethod
    def tearDownClass(cls):
        global result
        utils.commitresult(cls.caseid, result)
        launcher.exitLauncher()

    def testMenuDock(self):
    	launcher.menuDock(self.googleName)
    	dockApps = Dock().getAllDockApps()
    	self.assertIn('google-chrome',dockApps)


    def suite():
        suite = unittest.TestSuite()
        suite.addTest(LauncherAddToDock('testMenuDock'))
        return suite

    class MyTestResult(runner.MyTextTestResult):
        def addError(self, test, err):
            super(LauncherAddToDock.MyTestResult, self).addError(test, err)
            global result
            result = result and False

        def addFailure(self, test, err):
            super(LauncherAddToDock.MyTestResult, self).addFailure(test, err)
            global result
            result = result and False

if __name__ == "__main__":
    unittest.TextTestRunner(resultclass=LauncherAddToDock.MyTestResult).run(LauncherAddToDock.suite())