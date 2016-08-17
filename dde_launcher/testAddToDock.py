#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import unittest
from lib import runner,utils
from lib.launcher import *
from lib.dde_dock import *

result = True
caseid = '33840'
casename = 'all-518:添加到任务栏'

class MyTestResult(runner.MyTextTestResult):
    def addError(self, test, err):
        super(MyTestResult, self).addError(test, err)
        global result
        result = result and False

    def addFailure(self, test, err):
        super(MyTestResult, self).addFailure(test, err)
        global result
        result = result and False

class LauncherAddToDock(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.menuObj = root.application(appName='deepin-menu', description='/usr/lib/deepin-menu')
        cls.terminalName = 'Google Chrome'

    @classmethod
    def tearDownClass(cls):
        global result
        utils.commitresult(caseid, result)
        launcher.exitLauncher()

    def testMenuDock(self):
    	launcher.menuDock(self.terminalName)
    	dockApps = Dock().getAllDockApps()
    	self.assertIn(self.terminalName,dockApps)


def suite():
    suite = unittest.TestSuite()
    suite.addTest(LauncherAddToDock('testMenuDock'))
    return suite

if __name__ == "__main__":
    unittest.TextTestRunner(verbosity=1).run(suite())