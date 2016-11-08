#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
import time
from lib import utils
from lib import runner
from dogtail import rawinput

result = True
caseid = '68525'
casename = "all-2501:四个位置的智能隐藏测试"

class DockSmartHideOtherDirection(unittest.TestCase):
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

    @classmethod
    def tearDownClass(cls):
        seconds = %.3f % (time.time() - cls.startTime)
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
        if None != win:
            win.unmaximize()
            win.close(time.time())

    def testOpenFileManager(self):
        launcher = self.ddedockobject.child("Launcher")
        launcher.point()
        managerobj = self.ddedockobject.child(self.filemanager)
        managerobj.click()
        rawinput.absoluteMotion(int(utils.resolution.width/2), int(utils.resolution.height/2))

        if utils.dock.hidemode_smarthide != self.defaulthidemode:
            utils.setDdeDockHideMode(utils.dock.hidemode_smarthide)

        hidemode = utils.getDdeDockHideMode()
        hidestate = utils.getDdeDockHideState()
        self.assertTrue(hidemode == utils.dock.hidemode_smarthide)
        win = utils.findWindow(self.filemanager_windowname)
        self.assertTrue(win != None)

    def testMaximizeFileManager(self):
        win = utils.findWindow(self.filemanager_windowname)
        win.maximize()
        win.activate(time.time())
        rawinput.absoluteMotion(int(utils.resolution.width/2), int(utils.resolution.height/2))
        time.sleep(2)
        self.assertTrue(win != None)

    def testMinimizeFileManager(self):
        win = utils.findWindow(self.filemanager_windowname)
        win.minimize()
        time.sleep(2)
        self.assertTrue(win != None)
        win_test = utils.findWindow(self.filemanager_windowname)
        self.assertTrue(win_test.is_minimized())

    def testActivateFileManager(self):
        managerobj = self.ddedockobject.child(self.filemanager)
        managerobj.click()
        rawinput.absoluteMotion(int(utils.resolution.width/2), int(utils.resolution.height/2))
        time.sleep(3)
        win = utils.findWindow(self.filemanager_windowname)
        self.assertTrue(win != None)
        self.assertTrue(win.is_maximized())

    def testCheckDockSize(self):
        main_window = self.ddedockobject.child(self.dock_mainwindow)
        (width, height) = main_window.size
        position = utils.getDdeDockPosition()
        if position == utils.dock.position_top:
            self.assertTrue(height > 1, " the size is : %s" % str(main_window.size))
        elif position == utils.dock.position_right or position == utils.dock.position_left:
            self.assertTrue(width > 1, " the size is : %s" % str(main_window.size))

    def testCheckDockSizeHideState(self):
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

        time.sleep(1)

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
        # top
        suite.addTest(DockSmartHideOtherDirection('testChangePosition'))
        suite.addTest(DockSmartHideOtherDirection('testOpenFileManager'))
        suite.addTest(DockSmartHideOtherDirection('testCheckDockSize'))
        suite.addTest(DockSmartHideOtherDirection('testMaximizeFileManager'))
        suite.addTest(DockSmartHideOtherDirection('testCheckDockSizeHideState'))
        suite.addTest(DockSmartHideOtherDirection('testMinimizeFileManager'))
        suite.addTest(DockSmartHideOtherDirection('testCheckDockSize'))
        suite.addTest(DockSmartHideOtherDirection('testExChangeDisplayMode'))
        suite.addTest(DockSmartHideOtherDirection('testActivateFileManager'))
        suite.addTest(DockSmartHideOtherDirection('testCheckDockSizeHideState'))
        suite.addTest(DockSmartHideOtherDirection('testMinimizeFileManager'))
        suite.addTest(DockSmartHideOtherDirection('testCheckDockSize'))
        suite.addTest(DockSmartHideOtherDirection('testMoveMouseToDock'))

        # right
        suite.addTest(DockSmartHideOtherDirection('testChangePosition'))
        suite.addTest(DockSmartHideOtherDirection('testOpenFileManager'))
        suite.addTest(DockSmartHideOtherDirection('testCheckDockSizeHideState'))
        suite.addTest(DockSmartHideOtherDirection('testMaximizeFileManager'))
        suite.addTest(DockSmartHideOtherDirection('testCheckDockSizeHideState'))
        suite.addTest(DockSmartHideOtherDirection('testMinimizeFileManager'))
        suite.addTest(DockSmartHideOtherDirection('testCheckDockSize'))
        suite.addTest(DockSmartHideOtherDirection('testExChangeDisplayMode'))
        suite.addTest(DockSmartHideOtherDirection('testActivateFileManager'))
        suite.addTest(DockSmartHideOtherDirection('testCheckDockSizeHideState'))
        suite.addTest(DockSmartHideOtherDirection('testMinimizeFileManager'))
        suite.addTest(DockSmartHideOtherDirection('testCheckDockSize'))
        suite.addTest(DockSmartHideOtherDirection('testMoveMouseToDock'))

        # left
        suite.addTest(DockSmartHideOtherDirection('testChangePosition'))
        suite.addTest(DockSmartHideOtherDirection('testOpenFileManager'))
        suite.addTest(DockSmartHideOtherDirection('testCheckDockSizeHideState'))
        suite.addTest(DockSmartHideOtherDirection('testMaximizeFileManager'))
        suite.addTest(DockSmartHideOtherDirection('testCheckDockSizeHideState'))
        suite.addTest(DockSmartHideOtherDirection('testMinimizeFileManager'))
        suite.addTest(DockSmartHideOtherDirection('testCheckDockSize'))
        suite.addTest(DockSmartHideOtherDirection('testExChangeDisplayMode'))
        suite.addTest(DockSmartHideOtherDirection('testActivateFileManager'))
        suite.addTest(DockSmartHideOtherDirection('testCheckDockSizeHideState'))
        suite.addTest(DockSmartHideOtherDirection('testMinimizeFileManager'))
        suite.addTest(DockSmartHideOtherDirection('testCheckDockSize'))
        suite.addTest(DockSmartHideOtherDirection('testMoveMouseToDock'))
        return suite

    class MyTestResult(runner.MyTextTestResult):
        def addError(self, test, err):
            super(DockSmartHideOtherDirection.MyTestResult, self).addError(test, err)
            global result
            result = result and False

        def addFailure(self, test, err):
            super(DockSmartHideOtherDirection.MyTestResult, self).addFailure(test, err)
            global result
            result = result and False

if __name__ == "__main__":
    unittest.TextTestRunner(resultclass=DockSmartHideOtherDirection.MyTestResult).run(DockSmartHideOtherDirection.suite())
