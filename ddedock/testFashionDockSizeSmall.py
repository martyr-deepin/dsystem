#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from lib import executeTestCase
from lib import utils
from lib import runner

result = True
casename = "all-2491:时尚模式小图标显示"

class FashionDockSizeSmall(unittest.TestCase):
    caseid = '68483'
    @classmethod
    def setUpClass(cls):
        cls.ddedockobject = utils.getDdeDockObject()

        if utils.getDdeDockDisplayMode() != utils.dock.displaymode_fashion:
            utils.setDdeDockDisplayMode(utils.dock.displaymode_fashion)

        if utils.getDdeDockPosition() != utils.dock.position_bottom:
            utils.setDdeDockPosition(utils.dock.position_bottom)

        if utils.getDdeDockIconSize() != utils.dock.iconsize_medium:
            utils.setDdeDockIconSize(utils.dock.iconsize_medium)

    @classmethod
    def tearDownClass(cls):
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

    def suite():
        suite = unittest.TestSuite()
        suite.addTest(FashionDockSizeSmall('testIconSizeMedium'))
        suite.addTest(FashionDockSizeSmall('testChangeIconSizeToSmall'))
        suite.addTest(FashionDockSizeSmall('testIconSizeSmall'))
        return suite

if __name__ == "__main__":
    executeTestCase.runTest(FashionDockSizeSmall)