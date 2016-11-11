#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
import time
from lib import runner,utils
from lib.launcher import *

result = True
caseid = '33906'
casename = "all-533:launcher打开时对enter键的响应"

class LauncherEnterKey(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.startTime = time.time()
        cls.appName = 'Google Chrome'
        cls.googleTitleName = '打开新的标签页 - Google Chrome'
        cls.oldWindows = getAllWindows()

    @classmethod
    def tearDownClass(cls):
        seconds = "%.3f" % (time.time() - cls.startTime)
        minutes = utils.convertToMinutes(float(seconds))
        global result
        utils.commitresult(caseid, result, minutes)
        cls.newWindows = getAllWindows()
        if len(cls.newWindows) - len(cls.oldWindows) == 1:
            cls.newWindows[-1].close(1)

    def testEnterKey(self):
        launcher.openLauncher()
        launcher.launcherObj.child(self.appName).point()
        pyautogui.press('enter')
        win = getWindowName()
        self.assertEqual(self.googleTitleName, win)


    def suite():
        suite = unittest.TestSuite()
        suite.addTest(LauncherEnterKey('testEnterKey'))
        return suite

    class MyTestResult(runner.MyTextTestResult):
        def addError(self, test, err):
            super(LauncherEnterKey.MyTestResult, self).addError(test, err)
            global result
            result = result and False

        def addFailure(self, test, err):
            super(LauncherEnterKey.MyTestResult, self).addFailure(test, err)
            global result
            result = result and False

if __name__ == "__main__":
    unittest.TextTestRunner(resultclass=LauncherEnterKey.MyTestResult).run(LauncherEnterKey.suite())
