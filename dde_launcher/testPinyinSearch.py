#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from lib import executeTestCase
from lib import translation
import time
from lib import runner,utils
from lib.launcher import *
from time import sleep

result = True
casename = "all-2140:拼音字符串搜索"

class LauncherPinyinSearch(unittest.TestCase):
    caseid = '45706'
    @classmethod
    def setUpClass(cls):
        # cls.appName = '深度截图'
        cls.appName = translation.charTrans.getCharTrans('deepin-screenshot')
        cls.text1 = 'shendujietu'
        cls.text2 = 'sdjt'
        cls.text3 = 'SDJt'
        cls.text4 = 'djt'

    @classmethod
    def tearDownClass(cls):
        pass

    def testPinyinSearch1(self):
        launcher.searchApp(self.text1)
        sleep(2)
        apps = launcher.getLauncherAllApps()
        apps = ''.join(apps)
        #sleep(2)
        launcher.exitLauncher()
        self.assertEqual(self.appName, apps)


    def testPinyinSearch2(self):
        launcher.searchApp(self.text2)
        sleep(2)
        apps = launcher.getLauncherAllApps()
        apps = ''.join(apps)
        #sleep(2)
        launcher.exitLauncher()
        self.assertEqual(self.appName, apps)


    def testPinyinSearch3(self):
        launcher.searchApp(self.text3)
        sleep(2)
        apps = launcher.getLauncherAllApps()
        apps = ''.join(apps)
        #sleep(2)
        launcher.exitLauncher()
        self.assertEqual(self.appName, apps)

    def testPinyinSearch4(self):
        launcher.searchApp(self.text4)
        sleep(2)
        apps = launcher.getLauncherAllApps()
        #apps = ''.join(apps)
        #sleep(2)
        launcher.exitLauncher()
        self.assertIn(self.appName, apps)


    def suite():
        suite = unittest.TestSuite()
        suite.addTest(LauncherPinyinSearch('testPinyinSearch1'))
        suite.addTest(LauncherPinyinSearch('testPinyinSearch2'))
        suite.addTest(LauncherPinyinSearch('testPinyinSearch3'))
        suite.addTest(LauncherPinyinSearch('testPinyinSearch4'))
        return suite


if __name__ == "__main__":
    executeTestCase.runTest(LauncherPinyinSearch)
