#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
import time
from lib import runner,utils
from lib.launcher import *
from time import sleep

result = True
caseid = '33803'
casename = "all-510:英文字符串搜索"

class LauncherEnglishSearch(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.startTime = time.time()
        cls.appName1 = '深度音乐'
        cls.appName2 = '网易云音乐'
        cls.text1 = 'deepin music'
        cls.text2 = 'music'
        cls.text3 = 'deepin'

    @classmethod
    def tearDownClass(cls):
        seconds = "%.3f" % (time.time() - cls.startTime)
        minutes = utils.convertToMinutes(float(seconds))
        global result
        utils.commitresult(caseid, result, minutes)

    def testEnglishSearch1(self):
        launcher.searchApp(self.text1)
        sleep(2)
        apps = launcher.getLauncherAllApps()
        apps = ''.join(apps)
        #sleep(2)
        launcher.exitLauncher()
        self.assertEqual(self.appName1, apps)

    def testEnglishSearch2(self):
        launcher.searchApp(self.text2)
        sleep(2)
        apps = launcher.getLauncherAllApps()
        #sleep(2)
        launcher.exitLauncher()
        self.assertIn(self.appName1, apps)
        self.assertIn(self.appName2, apps)

    def testEnglishSearch3(self):
        launcher.searchApp(self.text3)
        sleep(2)
        apps = launcher.getLauncherAllApps()
        defaultdeepinapps = launcher.getDefaultDeepinApps()
        launcher.exitLauncher()
        self.assertListEqual(sorted(defaultdeepinapps), sorted(apps))

    def suite():
        suite = unittest.TestSuite()
        suite.addTest(LauncherEnglishSearch('testEnglishSearch1'))
        suite.addTest(LauncherEnglishSearch('testEnglishSearch2'))
        suite.addTest(LauncherEnglishSearch('testEnglishSearch3'))
        return suite

    class MyTestResult(runner.MyTextTestResult):
        def addError(self, test, err):
            super(LauncherEnglishSearch.MyTestResult, self).addError(test, err)
            global result
            result = result and False

        def addFailure(self, test, err):
            super(LauncherEnglishSearch.MyTestResult, self).addFailure(test, err)
            global result
            result = result and False

if __name__ == "__main__":
    unittest.TextTestRunner(resultclass=LauncherEnglishSearch.MyTestResult).run(LauncherEnglishSearch.suite())
