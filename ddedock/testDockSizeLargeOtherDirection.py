#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from lib import utils
from lib import runner

result = True
caseid = '68501'
casename = "all-2496:大图标在四个方向上显示"

class DockSizeLargeOtherDirection(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.startTime = time.time()
        cls.ddedockobject = utils.getDdeDockObject()

        if utils.getDdeDockDisplayMode() != utils.dock.displaymode_efficient:
            utils.setDdeDockDisplayMode(utils.dock.displaymode_efficient)

        if utils.getDdeDockPosition() != utils.dock.position_bottom:
            utils.setDdeDockPosition(utils.dock.position_bottom)

        if utils.getDdeDockIconSize() != utils.dock.iconsize_medium:
            utils.setDdeDockIconSize(utils.dock.iconsize_medium)

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

        if utils.getDdeDockIconSize() != utils.dock.iconsize_medium:
            utils.setDdeDockIconSize(utils.dock.iconsize_medium)

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testIconSizeMedium(self):
        launcher = self.ddedockobject.child("Launcher")
        dbus_iconsize = utils.getDdeDockIconSize()
        self.assertTrue(dbus_iconsize == utils.dock.iconsize_medium)
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
        suite.addTest(DockSizeLargeOtherDirection('testIconSizeMedium'))
        suite.addTest(DockSizeLargeOtherDirection('testChangeIconSizeToLarge'))
        suite.addTest(DockSizeLargeOtherDirection('testIconSizeLarge'))

        # top
        suite.addTest(DockSizeLargeOtherDirection('testChangePosition'))
        suite.addTest(DockSizeLargeOtherDirection('testIconSizeLarge'))
        suite.addTest(DockSizeLargeOtherDirection('testExChangeDisplayMode'))
        suite.addTest(DockSizeLargeOtherDirection('testIconSizeLarge'))

        # right
        suite.addTest(DockSizeLargeOtherDirection('testChangePosition'))
        suite.addTest(DockSizeLargeOtherDirection('testIconSizeLarge'))
        suite.addTest(DockSizeLargeOtherDirection('testExChangeDisplayMode'))
        suite.addTest(DockSizeLargeOtherDirection('testIconSizeLarge'))

        # left
        suite.addTest(DockSizeLargeOtherDirection('testChangePosition'))
        suite.addTest(DockSizeLargeOtherDirection('testIconSizeLarge'))
        suite.addTest(DockSizeLargeOtherDirection('testExChangeDisplayMode'))
        suite.addTest(DockSizeLargeOtherDirection('testIconSizeLarge'))
        return suite

    class MyTestResult(runner.MyTextTestResult):
        def addError(self, test, err):
            super(DockSizeLargeOtherDirection.MyTestResult, self).addError(test, err)
            global result
            result = result and False

        def addFailure(self, test, err):
            super(DockSizeLargeOtherDirection.MyTestResult, self).addFailure(test, err)
            global result
            result = result and False

if __name__ == "__main__":
    unittest.TextTestRunner(resultclass=DockSizeLargeOtherDirection.MyTestResult).run(DockSizeLargeOtherDirection.suite())
