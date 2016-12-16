#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from lib import executeTestCase
import time
from lib import runner,utils
from lib.launcher import *
from time import sleep

result = True
casename = "all-2233:搜索框有字符串时，排序开关功能测试"

class LauncherSortWithSearch(unittest.TestCase):
    caseid = '52146'
    @classmethod
    def setUpClass(cls):
        cls.text = '深度音乐'
        cls.defaultMode = launcher.getLauncherMode()

    @classmethod
    def tearDownClass(cls):
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


if __name__ == "__main__":
    executeTestCase.runTest(LauncherSortWithSearch)
