#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import unittest
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
        global result
        utils.commitresult(caseid, result)
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

    class MyTestResult(runner.MyTextTestResult):
        def addError(self, test, err):
            super(LauncherSortApp.MyTestResult, self).addError(test, err)
            global result
            result = result and False

        def addFailure(self, test, err):
            super(LauncherSortApp.MyTestResult, self).addFailure(test, err)
            global result
            result = result and False

if __name__ == "__main__":
    unittest.TextTestRunner(resultclass=LauncherSortApp.MyTestResult).run(LauncherSortApp.suite())
