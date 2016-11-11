#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
import time
import time
from lib import utils
from lib import runner
from dogtail import rawinput

result = True
caseid = '68517'
casename = "all-2499:四个位置的一直显示测试"

class DockKeepShownOtherDirection(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.startTime = time.time()
        cls.ddedockobject = utils.getDdeDockObject()
        cls.defaultdisplaymode = utils.getDdeDockDisplayMode()
        cls.defaultposition = utils.getDdeDockPosition()
        cls.defaulthidemode = utils.getDdeDockHideMode()
        cls.dock_mainwindow = "dock-mainwindow"
        cls.filemanager = "深度文件管理器"
        cls.filemanager_windowname = "深度文件管理器"

        if utils.dock.displaymode_fashion != cls.defaultdisplaymode:
            utils.setDdeDockDisplayMode(utils.dock.displaymode_fashion)

        if utils.dock.position_bottom != cls.defaultposition:
            utils.setDdeDockPosition(utils.dock.position_bottom)

        if utils.dock.hidemode_keepshowing != cls.defaulthidemode:
            utils.setDdeDockHideMode(utils.dock.hidemode_keepshowing)

    @classmethod
    def tearDownClass(cls):
        seconds = "%.3f" % (time.time() - cls.startTime)
        minutes = utils.convertToMinutes(float(seconds))
        global result
        utils.commitresult(caseid, result, minutes)

        if utils.getDdeDockDisplayMode() != utils.dock.displaymode_fashion:
            utils.setDdeDockDisplayMode(utils.dock.displaymode_fashion)

        if utils.getDdeDockPosition() != utils.dock.position_bottom:
            utils.setDdeDockPosition(utils.dock.position_bottom)

        if utils.getDdeDockHideMode() != utils.dock.hidemode_keepshowing:
            utils.setDdeDockHideMode(utils.dock.hidemode_keepshowing)

        win = utils.findWindow(cls.filemanager_windowname)
        if win != None:
            win.unmaximize()
            win.close(time.time())

    def testOpenFileManager(self):
        launcher = self.ddedockobject.child("Launcher")
        launcher.point()
        filemanager = self.ddedockobject.child(self.filemanager)
        filemanager.click()
        rawinput.click(int(utils.resolution.width/2), int(utils.resolution.height/2))
        time.sleep(2)
        win = utils.findWindow(self.filemanager_windowname)
        self.assertTrue(win != None)

    def testMaximizeFileManager(self):
        win = utils.findWindow(self.filemanager_windowname)
        win.maximize()
        time.sleep(2)
        self.assertTrue(win != None)

    def testMinimizeFileManager(self):
        win = utils.findWindow(self.filemanager_windowname)
        win.minimize()
        time.sleep(1)
        self.assertTrue(win != None)
        win_test = utils.findWindow(self.filemanager_windowname)
        self.assertTrue(win_test.is_minimized())

    def testActivateFileManager(self):
        win = utils.findWindow(self.filemanager_windowname)
        win.activate(time.time())
        self.assertTrue(win != None)
        self.assertTrue(win.is_maximized())

    def testCheckDockSize(self):
        main_window = self.ddedockobject.child(self.dock_mainwindow)
        (width, height) = main_window.size
        self.assertTrue(height > 1)
        self.assertTrue(width > 1)

    def testExChangeDisplayMode(self):
        if utils.getDdeDockDisplayMode() == utils.dock.displaymode_fashion:
            utils.setDdeDockDisplayMode(utils.dock.displaymode_efficient)
        elif utils.getDdeDockDisplayMode() == utils.dock.displaymode_efficient:
            utils.setDdeDockDisplayMode(utils.dock.displaymode_fashion)

    def testChangePosition(self):
        if utils.getDdeDockPosition() == utils.dock.position_bottom:
            utils.setDdeDockPosition(utils.dock.position_top)
        elif utils.getDdeDockPosition() == utils.dock.position_top:
            utils.setDdeDockPosition(utils.dock.position_right)
        elif utils.getDdeDockPosition() == utils.dock.position_right:
            utils.setDdeDockPosition(utils.dock.position_left)

    def suite():
        suite = unittest.TestSuite()
        suite.addTest(DockKeepShownOtherDirection('testOpenFileManager'))

        # top
        suite.addTest(DockKeepShownOtherDirection('testChangePosition'))
        suite.addTest(DockKeepShownOtherDirection('testMaximizeFileManager'))
        suite.addTest(DockKeepShownOtherDirection('testCheckDockSize'))
        suite.addTest(DockKeepShownOtherDirection('testMinimizeFileManager'))
        suite.addTest(DockKeepShownOtherDirection('testCheckDockSize'))
        suite.addTest(DockKeepShownOtherDirection('testExChangeDisplayMode'))
        suite.addTest(DockKeepShownOtherDirection('testActivateFileManager'))
        suite.addTest(DockKeepShownOtherDirection('testCheckDockSize'))
        suite.addTest(DockKeepShownOtherDirection('testMinimizeFileManager'))
        suite.addTest(DockKeepShownOtherDirection('testCheckDockSize'))

        # right
        suite.addTest(DockKeepShownOtherDirection('testChangePosition'))
        suite.addTest(DockKeepShownOtherDirection('testMaximizeFileManager'))
        suite.addTest(DockKeepShownOtherDirection('testCheckDockSize'))
        suite.addTest(DockKeepShownOtherDirection('testMinimizeFileManager'))
        suite.addTest(DockKeepShownOtherDirection('testCheckDockSize'))
        suite.addTest(DockKeepShownOtherDirection('testExChangeDisplayMode'))
        suite.addTest(DockKeepShownOtherDirection('testActivateFileManager'))
        suite.addTest(DockKeepShownOtherDirection('testCheckDockSize'))
        suite.addTest(DockKeepShownOtherDirection('testMinimizeFileManager'))
        suite.addTest(DockKeepShownOtherDirection('testCheckDockSize'))

        # left
        suite.addTest(DockKeepShownOtherDirection('testChangePosition'))
        suite.addTest(DockKeepShownOtherDirection('testMaximizeFileManager'))
        suite.addTest(DockKeepShownOtherDirection('testCheckDockSize'))
        suite.addTest(DockKeepShownOtherDirection('testMinimizeFileManager'))
        suite.addTest(DockKeepShownOtherDirection('testCheckDockSize'))
        suite.addTest(DockKeepShownOtherDirection('testExChangeDisplayMode'))
        suite.addTest(DockKeepShownOtherDirection('testActivateFileManager'))
        suite.addTest(DockKeepShownOtherDirection('testCheckDockSize'))
        suite.addTest(DockKeepShownOtherDirection('testMinimizeFileManager'))
        suite.addTest(DockKeepShownOtherDirection('testCheckDockSize'))

        return suite

    class MyTestResult(runner.MyTextTestResult):
        def addError(self, test, err):
            super(DockKeepShownOtherDirection.MyTestResult, self).addError(test, err)
            global result
            result = result and False

        def addFailure(self, test, err):
            super(DockKeepShownOtherDirection.MyTestResult, self).addFailure(test, err)
            global result
            result = result and False

if __name__ == "__main__":
    unittest.TextTestRunner(resultclass=DockKeepShownOtherDirection.MyTestResult).run(DockKeepShownOtherDirection.suite())
