#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
import time
import time
from lib import utils
from lib import runner
from dogtail.tree import root
from dogtail import rawinput

result = True
caseid = '33479'
casename = "all-449:程序显示隐藏测试"

class HideDisplayApp(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.startTime = time.time()
        cls.chromeiconname = "Google Chrome"
        cls.chromewindowname = "Google Chrome"
        cls.ddedockobject = utils.getDdeDockObject()

        if utils.dock.displaymode_fashion != utils.getDdeDockDisplayMode():
            utils.setDdeDockDisplayMode(utils.dock.displaymode_fashion)

        if utils.dock.position_bottom != utils.getDdeDockPosition():
            utils.setDdeDockPosition(utils.dock.position_bottom)

    @classmethod
    def tearDownClass(cls):
        seconds = "%.3f" % (time.time() - cls.startTime)
        minutes = utils.convertToMinutes(float(seconds))
        global result
        utils.commitresult(caseid, result, minutes)

        if utils.dock.displaymode_fashion != utils.getDdeDockDisplayMode():
            utils.setDdeDockDisplayMode(utils.dock.displaymode_fashion)

        if utils.dock.position_bottom != utils.getDdeDockPosition():
            utils.setDdeDockPosition(utils.dock.position_bottom)

    def testOpenRun(self):
        try:
            iconchrome = self.ddedockobject.child(self.chromeiconname)
        except:
            self.assertTrue(False, "Can't find the Google Chrome icon on the Dock")

        iconchrome.click(3)

        try:
            dockmenuapp = root.application('deepin-menu', '/usr/lib/deepin-menu')
            dockmenu = dockmenuapp.child(utils.dock.dockmenuname)
        except:
            self.assertTrue(False, "Can't find dockmenu")

        self.assertTrue(dockmenu.position[0] > 1)
        self.assertTrue(dockmenu.position[1] > 1)
        self.assertTrue(dockmenu.size[0] > 1)
        self.assertTrue(dockmenu.size[1] > 1)

        utils.keySingle(utils.k.down_key)
        utils.keySingle(utils.k.enter_key)

    def testCloseApp(self):
        chromewin = utils.findWindow(self.chromewindowname, comparetype="notequal")
        utils.closeWindow(chromewin)

        chromewin = utils.findWindow(self.chromewindowname, mode="nowait", comparetype="notequal")
        self.assertTrue(None == chromewin)

    def testAppExist(self):
        chromewin = utils.findWindow(self.chromewindowname, comparetype="notequal")
        self.assertTrue(None != chromewin)

    def clickDockAppIcon(self):
        dockappicon = self.ddedockobject.child(self.chromeiconname)
        dockappicon.click()

    def testClick(self):
        appwin = utils.findWindow(self.chromewindowname, comparetype="notequal")
        appstate = utils.WindowState(self.chromewindowname, comparetype="notequal")

        self.assertTrue(False == appstate.is_minimized())
        self.clickDockAppIcon()
        self.assertTrue(True == appstate.is_minimized())
        self.clickDockAppIcon()
        self.assertTrue(False == appstate.is_minimized())
        self.clickDockAppIcon()
        self.assertTrue(True == appstate.is_minimized())
        self.clickDockAppIcon()
        self.assertTrue(False == appstate.is_minimized())
        self.clickDockAppIcon()
        self.assertTrue(True == appstate.is_minimized())
        self.clickDockAppIcon()
        self.assertTrue(False == appstate.is_minimized())

    def testExChangeDisplayMode(self):
        if utils.getDdeDockDisplayMode() == utils.dock.displaymode_fashion:
            utils.setDdeDockDisplayMode(utils.dock.displaymode_efficient)
        elif utils.getDdeDockDisplayMode() == utils.dock.displaymode_efficient:
            utils.setDdeDockDisplayMode(utils.dock.displaymode_fashion)

    def suite():
        suite = unittest.TestSuite()
        suite.addTest(HideDisplayApp('testOpenRun'))
        suite.addTest(HideDisplayApp('testAppExist'))
        suite.addTest(HideDisplayApp('testClick'))
        suite.addTest(HideDisplayApp('testCloseApp'))

        # change display mode
        suite.addTest(HideDisplayApp('testExChangeDisplayMode'))

        suite.addTest(HideDisplayApp('testOpenRun'))
        suite.addTest(HideDisplayApp('testAppExist'))
        suite.addTest(HideDisplayApp('testClick'))
        suite.addTest(HideDisplayApp('testCloseApp'))

        return suite

    class MyTestResult(runner.MyTextTestResult):
        def addError(self, test, err):
            super(HideDisplayApp.MyTestResult, self).addError(test, err)
            global result
            result = result and False

        def addFailure(self, test, err):
            super(HideDisplayApp.MyTestResult, self).addFailure(test, err)
            global result
            result = result and False

if __name__ == "__main__":
    unittest.TextTestRunner(resultclass=HideDisplayApp.MyTestResult).run(HideDisplayApp.suite())
