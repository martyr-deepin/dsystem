#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
import time
from lib import runner,utils
from lib.launcher import *

result = True
caseid = '33952'
casename = "all-542:点击任务栏程序隐藏启动器"

class LauncherHideByClickDock(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.startTime = time.time()
        cls.menuObj = root.application(appName='deepin-menu', description='/usr/lib/deepin-menu')
        cls.oldWindows = getAllWindows()
        #apps = Dock().getDockedApps()
        cls.app = '深度商店'

    @classmethod
    def tearDownClass(cls):
        seconds = "%.3f" % (time.time() - cls.startTime)
        minutes = utils.convertToMinutes(float(seconds))
        global result
        utils.commitresult(caseid, result, minutes)
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

    class MyTestResult(runner.MyTextTestResult):
        def addError(self, test, err):
            super(LauncherHideByClickDock.MyTestResult, self).addError(test, err)
            global result
            result = result and False

        def addFailure(self, test, err):
            super(LauncherHideByClickDock.MyTestResult, self).addFailure(test, err)
            global result
            result = result and False

if __name__ == "__main__":
    unittest.TextTestRunner(resultclass=LauncherHideByClickDock.MyTestResult).run(LauncherHideByClickDock.suite())
