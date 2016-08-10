#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from lib import utils
from lib.waiter import waiter

class FashionDefaultIcons(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.defaultfashioniconlist = ["Launcher",
                               "显示桌面",
                               "多任务视图",
                               "文件",
                               "深度商店",
                               "深度音乐",
                               "Google Chrome",
                               "控制中心",
                               "system-tray-fashion-mode-item",
                               "shutdown-shutdown",
                               "datetime-"]

        cls.ddedockobject = utils.getDdeDockObject()
        cls.defaultdisplaymode = utils.getDdeDockDisplayMode()
        cls.defaultposition    = utils.getDdeDockPosition()

        if utils.dock.position_bottom != cls.defaultposition:
            utils.setDdeDockPosition(utils.dock.position_bottom)

        if utils.dock.displaymode_fashion != cls.defaultdisplaymode:
            utils.setDdeDockDisplayMode(utils.dock.displaymode_fashion)

    @classmethod
    def tearDownClass(cls):
        utils.setDdeDockDisplayMode(cls.defaultdisplaymode)
        utils.setDdeDockPosition(cls.defaultposition)
    
    def testExists(self):
        for name in self.defaultfashioniconlist:
            icon = self.ddedockobject.child(name)
            self.assertTrue(icon, "Can't find the [ %s ] icon in the dock region with Efficient Mode" % name)

    def testDifferentMode(self):
        mode = utils.getDdeDockDisplayMode()
        self.assertTrue(mode == utils.dock.displaymode_fashion)
        utils.setDdeDockDisplayMode(utils.dock.displaymode_efficient)
        mode = utils.getDdeDockDisplayMode()
        self.assertTrue(mode == utils.dock.displaymode_efficient)
        utils.setDdeDockDisplayMode(utils.dock.displaymode_fashion)
        mode = utils.getDdeDockDisplayMode()
        self.assertTrue(mode == utils.dock.displaymode_fashion)

    def testExistsChangedMode(self):
        for name in self.defaultfashioniconlist:
            icon = self.ddedockobject.child(name)
            self.assertTrue(icon, "Can't find the [ %s ] icon in the dock region after chenge back to Efficient Mode" % name)

    def testTopExists(self):
        utils.setDdeDockPosition(utils.dock.position_top)
        for name in self.defaultfashioniconlist:
            icon = self.ddedockobject.child(name)
            self.assertTrue(icon, "Position Top: Can't find the [ %s ] icon in the dock region after chenge back to Efficient Mode" % name)

    def testTopDifferentMode(self):
        mode = utils.getDdeDockDisplayMode()
        self.assertTrue(mode == utils.dock.displaymode_fashion)
        utils.setDdeDockDisplayMode(utils.dock.displaymode_efficient)
        mode = utils.getDdeDockDisplayMode()
        self.assertTrue(mode == utils.dock.displaymode_efficient)
        utils.setDdeDockDisplayMode(utils.dock.displaymode_fashion)
        mode = utils.getDdeDockDisplayMode()
        self.assertTrue(mode == utils.dock.displaymode_fashion)

    def testTopExistsChangedMode(self):
        for name in self.defaultfashioniconlist:
            icon = self.ddedockobject.child(name)
            self.assertTrue(icon, "Position Top: Can't find the [ %s ] icon in the dock region after chenge back to Efficient Mode" % name)

    def testRightExists(self):
        utils.setDdeDockPosition(utils.dock.position_right)
        for name in self.defaultfashioniconlist:
            icon = self.ddedockobject.child(name)
            self.assertTrue(icon, "Position Right: Can't find the [ %s ] icon in the dock region after chenge back to Efficient Mode" % name)

    def testRightDifferentMode(self):
        mode = utils.getDdeDockDisplayMode()
        self.assertTrue(mode == utils.dock.displaymode_fashion)
        utils.setDdeDockDisplayMode(utils.dock.displaymode_efficient)
        mode = utils.getDdeDockDisplayMode()
        self.assertTrue(mode == utils.dock.displaymode_efficient)
        utils.setDdeDockDisplayMode(utils.dock.displaymode_fashion)
        mode = utils.getDdeDockDisplayMode()
        self.assertTrue(mode == utils.dock.displaymode_fashion)

    def testRightExistsChangedMode(self):
        for name in self.defaultfashioniconlist:
            icon = self.ddedockobject.child(name)
            self.assertTrue(icon, "Position Right: Can't find the [ %s ] icon in the dock region after chenge back to Efficient Mode" % name)

    def testLeftExists(self):
        utils.setDdeDockPosition(utils.dock.position_left)
        for name in self.defaultfashioniconlist:
            icon = self.ddedockobject.child(name)
            self.assertTrue(icon, "Position Right: Can't find the [ %s ] icon in the dock region after chenge back to Efficient Mode" % name)

    def testLeftDifferentMode(self):
        mode = utils.getDdeDockDisplayMode()
        self.assertTrue(mode == utils.dock.displaymode_fashion)
        utils.setDdeDockDisplayMode(utils.dock.displaymode_efficient)
        mode = utils.getDdeDockDisplayMode()
        self.assertTrue(mode == utils.dock.displaymode_efficient)
        utils.setDdeDockDisplayMode(utils.dock.displaymode_fashion)
        mode = utils.getDdeDockDisplayMode()
        self.assertTrue(mode == utils.dock.displaymode_fashion)

    def testLeftExistsChangedMode(self):
        for name in self.defaultfashioniconlist:
            icon = self.ddedockobject.child(name)
            self.assertTrue(icon, "Position Left: Can't find the [ %s ] icon in the dock region after chenge back to Efficient Mode" % name)

def suite():
    suite = unittest.TestSuite()
    suite.addTest(FashionDefaultIcons('testExists'))
    suite.addTest(FashionDefaultIcons('testDifferentMode'))
    suite.addTest(FashionDefaultIcons('testExistsChangedMode'))
    suite.addTest(FashionDefaultIcons('testTopExists'))
    suite.addTest(FashionDefaultIcons('testTopDifferentMode'))
    suite.addTest(FashionDefaultIcons('testTopExistsChangedMode'))
    suite.addTest(FashionDefaultIcons('testRightExists'))
    suite.addTest(FashionDefaultIcons('testRightDifferentMode'))
    suite.addTest(FashionDefaultIcons('testRightExistsChangedMode'))
    suite.addTest(FashionDefaultIcons('testLeftExists'))
    suite.addTest(FashionDefaultIcons('testLeftDifferentMode'))
    suite.addTest(FashionDefaultIcons('testLeftExistsChangedMode'))
    return suite

if __name__ == "__main__":
    unittest.TextTestRunner(verbosity=1).run(suite())
