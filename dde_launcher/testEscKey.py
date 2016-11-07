#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from lib import runner,utils
from lib.launcher import *

result = True
caseid = '33931'
casename = "all-538:ESC隐藏启动器"

class LauncherEscKey(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.menuObj = root.application(appName='deepin-menu', description='/usr/lib/deepin-menu')
        apps = launcher.getLauncherAllApps()
        cls.appName = apps[17]
        print ('Ready to click right key in %s' % cls.appName)

    @classmethod
    def tearDownClass(cls):
        global result
        utils.commitresult(caseid, result)
        launcher.exitLauncher()


    def testQuitLauncher(self):
        launcher.openLauncher()
        pyautogui.press('esc')
        win = findWindow('dde-launcher')
        self.assertIsNone(win)

    def testQuitLauncherMenu(self):
        launcher.openLauncher()
        launcher.launcherObj.child(self.appName).click(3)
        if len(self.menuObj.children) > 0:
            pyautogui.press('esc')
        self.assertEqual(len(self.menuObj.children), 0)

    def testRepeatEscKey(self):
        for i in range(10):
            launcher.openLauncher()
            launcher.exitLauncher()
            win = findWindow('dde-launcher')
            self.assertIsNone(win)

    def suite():
        suite = unittest.TestSuite()
        suite.addTest(LauncherEscKey('testQuitLauncher'))
        suite.addTest(LauncherEscKey('testQuitLauncherMenu'))
        suite.addTest(LauncherEscKey('testRepeatEscKey'))
        return suite

    class MyTestResult(runner.MyTextTestResult):
        def addError(self, test, err):
            super(LauncherEscKey.MyTestResult, self).addError(test, err)
            global result
            result = result and False

        def addFailure(self, test, err):
            super(LauncherEscKey.MyTestResult, self).addFailure(test, err)
            global result
            result = result and False

if __name__ == "__main__":
    unittest.TextTestRunner(resultclass=LauncherEscKey.MyTestResult).run(LauncherEscKey.suite())
