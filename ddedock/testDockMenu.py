#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from lib import executeTestCase
from lib import utils
from lib import runner
from dogtail import rawinput
from dogtail.tree import *

result = True
caseid = '68161'
casename = "all-2473:方向设置菜单"

class DockMenu(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.ddedockobject = utils.getDdeDockObject()
        cls.defaultdisplaymode = utils.getDdeDockDisplayMode()
        cls.defaultposition = utils.getDdeDockPosition()
        cls.defaulthidemode = utils.getDdeDockHideMode()
        cls.dockmenuname = "DesktopMenu"

        if utils.dock.displaymode_fashion != cls.defaultdisplaymode:
            utils.setDdeDockDisplayMode(utils.dock.displaymode_fashion)

        if utils.dock.position_bottom != cls.defaultposition:
            utils.setDdeDockPosition(utils.dock.position_bottom)

        if utils.dock.hidemode_keepshowing != cls.defaulthidemode:
            utils.setDdeDockHideMode(utils.dock.hidemode_keepshowing)


    @classmethod
    def tearDownClass(cls):
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
            self.testClickScreenCenter()
            self.assertTrue(False, "Can not find the dock menu")

    def testRightClickOnDock(self, x, y):
        rawinput.click(x, y, 3)

    def testChangePosition(self):
        if utils.getDdeDockPosition() == utils.dock.position_bottom:
            utils.setDdeDockPosition(utils.dock.position_top)
        elif utils.getDdeDockPosition() == utils.dock.position_top:
            utils.setDdeDockPosition(utils.dock.position_right)
        elif utils.getDdeDockPosition() == utils.dock.position_right:
            utils.setDdeDockPosition(utils.dock.position_left)
        elif utils.getDdeDockPosition() == utils.dock.position_left:
            utils.setDdeDockPosition(utils.dock.position_bottom)

    def testExChangeDisplayMode(self):
        if utils.getDdeDockDisplayMode() == utils.dock.displaymode_fashion:
            utils.setDdeDockDisplayMode(utils.dock.displaymode_efficient)
        elif utils.getDdeDockDisplayMode() == utils.dock.displaymode_efficient:
            utils.setDdeDockDisplayMode(utils.dock.displaymode_fashion)

    def testProcess(self):
        try:
            dock = self.ddedockobject.child(utils.dock.mainwindowname)
        except:
            self.testClickScreenCenter()
            self.assertTrue(False, "Can't find the dock mainwindowname.")

        (xp, yp) = dock.position
        (width, height) = dock.size
        xylist = [(xp, yp),
                  (int(xp + width/2), yp),
                  (xp + width -1, yp),
                  (xp, int(yp + height/2)),
                  (xp + width -1, int(yp + height/2)),
                  (xp, yp + height - 1),
                  (int(xp + width/2), yp + height - 1),
                  (xp + width -1, yp + height - 1)]

        for xy in xylist:
            self.testRightClickOnDock(xy[0], xy[1])
            self.testDockMenuExist()
            self.testClickScreenCenter()

    def suite():
        suite = unittest.TestSuite()

        # fashtion
        suite.addTest(DockMenu('testProcess'))
        suite.addTest(DockMenu('testChangePosition'))
        suite.addTest(DockMenu('testProcess'))
        suite.addTest(DockMenu('testChangePosition'))
        suite.addTest(DockMenu('testProcess'))
        suite.addTest(DockMenu('testChangePosition'))
        suite.addTest(DockMenu('testProcess'))

        # change mode and direction
        suite.addTest(DockMenu('testExChangeDisplayMode'))
        suite.addTest(DockMenu('testChangePosition'))

        # efficient
        suite.addTest(DockMenu('testProcess'))
        suite.addTest(DockMenu('testChangePosition'))
        suite.addTest(DockMenu('testProcess'))
        suite.addTest(DockMenu('testChangePosition'))
        suite.addTest(DockMenu('testProcess'))
        suite.addTest(DockMenu('testChangePosition'))
        suite.addTest(DockMenu('testProcess'))

        return suite

if __name__ == "__main__":
    runTest(DockMenu.suite())
