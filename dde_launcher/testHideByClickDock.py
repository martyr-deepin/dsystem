#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from lib import executeTestCase
from lib import translation
import time
from lib import runner,utils
from lib.launcher import *

result = True
casename = "all-542:点击任务栏程序隐藏启动器"

class LauncherHideByClickDock(unittest.TestCase):
    caseid = '33952'
    @classmethod
    def setUpClass(cls):
        cls.menuObj = root.application(appName='deepin-menu', description='/usr/lib/deepin-menu')
        cls.oldWindows = getAllWindows()
        #apps = Dock().getDockedApps()
        # cls.app = '深度商店'
        cls.app = translation.charTrans.getCharTrans('deepin-appstore')
    @classmethod
    def tearDownClass(cls):
        launcher.exitLauncher()
        cls.newWindows = getAllWindows()
        if len(cls.newWindows) > len(cls.oldWindows):
            for win in cls.newWindows[len(cls.oldWindows):]:
                win.close(1)
        win = findWindow('dde-launcher')
        if win is not None:
            launcher.exitLauncher()

    def testClickApp(self):
        launcher.openLauncher()
        Dock().dockObj.child(self.app).click()
        win = findWindow('dde-launcher')
        self.assertIsNone(win)

    def testClickBlank(self):
        launcher.openLauncher()
        position = Dock().dockObj.child('dock-mainwindow').position
        size = Dock().dockObj.child('dock-mainwindow').size
        blank_left = (position[0]+2,position[1]+2)
        pyautogui.click(blank_left)
        win = findWindow('dde-launcher')
        self.assertIsNotNone(win)

    def suite():
        suite = unittest.TestSuite()
        suite.addTest(LauncherHideByClickDock('testClickApp'))
        suite.addTest(LauncherHideByClickDock('testClickBlank'))
        return suite


if __name__ == "__main__":
    executeTestCase.runTest(LauncherHideByClickDock)
