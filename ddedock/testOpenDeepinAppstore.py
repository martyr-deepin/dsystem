#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from time import sleep
import unittest
from lib import utils

class DeepinAppstore(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.icon_deepinappstore = "深度商店"
        cls.window_name = "深度商店 — Deepin Store"
        cls.ddedockobject = utils.getDdeDockObject()
        cls.defaultdisplaymode = utils.getDdeDockDisplayMode()
        cls.defaultposition = utils.getDdeDockPosition()
        if utils.dock.position_bottom != cls.defaultposition:
            utils.setDdeDockPosition(utils.dock.position_bottom)

    @classmethod
    def tearDownClass(cls):
        utils.setDdeDockDisplayMode(cls.defaultdisplaymode)
        utils.setDdeDockPosition(cls.defaultposition)

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testOpenWithClick(self):
        iconobj = self.ddedockobject.child(self.icon_deepinappstore)
        self.assertTrue(iconobj)
        iconobj.click()
        sleep(4)
        win = utils.findWindow(self.window_name)
        self.assertTrue(win)

    def testClose(self):
        win = utils.findWindow(self.window_name)
        utils.closeWindow(win)
        win = None
        sleep(3)
        win = utils.findWindow(self.window_name)
        self.assertFalse(win)

    def testOpenWithR(self):
        iconobj = self.ddedockobject.child(self.icon_deepinappstore)
        self.assertTrue(iconobj)
        iconobj.click(3)
        utils.keySingle('r')
        sleep(4)
        win = utils.findWindow(self.window_name)
        self.assertTrue(win)

    def testOpenWithEnter(self):
        iconobj = self.ddedockobject.child(self.icon_deepinappstore)
        self.assertTrue(iconobj)
        iconobj.click(3)
        utils.keySingle(utils.k.down_key)
        utils.keySingle(utils.k.enter_key)
        sleep(4)
        win = utils.findWindow(self.window_name)
        self.assertTrue(win)

    def testChangeDockPositionTop(self):
        utils.setDdeDockPosition(utils.dock.position_top)

    def testChangeDockPositionRight(self):
        utils.setDdeDockPosition(utils.dock.position_right)

    def testChangeDockPositionLeft(self):
        utils.setDdeDockPosition(utils.dock.position_left)

    def testChangeDockDisplayMode(self):
        currentmode = utils.getDdeDockDisplayMode()
        if utils.dock.displaymode_fashion == currentmode:
            utils.setDdeDockDisplayMode(utils.dock.displaymode_efficient)
        elif utils.dock.displaymode_efficient == currentmode:
            utils.setDdeDockDisplayMode(utils.dock.displaymode_fashion)
        else:
            self.assertTrue(False, "Can't find the special display mode")

def suite():
    suite = unittest.TestSuite()
    suite.addTest(DeepinAppstore('testOpenWithClick'))
    suite.addTest(DeepinAppstore('testClose'))
    suite.addTest(DeepinAppstore('testOpenWithR'))
    suite.addTest(DeepinAppstore('testClose'))
    suite.addTest(DeepinAppstore('testOpenWithEnter'))
    suite.addTest(DeepinAppstore('testClose'))
    suite.addTest(DeepinAppstore('testChangeDockDisplayMode'))
    suite.addTest(DeepinAppstore('testOpenWithClick'))
    suite.addTest(DeepinAppstore('testClose'))
    suite.addTest(DeepinAppstore('testOpenWithR'))
    suite.addTest(DeepinAppstore('testClose'))
    suite.addTest(DeepinAppstore('testOpenWithEnter'))
    suite.addTest(DeepinAppstore('testClose'))

    # position top
    suite.addTest(DeepinAppstore('testChangeDockPositionTop'))
    suite.addTest(DeepinAppstore('testOpenWithClick'))
    suite.addTest(DeepinAppstore('testClose'))
    suite.addTest(DeepinAppstore('testOpenWithR'))
    suite.addTest(DeepinAppstore('testClose'))
    suite.addTest(DeepinAppstore('testOpenWithEnter'))
    suite.addTest(DeepinAppstore('testClose'))
    suite.addTest(DeepinAppstore('testChangeDockDisplayMode'))
    suite.addTest(DeepinAppstore('testOpenWithClick'))
    suite.addTest(DeepinAppstore('testClose'))
    suite.addTest(DeepinAppstore('testOpenWithR'))
    suite.addTest(DeepinAppstore('testClose'))
    suite.addTest(DeepinAppstore('testOpenWithEnter'))
    suite.addTest(DeepinAppstore('testClose'))

    # position right
    suite.addTest(DeepinAppstore('testChangeDockPositionRight'))
    suite.addTest(DeepinAppstore('testOpenWithClick'))
    suite.addTest(DeepinAppstore('testClose'))
    suite.addTest(DeepinAppstore('testOpenWithR'))
    suite.addTest(DeepinAppstore('testClose'))
    suite.addTest(DeepinAppstore('testOpenWithEnter'))
    suite.addTest(DeepinAppstore('testClose'))
    suite.addTest(DeepinAppstore('testChangeDockDisplayMode'))
    suite.addTest(DeepinAppstore('testOpenWithClick'))
    suite.addTest(DeepinAppstore('testClose'))
    suite.addTest(DeepinAppstore('testOpenWithR'))
    suite.addTest(DeepinAppstore('testClose'))
    suite.addTest(DeepinAppstore('testOpenWithEnter'))
    suite.addTest(DeepinAppstore('testClose'))

    # position left
    suite.addTest(DeepinAppstore('testChangeDockPositionLeft'))
    suite.addTest(DeepinAppstore('testOpenWithClick'))
    suite.addTest(DeepinAppstore('testClose'))
    suite.addTest(DeepinAppstore('testOpenWithR'))
    suite.addTest(DeepinAppstore('testClose'))
    suite.addTest(DeepinAppstore('testOpenWithEnter'))
    suite.addTest(DeepinAppstore('testClose'))
    suite.addTest(DeepinAppstore('testChangeDockDisplayMode'))
    suite.addTest(DeepinAppstore('testOpenWithClick'))
    suite.addTest(DeepinAppstore('testClose'))
    suite.addTest(DeepinAppstore('testOpenWithR'))
    suite.addTest(DeepinAppstore('testClose'))
    suite.addTest(DeepinAppstore('testOpenWithEnter'))
    suite.addTest(DeepinAppstore('testClose'))

    return suite

if __name__ == "__main__":
    unittest.TextTestRunner(verbosity=1).run(suite())
