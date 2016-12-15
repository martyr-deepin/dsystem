#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from lib import executeTestCase
from lib import utils
from lib import runner
from dogtail import rawinput

result = True
caseid = '33421'
casename = "all-438:智能隐藏"

class DockSmartHide(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
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
        ddedock = self.ddedockobject.child(self.dock_mainwindow)
        (width, height) = ddedock.size
        if utils.dock.hidemode_smarthide != self.defaulthidemode:
            utils.setDdeDockHideMode(utils.dock.hidemode_smarthide)

        rawinput.absoluteMotion(int(utils.resolution.width/2), int(utils.resolution.height/2))
        time.sleep(3)

        hidemode = utils.getDdeDockHideMode()
        hidestate = utils.getDdeDockHideState()
        self.assertTrue(hidemode == utils.dock.hidemode_smarthide)
        time.sleep(2)
        win = utils.findWindow(self.filemanager_windowname)
        utils.resizeWindow(win, height + 1, height + 1, utils.resolution.width - 2*height -20, utils.resolution.height - 2*height -20)
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
        self.assertTrue(height > 1, " the size is : %s" % str(main_window.size))

    def testCheckDockSizeHideState(self):
        main_window = self.ddedockobject.child(self.dock_mainwindow)
        (width, height) = main_window.size
        self.assertTrue(height == 1, " the size is : %s" % str(main_window.size))

    def testExChangeDisplayMode(self):
        if utils.getDdeDockDisplayMode() == utils.dock.displaymode_fashion:
            utils.setDdeDockDisplayMode(utils.dock.displaymode_efficient)
        elif utils.getDdeDockDisplayMode() == utils.dock.displaymode_efficient:
            utils.setDdeDockDisplayMode(utils.dock.displaymode_fashion)

    def testMoveMouseToDock(self):
        rawinput.absoluteMotion(int(utils.resolution.width/2), utils.resolution.height)
        main_window = self.ddedockobject.child(self.dock_mainwindow)
        (width, height) = main_window.size
        self.assertTrue(height > 1, " the size is : %s" % str(main_window.size))

    def suite():
        suite = unittest.TestSuite()
        suite.addTest(DockSmartHide('testOpenFileManager'))
        suite.addTest(DockSmartHide('testCheckDockSize'))
        suite.addTest(DockSmartHide('testMaximizeFileManager'))
        suite.addTest(DockSmartHide('testCheckDockSizeHideState'))
        suite.addTest(DockSmartHide('testMinimizeFileManager'))
        suite.addTest(DockSmartHide('testCheckDockSize'))
        suite.addTest(DockSmartHide('testExChangeDisplayMode'))
        suite.addTest(DockSmartHide('testActivateFileManager'))
        suite.addTest(DockSmartHide('testCheckDockSizeHideState'))
        suite.addTest(DockSmartHide('testMinimizeFileManager'))
        suite.addTest(DockSmartHide('testCheckDockSize'))
        suite.addTest(DockSmartHide('testMoveMouseToDock'))
        return suite

if __name__ == "__main__":
    runTest(DockSmartHide.suite())
