#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from lib import executeTestCase
from lib import translation
from lib.launcher import *
from time import sleep

result = True
casename = "all-510:英文字符串搜索"

class LauncherEnglishSearch(unittest.TestCase):
    caseid = '33803'
    @classmethod
    def setUpClass(cls):
        # cls.appName1 = '深度音乐'
        # cls.appName2 = '网易云音乐'
        cls.appName1 = translation.charTrans.getCharTrans('deepin-music')
        cls.appName2 = translation.charTrans.getCharTrans('netease-cloud-music')
        cls.text1 = 'deepin music'
        cls.text2 = 'music'
        cls.text3 = 'deepin'

    @classmethod
    def tearDownClass(cls):
        pass

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


if __name__ == "__main__":
    executeTestCase.runTest(LauncherEnglishSearch)
