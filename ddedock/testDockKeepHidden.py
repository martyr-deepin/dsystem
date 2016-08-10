#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
import time
from lib import utils
from lib import runner
from dogtail import rawinput

result = True

class MyTestResult(runner.MyTextTestResult):
    def addError(self, test, err):
        super(MyTestResult, self).addError(test, err)
        global result
        result = result and False

    def addFailure(self, test, err):
        super(MyTestResult, self).addFailure(test, err)
        global result
        result = result and False

class DockKeepShown(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.caseid = '33414'
        cls.casename = "all-437:一直隐藏"
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

        if utils.getDdeDockDisplayMode() != cls.defaultdisplaymode:
            utils.setDdeDockDisplayMode(cls.defaultdisplaymode)

        if utils.getDdeDockPosition() != cls.defaultposition:
            utils.setDdeDockPosition(cls.defaultposition)

        if utils.getDdeDockHideMode() != cls.defaulthidemode:
            utils.setDdeDockHideMode(cls.defaulthidemode)

        google = cls.ddedockobject.child(cls.filemanager)
        win = utils.findWindow(cls.filemanager_windowname)
        if None != win:
            win.close(time.time())

    def testOpenFileManager(self):
        google = self.ddedockobject.child(self.filemanager)
        google.click()
        rawinput.click(int(utils.resolution.width/2), int(utils.resolution.height/2))

        if utils.dock.hidemode_keephidden != self.defaulthidemode:
            utils.setDdeDockHideMode(utils.dock.hidemode_keephidden)

        hidemode = utils.getDdeDockHideMode()
        hidestate = utils.getDdeDockHideState()
        self.assertTrue(hidemode == utils.dock.hidemode_keephidden)
        self.assertTrue(hidestate == utils.dock.hidestate_hide)
        win = utils.findWindow(self.filemanager_windowname)
        self.assertTrue(win != None)

    def testMaximizeFileManager(self):
        google = self.ddedockobject.child(self.filemanager)
        win = utils.findWindow(self.filemanager_windowname)
        win.maximize()
        self.assertTrue(win != None)
        self.assertTrue(win.is_maximized())

    def testMinimizeFileManager(self):
        google = self.ddedockobject.child(self.filemanager)
        win = utils.findWindow(self.filemanager_windowname)
        win.minimize()
        time.sleep(1)   
        self.assertTrue(win != None)
        win_test = utils.findWindow(self.filemanager_windowname)  
        self.assertTrue(win_test.is_minimized())

    def testActivateFileManager(self):
        google = self.ddedockobject.child(self.filemanager)
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
    suite.addTest(DockKeepShown('testOpenFileManager'))
    suite.addTest(DockKeepShown('testMaximizeFileManager'))
    suite.addTest(DockKeepShown('testCheckDockSize'))
    suite.addTest(DockKeepShown('testMinimizeFileManager'))
    suite.addTest(DockKeepShown('testCheckDockSize'))
    suite.addTest(DockKeepShown('testExChangeDisplayMode'))
    suite.addTest(DockKeepShown('testActivateFileManager'))
    suite.addTest(DockKeepShown('testCheckDockSize'))
    suite.addTest(DockKeepShown('testMinimizeFileManager'))
    suite.addTest(DockKeepShown('testCheckDockSize'))
    suite.addTest(DockKeepShown('testMoveMouseToDock'))
    return suite

if __name__ == "__main__":
    unittest.TextTestRunner(resultclass=MyTestResult).run(suite())
