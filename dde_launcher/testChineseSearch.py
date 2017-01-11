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
casename = "all-509:中文字符串搜索"

class LauncherChineseSearch(unittest.TestCase):
    caseid = '33795'
    @classmethod
    def setUpClass(cls):
        # cls.text1 = '深度音乐'
        cls.text1 = translation.charTrans.getCharTrans('deepin-music')

    @classmethod
    def tearDownClass(cls):
        pass

    def testChineseSearch1(self):
        launcher.searchApp(self.text1)
        sleep(2)
        apps = launcher.getLauncherAllApps()
        apps = ''.join(apps)
        #sleep(2)
        launcher.exitLauncher()
        self.assertEqual(self.text1, apps)

    def testChineseSearch2(self):
        launcher.searchApp(self.text2)
        sleep(2)
        apps = launcher.getLauncherAllApps()
        #apps = ''.join(apps)
        #sleep(2)
        launcher.exitLauncher()
        self.assertIn(self.text1, apps)


    def suite():
        suite = unittest.TestSuite()
        suite.addTest(LauncherChineseSearch('testChineseSearch1'))
        #suite.addTest(LauncherChineseSearch('testChineseSearch2'))
        return suite


if __name__ == "__main__":
    executeTestCase.runTest(LauncherChineseSearch)
