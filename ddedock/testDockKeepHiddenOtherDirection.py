#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
import time
from lib import utils
from lib import runner
from dogtail import rawinput

result = True

class DockKeepHiddenOtherDirection(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.caseid = '68521'
        cls.casename = "all-2500:四个位置的一直隐藏测试"
        cls.ddedockobject = utils.getDdeDockObject()
        cls.defaultdisplaymode = utils.getDdeDockDisplayMode()
        cls.defaultposition = utils.getDdeDockPosition()
        cls.defaulthidemode = utils.getDdeDockHideMode()
        cls.dock_mainwindow = "dock-mainwindow"
        cls.filemanager = "文件"
        cls.filemanager_windowname = "主文件夹"

        if utils.dock.displaymode_fashion != cls.defaultdisplaymode:
            utils.setDdeDockDisplayMode(utils.dock.displaymode_fashion)

        if utils.dock.position_bottom != cls.defaultposition:
            utils.setDdeDockPosition(utils.dock.position_bottom)

    @classmethod
    def tearDownClass(cls):
        global result
        utils.commitresult(cls.caseid, result)

        if utils.getDdeDockDisplayMode() != utils.dock.displaymode_fashion:
            utils.setDdeDockDisplayMode(utils.dock.displaymode_fashion)

        if utils.getDdeDockPosition() != utils.dock.position_bottom:
            utils.setDdeDockPosition(utils.dock.position_bottom)

        if utils.getDdeDockHideMode() != utils.dock.hidemode_keepshowing:
            utils.setDdeDockHideMode(utils.dock.hidemode_keepshowing)

        win = utils.findWindow(cls.filemanager_windowname)
        if None != win:
            win.unmaximize()
            win.close(time.time())

    def testOpenFileManager(self):
        launcher = self.ddedockobject.child("Launcher")
        launcher.point()
        filemanager = self.ddedockobject.child(self.filemanager)
        filemanager.click()
        rawinput.absoluteMotion(int(utils.resolution.width/2), int(utils.resolution.height/2))

        if utils.dock.hidemode_keephidden != self.defaulthidemode:
            utils.setDdeDockHideMode(utils.dock.hidemode_keephidden)

        hidemode = utils.getDdeDockHideMode()
        hidestate = utils.getDdeDockHideState()
        self.assertTrue(hidemode == utils.dock.hidemode_keephidden)
        self.assertTrue(hidestate == utils.dock.hidestate_hide)
        win = utils.findWindow(self.filemanager_windowname)
        self.assertTrue(win != None)

    def testMaximizeFileManager(self):
        filemanager = self.ddedockobject.child(self.filemanager)
        win = utils.findWindow(self.filemanager_windowname)
        win.maximize()
        self.assertTrue(win != None)

    def testMinimizeFileManager(self):
        filemanager = self.ddedockobject.child(self.filemanager)
        win = utils.findWindow(self.filemanager_windowname)
        win.minimize()
        time.sleep(1)
        self.assertTrue(win != None)
        win_test = utils.findWindow(self.filemanager_windowname)
        self.assertTrue(win_test.is_minimized())

    def testActivateFileManager(self):
        filemanager = self.ddedockobject.child(self.filemanager)
        win = utils.findWindow(self.filemanager_windowname)
        win.activate(time.time())
        self.assertTrue(win != None)
        self.assertTrue(win.is_maximized())

    def testCheckDockSize(self):
        main_window = self.ddedockobject.child(self.dock_mainwindow)
        (width, height) = main_window.size
        position = utils.getDdeDockPosition()
        if position == utils.dock.position_top:
            self.assertTrue(height == 1, " the size is : %s" % str(main_window.size))
        elif position == utils.dock.position_right or position == utils.dock.position_left:
            self.assertTrue(width == 1, " the size is : %s" % str(main_window.size))

    def testExChangeDisplayMode(self):
        if utils.getDdeDockDisplayMode() == utils.dock.displaymode_fashion:
            utils.setDdeDockDisplayMode(utils.dock.displaymode_efficient)
        elif utils.getDdeDockDisplayMode() == utils.dock.displaymode_efficient:
            utils.setDdeDockDisplayMode(utils.dock.displaymode_fashion)

    def testMoveMouseToDock(self):
        position = utils.getDdeDockPosition()
        if utils.dock.position_top == position:
            rawinput.absoluteMotion(int(utils.resolution.width/2), 0)
        elif utils.dock.position_right == position:
            rawinput.absoluteMotion(utils.resolution.width, int(utils.resolution.height/2))
        elif utils.dock.position_left == position:
            rawinput.absoluteMotion(0, int(utils.resolution.height/2))

        time.sleep(3)
        main_window = self.ddedockobject.child(self.dock_mainwindow)
        (width, height) = main_window.size
        self.assertTrue(height > 1, " the size is : %s" % str(main_window.size))
        self.assertTrue(width > 1, " the size is : %s" % str(main_window.size))

    def testChangePosition(self):
        if utils.getDdeDockPosition() == utils.dock.position_bottom:
            utils.setDdeDockPosition(utils.dock.position_top)
        elif utils.getDdeDockPosition() == utils.dock.position_top:
            utils.setDdeDockPosition(utils.dock.position_right)
        elif utils.getDdeDockPosition() == utils.dock.position_right:
            utils.setDdeDockPosition(utils.dock.position_left)

    def suite():
        suite = unittest.TestSuite()
        suite.addTest(DockKeepHiddenOtherDirection('testChangePosition'))

        # top
        suite.addTest(DockKeepHiddenOtherDirection('testOpenFileManager'))
        suite.addTest(DockKeepHiddenOtherDirection('testMaximizeFileManager'))
        suite.addTest(DockKeepHiddenOtherDirection('testCheckDockSize'))
        suite.addTest(DockKeepHiddenOtherDirection('testMinimizeFileManager'))
        suite.addTest(DockKeepHiddenOtherDirection('testCheckDockSize'))
        suite.addTest(DockKeepHiddenOtherDirection('testExChangeDisplayMode'))
        suite.addTest(DockKeepHiddenOtherDirection('testActivateFileManager'))
        suite.addTest(DockKeepHiddenOtherDirection('testCheckDockSize'))
        suite.addTest(DockKeepHiddenOtherDirection('testMinimizeFileManager'))
        suite.addTest(DockKeepHiddenOtherDirection('testCheckDockSize'))
        suite.addTest(DockKeepHiddenOtherDirection('testMoveMouseToDock'))

        # right
        suite.addTest(DockKeepHiddenOtherDirection('testChangePosition'))
        suite.addTest(DockKeepHiddenOtherDirection('testMaximizeFileManager'))
        suite.addTest(DockKeepHiddenOtherDirection('testCheckDockSize'))
        suite.addTest(DockKeepHiddenOtherDirection('testMinimizeFileManager'))
        suite.addTest(DockKeepHiddenOtherDirection('testCheckDockSize'))
        suite.addTest(DockKeepHiddenOtherDirection('testExChangeDisplayMode'))
        suite.addTest(DockKeepHiddenOtherDirection('testActivateFileManager'))
        suite.addTest(DockKeepHiddenOtherDirection('testCheckDockSize'))
        suite.addTest(DockKeepHiddenOtherDirection('testMinimizeFileManager'))
        suite.addTest(DockKeepHiddenOtherDirection('testCheckDockSize'))
        suite.addTest(DockKeepHiddenOtherDirection('testMoveMouseToDock'))

        # left
        suite.addTest(DockKeepHiddenOtherDirection('testChangePosition'))
        suite.addTest(DockKeepHiddenOtherDirection('testMaximizeFileManager'))
        suite.addTest(DockKeepHiddenOtherDirection('testCheckDockSize'))
        suite.addTest(DockKeepHiddenOtherDirection('testMinimizeFileManager'))
        suite.addTest(DockKeepHiddenOtherDirection('testCheckDockSize'))
        suite.addTest(DockKeepHiddenOtherDirection('testExChangeDisplayMode'))
        suite.addTest(DockKeepHiddenOtherDirection('testActivateFileManager'))
        suite.addTest(DockKeepHiddenOtherDirection('testCheckDockSize'))
        suite.addTest(DockKeepHiddenOtherDirection('testMinimizeFileManager'))
        suite.addTest(DockKeepHiddenOtherDirection('testCheckDockSize'))
        suite.addTest(DockKeepHiddenOtherDirection('testMoveMouseToDock'))

        return suite

    class MyTestResult(runner.MyTextTestResult):
        def addError(self, test, err):
            super(DockKeepHiddenOtherDirection.MyTestResult, self).addError(test, err)
            global result
            result = result and False

        def addFailure(self, test, err):
            super(DockKeepHiddenOtherDirection.MyTestResult, self).addFailure(test, err)
            global result
            result = result and False

if __name__ == "__main__":
    unittest.TextTestRunner(resultclass=DockKeepHiddenOtherDirection.MyTestResult).run(DockKeepHiddenOtherDirection.suite())
