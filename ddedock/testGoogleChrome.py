#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
import time
from lib import utils
from lib import runner
from dogtail.tree import root
from dogtail import rawinput

result = True

class GoogleChrome(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.caseid = '33440'
        cls.casename = "all-441:google chrome"
        cls.chromeiconname = "Google Chrome"
        cls.ddedockobject = utils.getDdeDockObject()

        if utils.dock.displaymode_fashion != utils.getDdeDockDisplayMode():
            utils.setDdeDockDisplayMode(utils.dock.displaymode_fashion)

        if utils.dock.position_bottom != utils.getDdeDockPosition():
            utils.setDdeDockPosition(utils.dock.position_bottom)

    @classmethod
    def tearDownClass(cls):
        global result
        utils.commitresult(cls.caseid, result)

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

    def testOpenNew(self):
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
        utils.keySingle(utils.k.down_key)
        utils.keySingle(utils.k.enter_key)

    def testOpenHide(self):
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
        utils.keySingle(utils.k.down_key)
        utils.keySingle(utils.k.down_key)
        utils.keySingle(utils.k.enter_key)

    def testCloseGoogleChrome(self):
        chromewin = utils.findWindow("Google Chrome", comparetype="notequal")
        utils.closeWindow(chromewin)

        chromewin = utils.findWindow("Google Chrome", mode="nowait", comparetype="notequal")
        self.assertTrue(None == chromewin)

    def testGoogleChromeExist(self):
        chromewin = utils.findWindow("Google Chrome", comparetype="notequal")
        self.assertTrue(None != chromewin)

    def clickScreenCenter(self):
        rawinput.click(int(utils.resolution.width/2), int(utils.resolution.height/2))
        time.sleep(1)

    def testExChangeDisplayMode(self):
        if utils.getDdeDockDisplayMode() == utils.dock.displaymode_fashion:
            utils.setDdeDockDisplayMode(utils.dock.displaymode_efficient)
        elif utils.getDdeDockDisplayMode() == utils.dock.displaymode_efficient:
            utils.setDdeDockDisplayMode(utils.dock.displaymode_fashion)

    def suite():
        suite = unittest.TestSuite()
        suite.addTest(GoogleChrome('testOpenRun'))
        suite.addTest(GoogleChrome('testGoogleChromeExist'))
        suite.addTest(GoogleChrome('testCloseGoogleChrome'))
        suite.addTest(GoogleChrome('testOpenNew'))
        suite.addTest(GoogleChrome('testGoogleChromeExist'))
        suite.addTest(GoogleChrome('testCloseGoogleChrome'))
        suite.addTest(GoogleChrome('testOpenHide'))
        suite.addTest(GoogleChrome('testGoogleChromeExist'))
        suite.addTest(GoogleChrome('testCloseGoogleChrome'))
        suite.addTest(GoogleChrome('clickScreenCenter'))

        # change display mode
        suite.addTest(GoogleChrome('testExChangeDisplayMode'))

        suite.addTest(GoogleChrome('testOpenRun'))
        suite.addTest(GoogleChrome('testGoogleChromeExist'))
        suite.addTest(GoogleChrome('testCloseGoogleChrome'))
        suite.addTest(GoogleChrome('testOpenNew'))
        suite.addTest(GoogleChrome('testGoogleChromeExist'))
        suite.addTest(GoogleChrome('testCloseGoogleChrome'))
        suite.addTest(GoogleChrome('testOpenHide'))
        suite.addTest(GoogleChrome('testGoogleChromeExist'))
        suite.addTest(GoogleChrome('testCloseGoogleChrome'))
        suite.addTest(GoogleChrome('clickScreenCenter'))

        return suite

    class MyTestResult(runner.MyTextTestResult):
        def addError(self, test, err):
            super(GoogleChrome.MyTestResult, self).addError(test, err)
            global result
            result = result and False

        def addFailure(self, test, err):
            super(GoogleChrome.MyTestResult, self).addFailure(test, err)
            global result
            result = result and False

if __name__ == "__main__":
    unittest.TextTestRunner(resultclass=GoogleChrome.MyTestResult).run(GoogleChrome.suite())
