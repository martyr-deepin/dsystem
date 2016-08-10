#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from lib import utils
from time import sleep

class IconDock(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.launchername = "deepin-appstore"
        cls.icon_deepinappstore = "深度商店"
        cls.ddedockobject = utils.getDdeDockObject()
        cls.defaultdisplaymode = utils.getDdeDockDisplayMode()
        cls.defaultposition = utils.getDdeDockPosition()
        if utils.dock.position_bottom != cls.defaultposition:
            utils.setDdeDockPosition(utils.dock.position_bottom)

    @classmethod
    def tearDownClass(cls):
        utils.setDdeDockDisplayMode(cls.defaultdisplaymode)
        utils.setDdeDockPosition(cls.defaultposition)
        utils.keySingle(utils.k.windows_l_key)

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testUnDock(self):
        iconobj = self.ddedockobject.child(self.icon_deepinappstore)
        self.assertTrue(iconobj)
        iconobj.click(3)
        utils.keySingle('u')
        sleep(3)
        iconobj_delete = self.ddedockobject.child(self.icon_deepinappstore)
        self.assertTrue(iconobj_delete.position == (0, 0))
        self.assertTrue(iconobj_delete.size == (0, 0))

    def testDragBack(self):
        utils.keySingle(utils.k.windows_l_key)
        utils.keyTypeString(self.launchername)
        #utils.keySingle(utils.k.enter_key)
        utils.m.move(253, 170)
        sleep(3)
        utils.m.press(253, 170)
        sleep(3)
        while utils.m.position()[0] < 427:
            utils.m.move((utils.m.position()[0]+1), utils.m.position()[1])
        while utils.m.position()[1] < 873:
            utils.m.move(utils.m.position()[0], (utils.m.position()[1]+1))
        while utils.m.position()[0] < 477:
            sleep(0.03)
            utils.m.move((utils.m.position()[0]+1), utils.m.position()[1])
        #utils.m.move(427, 873)
        sleep(2)
        utils.m.release(477, 873)
        sleep(3)
        iconobj = self.ddedockobject.child(self.icon_deepinappstore)
        self.assertTrue(iconobj)
        self.assertTrue(iconobj.position != (0, 0))
        self.assertTrue(iconobj.size != (0, 0))

    def testRightClickBack(self):
        utils.keySingle(utils.k.windows_l_key)
        utils.keyTypeString(self.launchername)
        utils.m.click(253, 170, 2)
        sleep(2)
        utils.keySingle(utils.k.down_key)
        utils.keySingle(utils.k.down_key)
        utils.keySingle(utils.k.down_key)
        utils.keySingle(utils.k.enter_key)
        iconobj = self.ddedockobject.child(self.icon_deepinappstore)
        self.assertTrue(iconobj)
        self.assertTrue(iconobj.position != (0, 0))
        self.assertTrue(iconobj.size != (0, 0))

def suite():
    suite = unittest.TestSuite()
    suite.addTest(IconDock('testUnDock'))
    suite.addTest(IconDock('testDragBack'))
    suite.addTest(IconDock('testUnDock'))
    suite.addTest(IconDock('testRightClickBack'))
    return suite

if __name__ == "__main__":
    unittest.TextTestRunner(verbosity=1).run(suite())
