#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from lib import utils
from lib import runner

result = True

class DockSizeSmallOtherDirection(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.caseid = '68511'
        cls.casename = "all-2498:小图标在四个方向上显示"
        cls.ddedockobject = utils.getDdeDockObject()

        if utils.getDdeDockDisplayMode() != utils.dock.displaymode_efficient:
            utils.setDdeDockDisplayMode(utils.dock.displaymode_efficient)

        if utils.getDdeDockPosition() != utils.dock.position_bottom:
            utils.setDdeDockPosition(utils.dock.position_bottom)

        if utils.getDdeDockIconSize() != utils.dock.iconsize_medium:
            utils.setDdeDockIconSize(utils.dock.iconsize_medium)

    @classmethod
    def tearDownClass(cls):
        global result
        utils.commitresult(cls.caseid, result)

        if utils.getDdeDockDisplayMode() != utils.dock.displaymode_fashion:
            utils.setDdeDockDisplayMode(utils.dock.displaymode_fashion)

        if utils.getDdeDockPosition() != utils.dock.position_bottom:
            utils.setDdeDockPosition(utils.dock.position_bottom)

        if utils.getDdeDockIconSize() != utils.dock.iconsize_medium:
            utils.setDdeDockIconSize(utils.dock.iconsize_medium)

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testIconSizeSmall(self):
        launcher = self.ddedockobject.child("Launcher")
        dbus_iconsize = utils.getDdeDockIconSize()
        self.assertTrue(dbus_iconsize == utils.dock.iconsize_small)
        displaymode = utils.getDdeDockDisplayMode()
        calculate_iconsize_y = 0
        calculate_iconsize_x = 0
        if utils.dock.displaymode_fashion == displaymode:
            calculate_iconsize_y = int(dbus_iconsize * 1.5)
            calculate_iconsize_x = int(calculate_iconsize_y * 1.1)
        elif utils.dock.displaymode_efficient == displaymode:
            calculate_iconsize_y = int(dbus_iconsize * 1.2)
            calculate_iconsize_x = int(calculate_iconsize_y * 1.4)

        self.assertEquals((calculate_iconsize_x, calculate_iconsize_y),
                          launcher.size)

    def testIconSizeLarge(self):
        launcher = self.ddedockobject.child("Launcher")
        dbus_iconsize = utils.getDdeDockIconSize()
        self.assertTrue(dbus_iconsize == utils.dock.iconsize_large)
        displaymode = utils.getDdeDockDisplayMode()
        calculate_iconsize_y = 0
        calculate_iconsize_x = 0
        if utils.dock.displaymode_fashion == displaymode:
            calculate_iconsize_y = int(dbus_iconsize * 1.5)
            calculate_iconsize_x = int(calculate_iconsize_y * 1.1)
        elif utils.dock.displaymode_efficient == displaymode:
            calculate_iconsize_y = int(dbus_iconsize * 1.2)
            calculate_iconsize_x = int(calculate_iconsize_y * 1.4)

        if utils.getDdeDockPosition() == utils.dock.position_top or \
           utils.getDdeDockPosition() == utils.dock.position_bottom:
            self.assertEquals((calculate_iconsize_x, calculate_iconsize_y),
                          launcher.size)
        elif utils.getDdeDockPosition() == utils.dock.position_right or \
           utils.getDdeDockPosition() == utils.dock.position_left:
            self.assertTrue(calculate_iconsize_x == launcher.size[0])
            self.assertTrue(calculate_iconsize_y > 1 and calculate_iconsize_y >= launcher.size[1])


    def testChangeIconSizeToLarge(self):
        utils.m.click(int(utils.resolution.width/2), utils.resolution.height, 2)
        utils.dockmenu.findMainWindow()
        utils.keySingle(utils.k.down_key)
        utils.keySingle(utils.k.left_key)
        utils.keySingle(utils.k.down_key)
        utils.keySingle(utils.k.left_key)
        utils.keySingle(utils.k.down_key)
        utils.keySingle(utils.k.enter_key)
        dbus_iconsize = utils.getDdeDockIconSize()
        self.assertTrue(dbus_iconsize == utils.dock.iconsize_large)

    def testChangeIconSizeToMedium(self):
        utils.m.click(int(utils.resolution.width/2), utils.resolution.height, 2)
        utils.dockmenu.findMainWindow()
        utils.keySingle(utils.k.down_key)
        utils.keySingle(utils.k.left_key)
        utils.keySingle(utils.k.down_key)
        utils.keySingle(utils.k.left_key)
        utils.keySingle(utils.k.down_key)
        utils.keySingle(utils.k.down_key)
        utils.keySingle(utils.k.enter_key)
        dbus_iconsize = utils.getDdeDockIconSize()
        self.assertTrue(dbus_iconsize == utils.dock.iconsize_medium)

    def testChangeIconSizeToSmall(self):
        utils.m.click(int(utils.resolution.width/2), utils.resolution.height, 2)
        utils.dockmenu.findMainWindow()
        utils.keySingle(utils.k.down_key)
        utils.keySingle(utils.k.left_key)
        utils.keySingle(utils.k.down_key)
        utils.keySingle(utils.k.left_key)
        utils.keySingle(utils.k.down_key)
        utils.keySingle(utils.k.down_key)
        utils.keySingle(utils.k.down_key)
        utils.keySingle(utils.k.enter_key)
        dbus_iconsize = utils.getDdeDockIconSize()
        self.assertTrue(dbus_iconsize == utils.dock.iconsize_small)

    def testChangePosition(self):
        if utils.getDdeDockPosition() == utils.dock.position_bottom:
            utils.setDdeDockPosition(utils.dock.position_top)
        elif utils.getDdeDockPosition() == utils.dock.position_top:
            utils.setDdeDockPosition(utils.dock.position_right)
        elif utils.getDdeDockPosition() == utils.dock.position_right:
            utils.setDdeDockPosition(utils.dock.position_left)

    def testExChangeDisplayMode(self):
        if utils.getDdeDockDisplayMode() == utils.dock.displaymode_fashion:
            utils.setDdeDockDisplayMode(utils.dock.displaymode_efficient)
        elif utils.getDdeDockDisplayMode() == utils.dock.displaymode_efficient:
            utils.setDdeDockDisplayMode(utils.dock.displaymode_fashion)

    def suite():
        suite = unittest.TestSuite()
        suite.addTest(DockSizeSmallOtherDirection('testChangeIconSizeToSmall'))
        suite.addTest(DockSizeSmallOtherDirection('testIconSizeSmall'))

        # top
        suite.addTest(DockSizeSmallOtherDirection('testChangePosition'))
        suite.addTest(DockSizeSmallOtherDirection('testIconSizeSmall'))
        suite.addTest(DockSizeSmallOtherDirection('testExChangeDisplayMode'))
        suite.addTest(DockSizeSmallOtherDirection('testIconSizeSmall'))

        # right
        suite.addTest(DockSizeSmallOtherDirection('testChangePosition'))
        suite.addTest(DockSizeSmallOtherDirection('testIconSizeSmall'))
        suite.addTest(DockSizeSmallOtherDirection('testExChangeDisplayMode'))
        suite.addTest(DockSizeSmallOtherDirection('testIconSizeSmall'))

        # left
        suite.addTest(DockSizeSmallOtherDirection('testChangePosition'))
        suite.addTest(DockSizeSmallOtherDirection('testIconSizeSmall'))
        suite.addTest(DockSizeSmallOtherDirection('testExChangeDisplayMode'))
        suite.addTest(DockSizeSmallOtherDirection('testIconSizeSmall'))
        return suite

    class MyTestResult(runner.MyTextTestResult):
        def addError(self, test, err):
            super(DockSizeSmallOtherDirection.MyTestResult, self).addError(test, err)
            global result
            result = result and False

        def addFailure(self, test, err):
            super(DockSizeSmallOtherDirection.MyTestResult, self).addFailure(test, err)
            global result
            result = result and False

if __name__ == "__main__":
    unittest.TextTestRunner(resultclass=DockSizeSmallOtherDirection.MyTestResult).run(DockSizeSmallOtherDirection.suite())
