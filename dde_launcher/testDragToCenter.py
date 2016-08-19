#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from lib import runner,utils
from lib.launcher import *

result = True
caseid = '33827'
casename = "all-515:左键拖动调整位置"

class MyTestResult(runner.MyTextTestResult):
    def addError(self, test, err):
        super(MyTestResult, self).addError(test, err)
        global result
        result = result and False

    def addFailure(self, test, err):
        super(MyTestResult, self).addFailure(test, err)
        global result
        result = result and False

class LauncherDragToCenter(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.menuObj = root.application(appName='deepin-menu', description='/usr/lib/deepin-menu')

    @classmethod
    def tearDownClass(cls):
        global result
        utils.commitresult(caseid, result)
        launcher.dragToFirstLeftKey()

    def testDragToCenterLeftKey(self):
        apps = launcher.getLauncherAllApps()
        first = apps[0]
        launcher.dragToCenterLeftKey()
        apps = launcher.getLauncherAllApps()
        new_center = apps[17]
        self.assertEqual(first, new_center)

    def testDragToCenterRightKey(self):
        apps = launcher.getLauncherAllApps()
        first = apps[0]
        launcher.dragToCenterRightKey()
        apps = launcher.getLauncherAllApps()
        new_center = apps[17]
        self.assertNotEqual(first, new_center)
        self.testLauncherMenuOpened()
        launcher.exitLauncher()
        launcher.exitLauncher()

    def testLauncherMenuOpened(self):
        kids = self.menuObj.children
        self.assertEqual(kids[0].name, "DesktopMenu")

def suite():
    suite = unittest.TestSuite()
    suite.addTest(LauncherDragToCenter('testDragToCenterLeftKey'))
    suite.addTest(LauncherDragToCenter('testDragToCenterRightKey'))
    return suite

if __name__ == "__main__":
    unittest.TextTestRunner(resultclass=MyTestResult).run(suite())
