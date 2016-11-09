#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
import time
from lib import utils
from lib import runner
from dogtail import rawinput
from dogtail.tree import *

result = True
caseid = '68464'
casename = "all-2485:高效模式上方显示测试"

class DockEfficientMode(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.startTime = time.time()
        cls.caseid_2 = '68467'
        cls.casename_2 = "all-2486:高效模式下方显示测试"
        cls.caseid_3 = '68470'
        cls.casename_3 = "all-2487:高效模式左方显示测试"
        cls.caseid_4 = '68473'
        cls.casename_4 = "all-2484:高效模式右方显示测试"
        cls.ddedockobject = utils.getDdeDockObject()
        cls.defaultdisplaymode = utils.getDdeDockDisplayMode()
        cls.defaultposition = utils.getDdeDockPosition()
        cls.defaulthidemode = utils.getDdeDockHideMode()
        cls.dockmenuname = "DesktopMenu"

        if utils.dock.displaymode_efficient != cls.defaultdisplaymode:
            utils.setDdeDockDisplayMode(utils.dock.displaymode_efficient)

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
        utils.commitresult(cls.caseid_2, result)
        utils.commitresult(cls.caseid_3, result)
        utils.commitresult(cls.caseid_4, result)

        if utils.getDdeDockDisplayMode() != utils.dock.displaymode_fashion:
            utils.setDdeDockDisplayMode(utils.dock.displaymode_fashion)

        if utils.getDdeDockPosition() != utils.dock.position_bottom:
            utils.setDdeDockPosition(utils.dock.position_bottom)

        if utils.getDdeDockHideMode() != utils.dock.hidemode_keepshowing:
            utils.setDdeDockHideMode(utils.dock.hidemode_keepshowing)

    def testClickScreenCenter(self):
        rawinput.click(int(utils.resolution.width/2), int(utils.resolution.height/2))
        time.sleep(1)

    def testDockMenuExist(self):
        try:
            dockmenuapp = root.application('deepin-menu', '/usr/lib/deepin-menu')
            dockmenu = dockmenuapp.child(self.dockmenuname)
        except:
            self.assertTrue(False, "Can not find the dock menu")

    def testRightClickOnDock(self, x, y):
        rawinput.click(x, y, 3)

    def testChangePositionTop(self):
        try:
            dock = self.ddedockobject.child(utils.dock.mainwindowname)
        except:
            self.assertTrue(False, "Can't find the dock mainwindowname.")

        (xp, yp) = dock.position
        (width, height) = dock.size
        xy = (int(xp + width/2), yp + height)

        self.testRightClickOnDock(xy[0], xy[1])

        self.testDockMenuExist()

        utils.keySingle(utils.k.down_key)
        utils.keySingle(utils.k.left_key)
        utils.keySingle(utils.k.down_key)
        utils.keySingle(utils.k.enter_key)

        try:
            dock = self.ddedockobject.child(utils.dock.mainwindowname)
        except:
            self.assertTrue(False, "Can't find the dock mainwindowname.")

        (xp, yp) = dock.position
        (width, height) = dock.size

        self.assertTrue(width > 1)
        self.assertTrue(height > 1)
        self.assertTrue(0 == yp)

    def testChangePositionRight(self):
        try:
            dock = self.ddedockobject.child(utils.dock.mainwindowname)
        except:
            self.assertTrue(False, "Can't find the dock mainwindowname.")

        (xp, yp) = dock.position
        (width, height) = dock.size
        xy = (int(xp + width/2), yp)

        self.testRightClickOnDock(xy[0], xy[1])

        self.testDockMenuExist()

        utils.keySingle(utils.k.down_key)
        utils.keySingle(utils.k.left_key)
        utils.keySingle(utils.k.down_key)
        utils.keySingle(utils.k.down_key)
        utils.keySingle(utils.k.down_key)
        utils.keySingle(utils.k.down_key)
        utils.keySingle(utils.k.enter_key)

        try:
            dock = self.ddedockobject.child(utils.dock.mainwindowname)
        except:
            self.assertTrue(False, "Can't find the dock mainwindowname.")

        (xp, yp) = dock.position
        (width, height) = dock.size

        self.assertTrue(width > 1)
        self.assertTrue(height > 1)
        self.assertTrue(width == utils.resolution.width - xp)

    def testChangePositionLeft(self):
        try:
            dock = self.ddedockobject.child(utils.dock.mainwindowname)
        except:
            self.assertTrue(False, "Can't find the dock mainwindowname.")

        (xp, yp) = dock.position
        (width, height) = dock.size
        xy = (xp, int(yp + height/2))

        self.testRightClickOnDock(xy[0], xy[1])

        self.testDockMenuExist()

        utils.keySingle(utils.k.down_key)
        utils.keySingle(utils.k.left_key)
        utils.keySingle(utils.k.down_key)
        utils.keySingle(utils.k.down_key)
        utils.keySingle(utils.k.down_key)
        utils.keySingle(utils.k.enter_key)

        try:
            dock = self.ddedockobject.child(utils.dock.mainwindowname)
        except:
            self.assertTrue(False, "Can't find the dock mainwindowname.")

        (xp, yp) = dock.position
        (width, height) = dock.size

        self.assertTrue(width > 1)
        self.assertTrue(height > 1)
        self.assertTrue(0 == xp)

    def testChangePositionBottom(self):
        try:
            dock = self.ddedockobject.child(utils.dock.mainwindowname)
        except:
            self.assertTrue(False, "Can't find the dock mainwindowname.")

        (xp, yp) = dock.position
        (width, height) = dock.size
        xy = (xp, int(yp + height/2))

        self.testRightClickOnDock(xy[0], xy[1])

        self.testDockMenuExist()

        utils.keySingle(utils.k.down_key)
        utils.keySingle(utils.k.left_key)
        utils.keySingle(utils.k.down_key)
        utils.keySingle(utils.k.down_key)
        utils.keySingle(utils.k.enter_key)

        try:
            dock = self.ddedockobject.child(utils.dock.mainwindowname)
        except:
            self.assertTrue(False, "Can't find the dock mainwindowname.")

        (xp, yp) = dock.position
        (width, height) = dock.size

        self.assertTrue(width > 1)
        self.assertTrue(height > 1)
        self.assertTrue(yp == utils.resolution.height - height)

    def testChangePosition(self):
        if utils.getDdeDockPosition() == utils.dock.position_bottom:
            self.testChangePositionTop()
        elif utils.getDdeDockPosition() == utils.dock.position_top:
            self.testChangePositionRight()
        elif utils.getDdeDockPosition() == utils.dock.position_right:
            self.testChangePositionLeft()
        elif utils.getDdeDockPosition() == utils.dock.position_left:
            self.testChangePositionBottom()

    def suite():
        suite = unittest.TestSuite()

        # Efficient
        suite.addTest(DockEfficientMode('testChangePositionTop'))
        suite.addTest(DockEfficientMode('testChangePositionRight'))
        suite.addTest(DockEfficientMode('testChangePositionLeft'))
        suite.addTest(DockEfficientMode('testChangePositionBottom'))

        return suite

    class MyTestResult(runner.MyTextTestResult):
        def addError(self, test, err):
            super(DockEfficientMode.MyTestResult, self).addError(test, err)
            global result
            result = result and False

        def addFailure(self, test, err):
            super(DockEfficientMode.MyTestResult, self).addFailure(test, err)
            global result
            result = result and False

if __name__ == "__main__":
    unittest.TextTestRunner(resultclass=DockEfficientMode.MyTestResult).run(DockEfficientMode.suite())
