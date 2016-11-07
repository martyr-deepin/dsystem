#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import unittest
from lib import runner,utils
from lib.launcher import *
from lib.dde_dock import *

result = True
caseid = '33846'
casename = 'all-520:发送到桌面'

class LauncherSendToDesktop(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.menuObj = root.application(appName='deepin-menu', description='/usr/lib/deepin-menu')
        cls.QQName = 'QQ'

    @classmethod
    def tearDownClass(cls):
        global result
        utils.commitresult(caseid, result)
        launcher.exitLauncher()

    def testMenuSendToDesktop(self):
        launcher.menuDesktop(self.QQName)
        desktopFiles = getDesktopFiles()
        QQdesktopFile = 'apps.com.qq.im.desktop'
        self.assertIn(QQdesktopFile,desktopFiles)

    def suite():
        suite = unittest.TestSuite()
        suite.addTest(LauncherSendToDesktop('testMenuSendToDesktop'))
        return suite

    class MyTestResult(runner.MyTextTestResult):
        def addError(self, test, err):
            super(LauncherSendToDesktop.MyTestResult, self).addError(test, err)
            global result
            result = result and False

        def addFailure(self, test, err):
            super(LauncherSendToDesktop.MyTestResult, self).addFailure(test, err)
            global result
            result = result and False

if __name__ == "__main__":
    unittest.TextTestRunner(resultclass=LauncherSendToDesktopMyTestResult).run(LauncherSendToDesktop.suite())
