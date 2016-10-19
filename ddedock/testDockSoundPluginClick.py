#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from time import sleep
import unittest
from lib import utils
from lib import runner

result = True

class DockSoundPluginClick(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.caseid = '91223'
        cls.casename = 'all-3546:声音插件对单击的响应'
        cls.icon_sound = "sound-"
        cls.popup_name = "设备"
        cls.ddedockobject = utils.getDdeDockObject()

        if utils.getDdeDockPosition != utils.dock.position_bottom:
            utils.setDdeDockPosition(utils.dock.position_bottom)

        if utils.getDdeDockDisplayMode != utils.dock.displaymode_fashion:
            utils.setDdeDockDisplayMode(utils.dock.displaymode_fashion)

    @classmethod
    def tearDownClass(cls):
        global result
        utils.commitresult(cls.caseid, result)

        if utils.getDdeDockPosition != utils.dock.position_bottom:
            utils.setDdeDockPosition(utils.dock.position_bottom)

        if utils.getDdeDockDisplayMode != utils.dock.displaymode_fashion:
            utils.setDdeDockDisplayMode(utils.dock.displaymode_fashion)

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSoundPluginClick(self):
        iconobj = self.ddedockobject.child(self.icon_sound)
        self.assertTrue(iconobj)
        iconobj.click()
        popupobj = self.ddedockobject.child(self.popup_name)
        self.assertTrue(popupobj)
        popupobj.point()
        self.assertTrue((0, 0) != popupobj.position)
        self.assertTrue((0, 0) != popupobj.size)

        iconobj = self.ddedockobject.child(self.icon_sound)
        self.assertTrue(iconobj)
        iconobj.click()
        popupobj = self.ddedockobject.child(self.popup_name)
        self.assertTrue((0, 0) == popupobj.position)
        self.assertTrue((0, 0) == popupobj.size)

    def testExChangeDisplayMode(self):
        if utils.getDdeDockDisplayMode() == utils.dock.displaymode_fashion:
            utils.setDdeDockDisplayMode(utils.dock.displaymode_efficient)
        elif utils.getDdeDockDisplayMode() == utils.dock.displaymode_efficient:
            utils.setDdeDockDisplayMode(utils.dock.displaymode_fashion)

    def suite():
        suite = unittest.TestSuite()
        suite.addTest(DockSoundPluginClick('testSoundPluginClick'))
        suite.addTest(DockSoundPluginClick('testExChangeDisplayMode'))
        suite.addTest(DockSoundPluginClick('testSoundPluginClick'))

        return suite

    class MyTestResult(runner.MyTextTestResult):
        def addError(self, test, err):
            super(DockSoundPluginClick.MyTestResult, self).addError(test, err)
            global result
            result = result and False

        def addFailure(self, test, err):
            super(DockSoundPluginClick.MyTestResult, self).addFailure(test, err)
            global result
            result = result and False

if __name__ == "__main__":
    unittest.TextTestRunner(resultclass=DockSoundPluginClick.MyTestResult).run(DockSoundPluginClick.suite())
