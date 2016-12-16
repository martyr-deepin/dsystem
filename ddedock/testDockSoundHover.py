#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from time import sleep
import unittest
from lib import executeTestCase
from lib import utils
from lib import runner

result = True
class DockSoundHover(unittest.TestCase):
    caseid = '91228'
    @classmethod
    def setUpClass(cls):
        cls.casename = 'all-3547:hover 声音插件'
        cls.icon_sound = "sound-"
        cls.popup_percent = "70%"
        cls.ddedockobject = utils.getDdeDockObject()

        if utils.getDdeDockPosition != utils.dock.position_bottom:
            utils.setDdeDockPosition(utils.dock.position_bottom)

        if utils.getDdeDockDisplayMode != utils.dock.displaymode_fashion:
            utils.setDdeDockDisplayMode(utils.dock.displaymode_fashion)

    @classmethod
    def tearDownClass(cls):
        if utils.getDdeDockPosition != utils.dock.position_bottom:
            utils.setDdeDockPosition(utils.dock.position_bottom)

        if utils.getDdeDockDisplayMode != utils.dock.displaymode_fashion:
            utils.setDdeDockDisplayMode(utils.dock.displaymode_fashion)

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSoundHover(self):
        iconobj = self.ddedockobject.child(self.icon_sound)
        self.assertTrue(iconobj)
        iconobj.point()

        percentobj = self.ddedockobject.child(self.popup_percent)
        sleep(2)
        self.assertTrue(percentobj)
        percentobj.point()

    def testExChangeDisplayMode(self):
        if utils.getDdeDockDisplayMode() == utils.dock.displaymode_fashion:
            utils.setDdeDockDisplayMode(utils.dock.displaymode_efficient)
        elif utils.getDdeDockDisplayMode() == utils.dock.displaymode_efficient:
            utils.setDdeDockDisplayMode(utils.dock.displaymode_fashion)

    def suite():
        suite = unittest.TestSuite()
        suite.addTest(DockSoundHover('testSoundHover'))

        return suite

if __name__ == "__main__":
    executeTestCase.runTest(DockSoundHover)
