#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from lib import runner,utils
from lib.launcher import *

result = True

class LauncherHideByClickDock(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.caseid = '33952'
        cls.casename = "all-542:点击任务栏程序隐藏启动器"
        cls.menuObj = root.application(appName='deepin-menu', description='/usr/lib/deepin-menu')
        cls.oldWindows = getAllWindows()
        apps = Dock().getDockedApps()
        cls.app = apps[1]


    @classmethod
    def tearDownClass(cls):
        global result
        utils.commitresult(cls.caseid, result)
        launcher.exitLauncher()
        cls.newWindows = getAllWindows()
        if len(cls.newWindows) - len(cls.oldWindows) == 1:
            cls.newWindows[-1].close(1)

    
    def testClickApp(self):
        launcher.openLauncher()
        Dock().dockObj.child(self.app).click()
        win = findWindow('dde-launcher')
        self.assertIsNone(win)


    def testClickBlank(self):
        launcher.openLauncher()
        position = Dock().dockObj.child('dock-mainwindow').position
        size = Dock().dockObj.child('dock-mainwindow').size
        blank = (position[0]+5,position[1]+size[1]/2)
        pyautogui.click(blank)
        win = findWindow('dde-launcher')
        self.assertIsNotNone(win)


    def suite():
        suite = unittest.TestSuite()
        suite.addTest(LauncherHideByClickDock('testClickApp'))
        #suite.addTest(LauncherHideByClickDock('testClickBlank'))
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
