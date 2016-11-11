#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import unittest
import time
from lib import runner,utils
from lib.launcher import *
from lib.dde_dock import *

result = True
caseid = '33840'
casename = 'all-518:添加到任务栏'

class LauncherAddToDock(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.startTime = time.time()
        cls.menuObj = root.application(appName='deepin-menu', description='/usr/lib/deepin-menu')
        cls.googleName = 'Google Chrome'
        dockApps = Dock().getAllDockApps()
        if 'google-chrome' in dockApps:
            Dock().unDockApp(cls.googleName)
        launcher.freeMode()

    @classmethod
    def tearDownClass(cls):
        seconds = "%.3f" % (time.time() - cls.startTime)
        minutes = utils.convertToMinutes(float(seconds))
        global result
        utils.commitresult(caseid, result, minutes)
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
