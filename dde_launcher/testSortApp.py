#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import unittest
from lib import runner,utils
from lib.launcher import *
from lib.dde_dock import *

result = True
caseid = '33902'
casename = 'all-532:应用安装之后左侧分类更新测试'

class MyTestResult(runner.MyTextTestResult):
    def addError(self, test, err):
        super(MyTestResult, self).addError(test, err)
        global result
        result = result and False

    def addFailure(self, test, err):
        super(MyTestResult, self).addFailure(test, err)
        global result
        result = result and False

class LauncherSortApp(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.menuObj = root.application(appName='deepin-menu', description='/usr/lib/deepin-menu')
        cls.installAppName = 'robomongo'
        cls.oldWindows = getAllWindows()

    @classmethod
    def tearDownClass(cls):
        global result
        utils.commitresult(caseid, result)
        cls.newWindows = getAllWindows()
        if len(cls.newWindows) - len(cls.oldWindows) == 1: 
            cls.newWindows[-1].close(1)
        kids = launcher.getKidsCategory('development')
        if 'Robomongo' in kids:
            launcher.removeApp(cls.installAppName)
        launcher.freeMode()


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
    unittest.TextTestRunner(resultclass=MyTestResult).run(suite())