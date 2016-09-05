#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
import time
from lib import utils
from lib import runner
from dogtail.tree import root

result = True

class DockIconMenu(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.caseid = '33454'
        cls.casename = "all-444:驻留"
        cls.terminaliconname = "深度终端"
        cls.terminalwindowname = "deepin-terminal"
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

    def testOpenTerminalFromLauncher(self):
        utils.keySingle(utils.k.windows_l_key)
        try:
            launcherwin = utils.findWindow("dde-launcher")
        except:
            self.assertTrue(False, "Can't open dde-launcher")

        utils.keyTypeString("deepin-terminal")
        utils.keySingle(utils.k.enter_key)

        try:
            terminalwin = utils.findWindow(self.terminalwindowname)
            self.assertTrue(True)
        except:
            self.assertTrue(False, "Can't find window: %s" % self.terminalwindowname)

    def testDockTerminal(self):
        try:
            iconterminal = self.ddedockobject.child(self.terminaliconname)
        except:
            self.assertTrue(False, "Can't find the terminal icon on the Dock")

        iconterminal.click(3)

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
        utils.keySingle(utils.k.down_key)
        utils.keySingle(utils.k.down_key)
        utils.keySingle(utils.k.down_key)
        utils.keySingle(utils.k.enter_key)

    def testCloseTerminal(self):
        terminalwin = utils.findWindow(self.terminalwindowname)
        utils.closeWindow(terminalwin)
        terminalwin_later = utils.findWindow(self.terminalwindowname, mode="nowait")
        self.assertTrue(None == terminalwin_later)

    def testExpectResult(self):
        try:
            iconterminal = self.ddedockobject.child(self.terminaliconname)
            self.assertTrue(True)
        except:
            self.assertTrue(False, "Can't find terminal icon on the Dock")

    def testDragTerminalIconToDesktop(self):
        iconterminal = self.ddedockobject.child(self.terminaliconname)
        fromXY = utils.getDockIconCenterPoint(iconterminal)
        utils.mouseDrag(fromXY, (fromXY[0], fromXY[1] - 100))

        ddedock = utils.getDdeDockObject()
        try:
            iconterminal_later = ddedock.child(self.terminaliconname)
        except:
            self.assertTrue(True)

    def testExChangeDisplayMode(self):
        if utils.getDdeDockDisplayMode() == utils.dock.displaymode_fashion:
            utils.setDdeDockDisplayMode(utils.dock.displaymode_efficient)
        elif utils.getDdeDockDisplayMode() == utils.dock.displaymode_efficient:
            utils.setDdeDockDisplayMode(utils.dock.displaymode_fashion)

    def suite():
        suite = unittest.TestSuite()
        suite.addTest(DockIconMenu('testOpenTerminalFromLauncher'))
        suite.addTest(DockIconMenu('testDockTerminal'))
        suite.addTest(DockIconMenu('testCloseTerminal'))
        suite.addTest(DockIconMenu('testExpectResult'))
        suite.addTest(DockIconMenu('testDragTerminalIconToDesktop'))

        # change display mode
        suite.addTest(DockIconMenu('testExChangeDisplayMode'))

        suite.addTest(DockIconMenu('testOpenTerminalFromLauncher'))
        suite.addTest(DockIconMenu('testDockTerminal'))
        suite.addTest(DockIconMenu('testCloseTerminal'))
        suite.addTest(DockIconMenu('testExpectResult'))
        suite.addTest(DockIconMenu('testDragTerminalIconToDesktop'))

        return suite

    class MyTestResult(runner.MyTextTestResult):
        def addError(self, test, err):
            super(DockIconMenu.MyTestResult, self).addError(test, err)
            global result
            result = result and False

        def addFailure(self, test, err):
            super(DockIconMenu.MyTestResult, self).addFailure(test, err)
            global result
            result = result and False

if __name__ == "__main__":
    unittest.TextTestRunner(resultclass=DockIconMenu.MyTestResult).run(DockIconMenu.suite())
