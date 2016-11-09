#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from lib import runner,utils
from lib.launcher import *
from time import sleep

result = True
caseid = '45706'
casename = "all-2140:拼音字符串搜索"

class LauncherPinyinSearch(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.startTime = time.time()
        cls.appName = '图像查看器'
        cls.text1 = 'tuxiangchakanqi'
        cls.text2 = 'txckq'
        cls.text3 = 'TXCkq'
        cls.text4 = 'ckq'

    @classmethod
    def tearDownClass(cls):
        seconds = "%.3f" % (time.time() - cls.startTime)
        minutes = utils.convertToMinutes(float(seconds))
        global result
        utils.commitresult(caseid, result, minutes)

    def testPinyinSearch1(self):
        launcher.searchApp(self.text1)
        sleep(2)
        apps = launcher.getLauncherAllApps()
        apps = ''.join(apps)
        sleep(2)
        launcher.exitLauncher()
        self.assertEqual(self.appName, apps)


    def testPinyinSearch2(self):
        launcher.searchApp(self.text2)
        sleep(2)
        apps = launcher.getLauncherAllApps()
        apps = ''.join(apps)
        sleep(2)
        launcher.exitLauncher()
        self.assertEqual(self.appName, apps)


    def testPinyinSearch3(self):
        launcher.searchApp(self.text3)
        sleep(2)
        apps = launcher.getLauncherAllApps()
        apps = ''.join(apps)
        sleep(2)
        launcher.exitLauncher()
        self.assertEqual(self.appName, apps)

    def testPinyinSearch4(self):
        launcher.searchApp(self.text4)
        sleep(2)
        apps = launcher.getLauncherAllApps()
        #apps = ''.join(apps)
        sleep(2)
        launcher.exitLauncher()
        self.assertNotIn(self.appName, apps)


    def suite():
        suite = unittest.TestSuite()
        suite.addTest(LauncherPinyinSearch('testPinyinSearch1'))
        suite.addTest(LauncherPinyinSearch('testPinyinSearch2'))
        suite.addTest(LauncherPinyinSearch('testPinyinSearch3'))
        suite.addTest(LauncherPinyinSearch('testPinyinSearch4'))
        return suite

    class MyTestResult(runner.MyTextTestResult):
        def addError(self, test, err):
            super(LauncherPinyinSearch.MyTestResult, self).addError(test, err)
            global result
            result = result and False

        def addFailure(self, test, err):
            super(LauncherPinyinSearch.MyTestResult, self).addFailure(test, err)
            global result
        result = result and False

if __name__ == "__main__":
    unittest.TextTestRunner(resultclass=LauncherPinyinSearch.MyTestResult).run(LauncherPinyinSearch.suite())
