#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from lib import utils
from lib import runner

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

class OtherDirectionDockSize(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.caseid = '68501'
        cls.casename = "all-2496:大图标在四个方向上显示"
        cls.ddedockobject = utils.getDdeDockObject()
        cls.defaultdisplaymode = utils.getDdeDockDisplayMode()
        cls.defaultposition = utils.getDdeDockPosition()
        cls.defaulticonsize = utils.getDdeDockIconSize()

    @classmethod
    def tearDownClass(cls):
        global result
        utils.commitresult(cls.caseid, result)

        if utils.getDdeDockDisplayMode() != cls.defaultdisplaymode:
            utils.setDdeDockDisplayMode(cls.defaultdisplaymode)

        if utils.getDdeDockPosition() != cls.defaultposition:
            utils.setDdeDockPosition(cls.defaultposition)

        if utils.getDdeDockIconSize() != cls.defaulticonsize:
            utils.setDdeDockIconSize(cls.defaulticonsize)

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testIconSize(self):
        launcher = self.ddedockobject.child("Launcher")
        dbus_iconsize = utils.getDdeDockIconSize()
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
        utils.keySingle(utils.k.down_key)
        utils.keySingle(utils.k.down_key)
        utils.keySingle(utils.k.enter_key)
        dbus_iconsize = utils.getDdeDockIconSize()
        self.assertTrue(dbus_iconsize == utils.dock.iconsize_small)

    def testExChangeDisplayMode(self):
        if utils.getDdeDockDisplayMode() == utils.dock.displaymode_fashion:
            utils.setDdeDockDisplayMode(utils.dock.displaymode_efficient)
        elif utils.getDdeDockDisplayMode() == utils.dock.displaymode_efficient:
            utils.setDdeDockDisplayMode(utils.dock.displaymode_fashion)

    def testChangePosition(self):
        if utils.getDdeDockPosition() == utils.dock.position_bottom:
            utils.setDdeDockPosition(utils.dock.position_top)
        elif utils.getDdeDockPosition() == utils.dock.position_top:
            utils.setDdeDockPosition(utils.dock.position_right)
        elif utils.getDdeDockPosition() == utils.dock.position_right:
            utils.setDdeDockPosition(utils.dock.position_left)

    def testCheckDockSizeTop(self):
        launcher = self.ddedockobject.child("Launcher")
        main_window = self.ddedockobject.child("dock-mainwindow")
        dbus_iconsize = utils.getDdeDockIconSize()
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
        self.assertTrue(dbus_iconsize == utils.dock.iconsize_small)
        self.assertTrue(main_window.position[1] == 0)

    def testCheckDockSizeRight(self):
        launcher = self.ddedockobject.child("Launcher")
        main_window = self.ddedockobject.child("dock-mainwindow")
        dbus_iconsize = utils.getDdeDockIconSize()
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
        self.assertTrue(dbus_iconsize == utils.dock.iconsize_small)
        self.assertTrue(main_window.position[0] == (utils.resolution.width - main_window.size[0]))

    def testCheckDockSizeLeft(self):
        launcher = self.ddedockobject.child("Launcher")
        main_window = self.ddedockobject.child("dock-mainwindow")
        dbus_iconsize = utils.getDdeDockIconSize()
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
        self.assertTrue(dbus_iconsize == utils.dock.iconsize_small)
        self.assertTrue(main_window.position[0] == 0)

def suite():
    suite = unittest.TestSuite()
    suite.addTest(OtherDirectionDockSize('testIconSize'))
    suite.addTest(OtherDirectionDockSize('testChangeIconSizeToLarge'))
    suite.addTest(OtherDirectionDockSize('testChangePosition'))
    suite.addTest(OtherDirectionDockSize('testCheckDockSizeTop'))
    suite.addTest(OtherDirectionDockSize('testExChangeDisplayMode'))
    suite.addTest(OtherDirectionDockSize('testCheckDockSizeTop'))
    suite.addTest(OtherDirectionDockSize('testChangePosition'))
    suite.addTest(OtherDirectionDockSize('testCheckDockSizeRight'))
    suite.addTest(OtherDirectionDockSize('testExChangeDisplayMode'))
    suite.addTest(OtherDirectionDockSize('testCheckDockSizeRight'))
    suite.addTest(OtherDirectionDockSize('testChangePosition'))
    suite.addTest(OtherDirectionDockSize('testCheckDockSizeLeft'))
    suite.addTest(OtherDirectionDockSize('testExChangeDisplayMode'))
    suite.addTest(OtherDirectionDockSize('testCheckDockSizeLeft'))
    return suite

if __name__ == "__main__":
    unittest.TextTestRunner(resultclass=MyTestResult).run(suite())
