#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from lib import runner,utils
from lib.launcher import *
from time import sleep

result = True
caseid = '52350'
casename = "all-2270:输入空格符搜索测试"

class MyTestResult(runner.MyTextTestResult):
    def addError(self, test, err):
        super(MyTestResult, self).addError(test, err)
        global result
        result = result and False

    def addFailure(self, test, err):
        super(MyTestResult, self).addFailure(test, err)
        global result
        result = result and False

class LauncherSpaceSearch(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.text1 = ' '
        cls.text2 = 'deepin   '
        cls.text3 = 'deepin music'
        cls.text4 = 'deepin   music'


    @classmethod
    def tearDownClass(cls):
        global result
        utils.commitresult(caseid, result)
    
        
    
    def testSpaceSearch1(self):
        launcher.searchApp(self.text1)
        sleep(2)
        apps = launcher.getLauncherAllApps()
        apps = ''.join(apps)
        sleep(2)
        launcher.exitLauncher()
        self.assertEqual('', apps)

    def testSpaceSearch2(self):
        deepinApps = launcher.getDefaultDeepinApps()
        launcher.searchApp(self.text2)
        sleep(2)
        apps = launcher.getLauncherAllApps()
        sleep(2)
        launcher.exitLauncher()
        self.assertEqual(deepinApps, apps)

    def testSpaceSearch3(self):
        launcher.searchApp(self.text3)
        sleep(2)
        apps = launcher.getLauncherAllApps()
        apps = ''.join(apps)
        sleep(2)
        launcher.exitLauncher()
        self.assertEqual('深度音乐', apps)

    def testSpaceSearch4(self):
        launcher.searchApp(self.text4)
        sleep(2)
        apps = launcher.getLauncherAllApps()
        apps = ''.join(apps)
        sleep(2)
        launcher.exitLauncher()
        self.assertEqual('', apps)


def suite():
    suite = unittest.TestSuite()
    suite.addTest(LauncherSpaceSearch('testSpaceSearch1'))
    suite.addTest(LauncherSpaceSearch('testSpaceSearch2'))
    suite.addTest(LauncherSpaceSearch('testSpaceSearch3'))
    suite.addTest(LauncherSpaceSearch('testSpaceSearch4'))
    return suite

if __name__ == "__main__":
    unittest.TextTestRunner(resultclass=MyTestResult).run(suite())
