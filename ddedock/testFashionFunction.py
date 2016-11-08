#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from lib import utils
from lib import runner

caseid = '68136'
casename = "all-2471:时尚模式功能测试"
result = True

class FashionFunction(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.startTime = time.time()
        cls.ddedockobject = utils.getDdeDockObject()
        cls.defaultdisplaymode = utils.getDdeDockDisplayMode()
        cls.defaultposition = utils.getDdeDockPosition()
        cls.dock_mainwindow = "dock-mainwindow"

    @classmethod
    def tearDownClass(cls):
        seconds = %.3f % (time.time() - cls.startTime)
        minutes = utils.convertToMinutes(float(seconds))
        global result
        utils.commitresult(caseid, result, minutes)

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

    def testKeepDisplayMode(self):
        utils.m.click(int(utils.resolution.width/2), utils.resolution.height, 2)
        utils.dockmenu.findMainWindow()
        utils.keySingle(utils.k.down_key)
        utils.keySingle(utils.k.enter_key)
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

    def testChangeDisplayMode(self):
        utils.m.click(int(utils.resolution.width/2), utils.resolution.height, 2)
        utils.dockmenu.findMainWindow()
        utils.keySingle(utils.k.down_key)
        utils.keySingle(utils.k.down_key)
        utils.keySingle(utils.k.enter_key)
        defaultdisplaymode = utils.getDdeDockDisplayMode()
        self.assertTrue(utils.dock.displaymode_efficient == defaultdisplaymode)
        defaultposition = utils.getDdeDockPosition()
        self.assertTrue(utils.dock.position_bottom == defaultposition)
        defaulthidestate = utils.getDdeDockHideState()
        self.assertTrue(utils.dock.hidestate_show == defaulthidestate)
        main_window = self.ddedockobject.child(self.dock_mainwindow)
        (width, height) = main_window.size
        self.assertTrue(width > 0)
        self.assertTrue(height > 0)

    def testChangeBackDisplayMode(self):
        utils.m.click(int(utils.resolution.width/2), utils.resolution.height, 2)
        utils.dockmenu.findMainWindow()
        utils.keySingle(utils.k.down_key)
        utils.keySingle(utils.k.enter_key)
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

    def suite():
        suite = unittest.TestSuite()
        suite.addTest(FashionFunction('testBasicFunction'))
        suite.addTest(FashionFunction('testKeepDisplayMode'))
        suite.addTest(FashionFunction('testChangeDisplayMode'))
        suite.addTest(FashionFunction('testChangeBackDisplayMode'))
        return suite

    class MyTestResult(runner.MyTextTestResult):
        def addError(self, test, err):
            super(FashionFunction.MyTestResult, self).addError(test, err)
            global result
            result = result and False

        def addFailure(self, test, err):
            super(FashionFunction.MyTestResult, self).addFailure(test, err)
            global result
            result = result and False

if __name__ == "__main__":
    unittest.TextTestRunner(resultclass=FashionFunction.MyTestResult).run(FashionFunction.suite())
