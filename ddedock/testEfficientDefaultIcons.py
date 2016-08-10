#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from lib import utils

class EfficientDefaultIcons(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.defaultefficienticonlist = ["Launcher",
                                        "显示桌面",
                                        "多任务视图",
                                        "文件",
                                        "深度商店",
                                        "深度音乐",
                                        "Google Chrome",
                                        "控制中心",
                                        "shutdown-shutdown",
                                        "datetime-"]

        cls.ddedockobject = utils.getDdeDockObject()
        cls.defaultdisplaymode = utils.getDdeDockDisplayMode()
        cls.defaultposition    = utils.getDdeDockPosition()

        if utils.dock.displaymode_efficient != cls.defaultdisplaymode:
            utils.setDdeDockDisplayMode(utils.dock.displaymode_efficient)

        if utils.dock.position_bottom != cls.defaultposition:
            utils.setDdeDockPosition(utils.dock.position_bottom)

    @classmethod
    def tearDownClass(cls):
        utils.setDdeDockDisplayMode(cls.defaultdisplaymode)
        utils.setDdeDockPosition(cls.defaultposition)

    def testExists(self):
        for name in self.defaultefficienticonlist:
            icon = self.ddedockobject.child(name)
            self.assertTrue(icon, "Can't find the [ %s ] icon in the dock region with Fashion Mode" % name)

    def testDifferentMode(self):
        mode = utils.getDdeDockDisplayMode()
        self.assertTrue(mode == utils.dock.displaymode_efficient)
        utils.setDdeDockDisplayMode(utils.dock.displaymode_fashion)
        mode = utils.getDdeDockDisplayMode()
        self.assertTrue(mode == utils.dock.displaymode_fashion)
        utils.setDdeDockDisplayMode(utils.dock.displaymode_efficient)
        mode = utils.getDdeDockDisplayMode()
        self.assertTrue(mode == utils.dock.displaymode_efficient)

    def testExistsChangedMode(self):
        for name in self.defaultefficienticonlist:
            icon = self.ddedockobject.child(name)
            self.assertTrue(icon, "Can't find the [ %s ] icon in the dock region after chenge back to Fashion Mode" % name)

    def testTopExists(self):
        utils.setDdeDockPosition(utils.dock.position_top)
        for name in self.defaultefficienticonlist:
            icon = self.ddedockobject.child(name)
            self.assertTrue(icon, "Position Top: Can't find the [ %s ] icon in the dock region after chenge back to Fashion Mode" % name)

    def testTopDifferentMode(self):
        mode = utils.getDdeDockDisplayMode()
        self.assertTrue(mode == utils.dock.displaymode_efficient)
        utils.setDdeDockDisplayMode(utils.dock.displaymode_fashion)
        mode = utils.getDdeDockDisplayMode()
        self.assertTrue(mode == utils.dock.displaymode_fashion)
        utils.setDdeDockDisplayMode(utils.dock.displaymode_efficient)
        mode = utils.getDdeDockDisplayMode()
        self.assertTrue(mode == utils.dock.displaymode_efficient)

    
    def testTopExistsChangedMode(self):
        for name in self.defaultefficienticonlist:
            icon = self.ddedockobject.child(name)
            self.assertTrue(icon, "Position Top: Can't find the [ %s ] icon in the dock region after chenge back to Fashion Mode" % name)

    def testRightExists(self):
        utils.setDdeDockPosition(utils.dock.position_right)
        for name in self.defaultefficienticonlist:
            icon = self.ddedockobject.child(name)
            self.assertTrue(icon, "Position Right: Can't find the [ %s ] icon in the dock region after chenge back to Fashion Mode" % name)

    def testRightDifferentMode(self):
        mode = utils.getDdeDockDisplayMode()
        self.assertTrue(mode == utils.dock.displaymode_efficient)
        utils.setDdeDockDisplayMode(utils.dock.displaymode_fashion)
        mode = utils.getDdeDockDisplayMode()
        self.assertTrue(mode == utils.dock.displaymode_fashion)
        utils.setDdeDockDisplayMode(utils.dock.displaymode_efficient)
        mode = utils.getDdeDockDisplayMode()
        self.assertTrue(mode == utils.dock.displaymode_efficient)

    def testRightExistsChangedMode(self):
        for name in self.defaultefficienticonlist:
            icon = self.ddedockobject.child(name)
            self.assertTrue(icon, "Position right: Can't find the [ %s ] icon in the dock region after chenge back to Fashion Mode" % name)

    def testLeftExists(self):
        utils.setDdeDockPosition(utils.dock.position_left)
        for name in self.defaultefficienticonlist:
            icon = self.ddedockobject.child(name)
            self.assertTrue(icon, "Position Left: Can't find the [ %s ] icon in the dock region after chenge back to Fashion Mode" % name)

    def testLeftDifferentMode(self):
        mode = utils.getDdeDockDisplayMode()
        self.assertTrue(mode == utils.dock.displaymode_efficient)
        utils.setDdeDockDisplayMode(utils.dock.displaymode_fashion)
        mode = utils.getDdeDockDisplayMode()
        self.assertTrue(mode == utils.dock.displaymode_fashion)
        utils.setDdeDockDisplayMode(utils.dock.displaymode_efficient)
        mode = utils.getDdeDockDisplayMode()
        self.assertTrue(mode == utils.dock.displaymode_efficient)

    def testLeftExistsChangedMode(self):
        for name in self.defaultefficienticonlist:
            icon = self.ddedockobject.child(name)
            self.assertTrue(icon, "Position Left: Can't find the [ %s ] icon in the dock region after chenge back to Fashion Mode" % name)

def suite():
    suite = unittest.TestSuite()
    suite.addTest(EfficientDefaultIcons('testExists'))
    suite.addTest(EfficientDefaultIcons('testDifferentMode'))
    suite.addTest(EfficientDefaultIcons('testExistsChangedMode'))
    suite.addTest(EfficientDefaultIcons('testTopExists'))
    suite.addTest(EfficientDefaultIcons('testTopDifferentMode'))
    suite.addTest(EfficientDefaultIcons('testTopExistsChangedMode'))
    suite.addTest(EfficientDefaultIcons('testRightExists'))
    suite.addTest(EfficientDefaultIcons('testRightDifferentMode'))
    suite.addTest(EfficientDefaultIcons('testRightExistsChangedMode'))
    suite.addTest(EfficientDefaultIcons('testLeftExists'))
    suite.addTest(EfficientDefaultIcons('testLeftDifferentMode'))
    suite.addTest(EfficientDefaultIcons('testLeftExistsChangedMode'))
    return suite

if __name__ == "__main__":
    unittest.TextTestRunner(verbosity=1).run(suite())
