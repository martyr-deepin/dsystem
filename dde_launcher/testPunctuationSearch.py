#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from lib import executeTestCase
import time
from lib import runner,utils
from lib.launcher import *
from time import sleep

result = True
caseid = '52345'
casename = "all-2269:输入标点符号测试"

class LauncherPunctuationSearch(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.text1 = '! '
        cls.text2 = '*'
        cls.text3 = 'deepin*'

    @classmethod
    def tearDownClass(cls):
        pass

    def testPunctuationSearch1(self):
        launcher.searchApp(self.text1)
        sleep(2)
        apps = launcher.getLauncherAllApps()
        apps = ''.join(apps)
        sleep(2)
        launcher.exitLauncher()
        self.assertEqual('', apps)

    def testPunctuationSearch2(self):
        launcher.searchApp(self.text2)
        sleep(2)
        apps = launcher.getLauncherAllApps()
        apps = ''.join(apps)
        sleep(2)
        launcher.exitLauncher()
        self.assertEqual('', apps)

    def testPunctuationSearch3(self):
        launcher.searchApp(self.text3)
        sleep(2)
        apps = launcher.getLauncherAllApps()
        apps = ''.join(apps)
        sleep(2)
        launcher.exitLauncher()
        self.assertEqual('', apps)


    def suite():
        suite = unittest.TestSuite()
        suite.addTest(LauncherPunctuationSearch('testPunctuationSearch1'))
        suite.addTest(LauncherPunctuationSearch('testPunctuationSearch2'))
        suite.addTest(LauncherPunctuationSearch('testPunctuationSearch3'))
        return suite


if __name__ == "__main__":
    runTest(LauncherPunctuationSearch.suite())
