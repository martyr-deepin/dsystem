#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from time import sleep
import unittest
from lib import utils
from lib import runner

result = True

class DockSoundHover(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.startTime = time.time()
        cls.caseid = '91228'
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
        seconds = %.3f % (time.time() - cls.startTime)
        minutes = utils.convertToMinutes(float(seconds))
        global result
        utils.commitresult(caseid, result, minutes)

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

    class MyTestResult(runner.MyTextTestResult):
        def addError(self, test, err):
            super(DockSoundHover.MyTestResult, self).addError(test, err)
            global result
            result = result and False

        def addFailure(self, test, err):
            super(DockSoundHover.MyTestResult, self).addFailure(test, err)
            global result
            result = result and False

if __name__ == "__main__":
    unittest.TextTestRunner(resultclass=DockSoundHover.MyTestResult).run(DockSoundHover.suite())
