#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import unittest
from lib import runner,utils
from lib.launcher import *
from lib.dde_dock import *

result = True
caseid = '33837'
casename = 'all-517:从任务栏移除'

class MyTestResult(runner.MyTextTestResult):
    def addError(self, test, err):
        super(MyTestResult, self).addError(test, err)
        global result
        result = result and False

    def addFailure(self, test, err):
        super(MyTestResult, self).addFailure(test, err)
        global result
        result = result and False

class LauncherRemoveFromDock(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.menuObj = root.application(appName='deepin-menu', description='/usr/lib/deepin-menu')
        cls.terminalName = 'Google Chrome'

    @classmethod
    def tearDownClass(cls):
        global result
        utils.commitresult(caseid, result)
        launcher.exitLauncher()

    def testMenuUnDock(self):
    	launcher.menuUnDock(self.terminalName)
    	dockApps = Dock().getAllDockApps()
    	self.assertNotIn(self.terminalName,dockApps)

def suite():
    suite = unittest.TestSuite()
    suite.addTest(LauncherRemoveFromDock('testMenuUnDock'))
    return suite

if __name__ == "__main__":
    unittest.TextTestRunner(resultclass=MyTestResult).run(suite())