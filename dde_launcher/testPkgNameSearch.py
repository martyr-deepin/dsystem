#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from lib import executeTestCase
import time
from lib import runner,utils
from lib.launcher import *
from time import sleep

result = True
casename = "all-509:中文字符串搜索"

class LauncherPkgNameSearch(unittest.TestCase):
    caseid = '33795'
    @classmethod
    def setUpClass(cls):
        cls.text = 'deepin-appstore'
        cls.appName = '深度商店'


    @classmethod
    def tearDownClass(cls):
        pass

    def testPkgNameSearch1(self):
        launcher.searchApp(self.text1)
        sleep(2)
        apps = launcher.getLauncherAllApps()
        #apps = ''.join(apps)
        sleep(2)
        launcher.exitLauncher()
        self.assertIn(self.appName1, apps)

    def testPkgNameSearch2(self):
        launcher.searchApp(self.text)
        sleep(2)
        apps = launcher.getLauncherAllApps()
        apps = ''.join(apps)
        #sleep(2)
        launcher.exitLauncher()
        self.assertEqual(self.appName, apps)

    def suite():
        suite = unittest.TestSuite()
        #suite.addTest(LauncherPkgNameSearch('testPkgNameSearch1'))
        suite.addTest(LauncherPkgNameSearch('testPkgNameSearch2'))
        return suite


if __name__ == "__main__":
    executeTestCase.runTest(LauncherPkgNameSearch)
