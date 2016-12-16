#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from lib import executeTestCase
import time
from lib import runner,utils
from lib.launcher import *
from time import sleep

result = True
casename = "all-2270:输入空格符搜索测试"

class LauncherSpaceSearch(unittest.TestCase):
    caseid = '52350'
    @classmethod
    def setUpClass(cls):
        cls.text1 = ' '
        cls.text2 = 'deepin   '
        cls.text3 = 'deepin music'
        cls.text4 = 'deepin   music'
        launcher.openLauncher()
        launcher.exitLauncher()
        cls.defaultApps = launcher.getLauncherAllApps()

    @classmethod
    def tearDownClass(cls):
        pass

    def testSpaceSearch1(self):
        launcher.searchApp(self.text1)
        sleep(2)
        apps = launcher.getLauncherAllApps()
        #apps = ''.join(apps)
        sleep(2)
        launcher.exitLauncher()
        self.assertListEqual(apps, self.defaultApps)

    def testSpaceSearch2(self):
        deepinApps = launcher.getDefaultDeepinApps()
        launcher.searchApp(self.text2)
        sleep(2)
        apps = launcher.getLauncherAllApps()
        sleep(2)
        launcher.exitLauncher()
        self.assertEqual(sorted(deepinApps), sorted(apps))

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
    executeTestCase.runTest(LauncherSpaceSearch)
