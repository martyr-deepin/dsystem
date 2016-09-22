#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from lib import runner,utils
from lib.launcher import *
from lib.dde_dock import *

result = True

class ShowDesktopBtn(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.caseid = '80163'
        cls.casename = "all-2837:dock-显示桌面按钮测试"
        cls.btn = '显示桌面'
        cls.app = '深度商店'
        cls.appname = '深度商店 — Deepin Store'
        cls.desktop = 'dde-desktop'
        cls.oldWindows = getAllWindows()


    @classmethod
    def tearDownClass(cls):
        global result
        utils.commitresult(cls.caseid, result)
        cls.newWindows = getAllWindows()
        if len(cls.newWindows) - len(cls.oldWindows) == 1:
            cls.newWindows[-1].close(1)

    def testExitBtn(self):
        apps = Dock().getDockedApps()
        self.assertIn(self.btn,apps)

    def testShowDesktop(self):
        Dock().dockObj.child(self.app).click()
        winName = getWindowName()
        self.assertEqual(self.appname, winName)
        Dock().dockObj.child(self.btn).click()
        winName = getWindowName()
        self.assertEqual(self.desktop,winName)
        Dock().dockObj.child(self.btn).click()
        winName = getWindowName()
        self.assertEqual(self.appname,winName)

    def suite():
        suite = unittest.TestSuite()
        suite.addTest(ShowDesktopBtn('testExitBtn'))
        suite.addTest(ShowDesktopBtn('testShowDesktop'))
        return suite

    class MyTestResult(runner.MyTextTestResult):
        def addError(self, test, err):
            super(ShowDesktopBtn.MyTestResult, self).addError(test, err)
            global result
            result = result and False

        def addFailure(self, test, err):
            super(ShowDesktopBtn.MyTestResult, self).addFailure(test, err)
            global result
            result = result and False

if __name__ == "__main__":
    unittest.TextTestRunner(resultclass=ShowDesktopBtn.MyTestResult).run(ShowDesktopBtn.suite())
