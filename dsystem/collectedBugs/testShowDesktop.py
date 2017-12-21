#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from lib import executeTestCase
from lib import runner,utils
from lib.launcher import *
from lib.dde_dock import *

result = True
casename = "all-2837:dock-显示桌面按钮测试"

class ShowDesktopBtn(unittest.TestCase):
    caseid = '80163'
    @classmethod
    def setUpClass(cls):
        cls.btn = '显示桌面'
        cls.app = '深度商店'
        cls.appname = '深度商店 — Deepin Store'
        cls.desktop = 'dde-desktop'
        cls.oldWindows = getAllWindows()


    @classmethod
    def tearDownClass(cls):
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

if __name__ == "__main__":
    executeTestCase.runTest(ShowDesktopBtn)
