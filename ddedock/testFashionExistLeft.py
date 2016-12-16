#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from lib import executeTestCase
from lib import utils
from lib import runner

result = True
casename = "all-2483:时尚模式左方显示测试"

class FashionExistLeft(unittest.TestCase):
    caseid = '68458'
    @classmethod
    def setUpClass(cls):
        cls.ddedockobject = utils.getDdeDockObject()
        cls.defaultdisplaymode = utils.getDdeDockDisplayMode()
        cls.defaultposition = utils.getDdeDockPosition()
        cls.dock_mainwindow = "dock-mainwindow"

    @classmethod
    def tearDownClass(cls):
        if utils.getDdeDockDisplayMode() != cls.defaultdisplaymode:
            utils.setDdeDockDisplayMode(cls.defaultdisplaymode)

        if utils.getDdeDockPosition() != cls.defaultposition:
            utils.setDdeDockPosition(cls.defaultposition)

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testBasicFunction(self):
        defaultdisplaymode = utils.getDdeDockDisplayMode()
        self.assertTrue(utils.dock.displaymode_fashion == defaultdisplaymode)
        defaultposition = utils.getDdeDockPosition()
        self.assertTrue(utils.dock.position_bottom == defaultposition)
        defaulthidestate = utils.getDdeDockHideState()
        self.assertTrue(utils.dock.hidestate_show == defaulthidestate)
        main_window = self.ddedockobject.child(self.dock_mainwindow)
        (width, height) = main_window.size
        self.assertTrue(width > 0)
        self.assertTrue(height > 0)

    def testChangePositionToLeft(self):
        utils.m.click(int(utils.resolution.width/2), utils.resolution.height, 2)
        utils.dockmenu.findMainWindow()
        utils.keySingle(utils.k.down_key)
        utils.keySingle(utils.k.left_key)
        utils.keySingle(utils.k.down_key)
        utils.keySingle(utils.k.down_key)
        utils.keySingle(utils.k.down_key)
        utils.keySingle(utils.k.enter_key)
        defaultdisplaymode = utils.getDdeDockDisplayMode()
        self.assertTrue(utils.dock.displaymode_fashion == defaultdisplaymode)
        defaultposition = utils.getDdeDockPosition()
        self.assertTrue(utils.dock.position_left == defaultposition)
        defaulthidestate = utils.getDdeDockHideState()
        self.assertTrue(utils.dock.hidestate_show == defaulthidestate)
        main_window = self.ddedockobject.child(self.dock_mainwindow)
        (width, height) = main_window.size
        self.assertTrue(width > 0)
        self.assertTrue(height > 0)
        (x, y) = main_window.position
        self.assertTrue(0 == x)

    def suite():
        suite = unittest.TestSuite()
        suite.addTest(FashionExistLeft('testBasicFunction'))
        suite.addTest(FashionExistLeft('testChangePositionToLeft'))
        return suite

if __name__ == "__main__":
    executeTestCase.runTest(FashionExistLeft)
