#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import unittest
from lib import executeTestCase
import time
from lib import runner,utils
from lib.launcher import *
from lib.dde_dock import *

result = True
caseid = '33902'
casename = 'all-532:应用安装之后左侧分类更新测试'

class LauncherSortApp(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.menuObj = root.application(appName='deepin-menu', description='/usr/lib/deepin-menu')
        cls.installAppName = 'robomongo'


    @classmethod
    def tearDownClass(cls):
        kids = launcher.getKidsCategory('development')
        if 'Robomongo' in kids:
            launcher.removeApp(cls.installAppName)
        launcher.checkLableKids('internet')
        launcher.freeMode()
        launcher.exitLauncher()


    def testSortApp(self):
        launcher.installApp(self.installAppName)
        launcher.checkLableKids('development')
        kids = launcher.getKidsCategory('development')
        launcher.exitLauncher()
        self.assertIn('Robomongo',kids)


    def suite():
        suite = unittest.TestSuite()
        suite.addTest(LauncherSortApp('testSortApp'))
        return suite


if __name__ == "__main__":
    runTest(LauncherSortApp.suite())
