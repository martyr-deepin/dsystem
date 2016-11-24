#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
import time
from lib import runner,utils
from lib.launcher import *
from time import sleep

result = True
caseid = '52146'
casename = "all-2233:搜索框有字符串时，排序开关功能测试"

class LauncherSortWithSearch(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.startTime = time.time()
        cls.text = '深度音乐'
        cls.defaultMode = launcher.getLauncherMode()

    @classmethod
    def tearDownClass(cls):
        seconds = "%.3f" % (time.time() - cls.startTime)
        minutes = utils.convertToMinutes(float(seconds))
        global result
        utils.commitresult(caseid, result, minutes)
        mode = launcher.getLauncherMode()
        if mode != cls.defaultMode:
            launcher.launcherObj.child('mode-toggle-button').click()
        launcher.exitLauncher()


    def test_switch1(self):
        launcher.openLauncher()
        launcher.launcherObj.child('search-edit').click()
        launcher.launcherObj.child('search-edit').text = self.text
        launcher.launcherObj.child('mode-toggle-button').click()
        mode = launcher.getLauncherMode()
        self.assertNotEqual(self.defaultMode, mode)

    def test_switch2(self):
        launcher.launcherObj.child('mode-toggle-button').click()
        mode = launcher.getLauncherMode()
        self.assertEqual(self.defaultMode, mode)


    def suite():
        suite = unittest.TestSuite()
        suite.addTest(LauncherSortWithSearch('test_switch1'))
        suite.addTest(LauncherSortWithSearch('test_switch2'))
        return suite

    class MyTestResult(runner.MyTextTestResult):
        def addError(self, test, err):
            super(LauncherSortWithSearch.MyTestResult, self).addError(test, err)
            global result
            result = result and False

        def addFailure(self, test, err):
            super(LauncherSortWithSearch.MyTestResult, self).addFailure(test, err)
            global result
            result = result and False

if __name__ == "__main__":
    unittest.TextTestRunner(resultclass=LauncherSortWithSearch.MyTestResult).run(LauncherSortWithSearch.suite())
