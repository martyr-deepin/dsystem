#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
import time
from lib import executeTestCase
from lib import utils
from lib import runner
from dogtail import rawinput

casename = "all-437:一直隐藏"

class DockKeepHidden(unittest.TestCase):
    caseid = '33414'
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

        filemanager = cls.ddedockobject.child(cls.filemanager)
        win = utils.findWindow(cls.filemanager_windowname)
        if None != win:
            win.unmaximize()
            win.close(time.time())

    def testOpenFileManager(self):
        launcher = self.ddedockobject.child("Launcher")
        launcher.point()
        filemanager = self.ddedockobject.child(self.filemanager)
        filemanager.click()
        if utils.dock.hidemode_keephidden != self.defaulthidemode:
            utils.setDdeDockHideMode(utils.dock.hidemode_keephidden)

        rawinput.absoluteMotion(int(utils.resolution.width/2), int(utils.resolution.height/2))
        time.sleep(3)

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
        self.assertTrue(height == 1, " the size is : %s" % str(main_window.size))

    def testExChangeDisplayMode(self):
        if utils.getDdeDockDisplayMode() == utils.dock.displaymode_fashion:
            utils.setDdeDockDisplayMode(utils.dock.displaymode_efficient)
        elif utils.getDdeDockDisplayMode() == utils.dock.displaymode_efficient:
            utils.setDdeDockDisplayMode(utils.dock.displaymode_fashion)

    def testMoveMouseToDock(self):
        rawinput.absoluteMotion(int(utils.resolution.width/2), utils.resolution.height)
        time.sleep(3)
        main_window = self.ddedockobject.child(self.dock_mainwindow)
        (width, height) = main_window.size
        self.assertTrue(height > 1, " the size is : %s" % str(main_window.size))

    def suite():
        suite = unittest.TestSuite()
        suite.addTest(DockKeepHidden('testOpenFileManager'))
        suite.addTest(DockKeepHidden('testMaximizeFileManager'))
        suite.addTest(DockKeepHidden('testCheckDockSize'))
        suite.addTest(DockKeepHidden('testMinimizeFileManager'))
        suite.addTest(DockKeepHidden('testCheckDockSize'))
        suite.addTest(DockKeepHidden('testExChangeDisplayMode'))
        suite.addTest(DockKeepHidden('testActivateFileManager'))
        suite.addTest(DockKeepHidden('testCheckDockSize'))
        suite.addTest(DockKeepHidden('testMinimizeFileManager'))
        suite.addTest(DockKeepHidden('testCheckDockSize'))
        suite.addTest(DockKeepHidden('testMoveMouseToDock'))
        return suite

if __name__ == "__main__":
    executeTestCase.runTest(DockKeepHidden)
