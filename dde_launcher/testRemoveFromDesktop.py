#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import unittest
from lib import runner,utils
from lib.launcher import *
from lib.dde_dock import *

result = True

class LauncherRemoveFromDesktop(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.caseid = '33843'
        cls.casename = 'all-519:从桌面上移除'
        cls.menuObj = root.application(appName='deepin-menu', description='/usr/lib/deepin-menu')
        cls.QQName = 'QQ'

    @classmethod
    def tearDownClass(cls):
        global result
        utils.commitresult(cls.caseid, result)
        launcher.exitLauncher()

    def testMenuRemoveFromDesktop(self):
        launcher.menuDesktop(self.QQName)
        desktopFiles = getDesktopFiles()
        QQdesktopFile = 'apps.com.qq.im.desktop'
        self.assertNotIn(QQdesktopFile,desktopFiles)


    def suite():
        suite = unittest.TestSuite()
        suite.addTest(LauncherRemoveFromDesktop('testMenuRemoveFromDesktop'))
        return suite

    class MyTestResult(runner.MyTextTestResult):
        def addError(self, test, err):
            super(LauncherRemoveFromDesktop.MyTestResult, self).addError(test, err)
            global result
            result = result and False

        def addFailure(self, test, err):
            super(LauncherRemoveFromDesktop.MyTestResult, self).addFailure(test, err)
            global result
            result = result and False

if __name__ == "__main__":
    unittest.TextTestRunner(resultclass=LauncherRemoveFromDesktop.MyTestResult).run(LauncherRemoveFromDesktop.suite())