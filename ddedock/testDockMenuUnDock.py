#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
import time
import time
from lib import utils
from lib import runner
from lib.launcher import launcher
from dogtail.tree import root
from dogtail import rawinput

result = True
caseid = '63333'
casename = "all-2416:移除驻留"

class DockMenuUnDock(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.startTime = time.time()
        cls.filemanagericonname = "深度文件管理器"
        cls.filemanagerwindowname = "深度文件管理器"
        cls.filemanagerlauncher = "dde-file-manager"
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

    def testOpenKeyR(self):
        try:
            iconfilemanager = self.ddedockobject.child(self.filemanagericonname)
        except:
            self.assertTrue(False, "Can't find the file manager icon on the Dock")

        iconfilemanager.click(3)

        try:
            dockmenuapp = root.application('deepin-menu', '/usr/lib/deepin-menu')
            dockmenu = dockmenuapp.child(utils.dock.dockmenuname)
        except:
            self.assertTrue(False, "Can't find dockmenu")

        self.assertTrue(dockmenu.position[0] > 1)
        self.assertTrue(dockmenu.position[1] > 1)
        self.assertTrue(dockmenu.size[0] > 1)
        self.assertTrue(dockmenu.size[1] > 1)

        utils.keySingle('r')

    def testOpenKeyU(self):
        try:
            iconfilemanager = self.ddedockobject.child(self.filemanagericonname)
        except:
            self.assertTrue(False, "Can't find the file manager icon on the Dock")

        iconfilemanager.click(3)

        try:
            dockmenuapp = root.application('deepin-menu', '/usr/lib/deepin-menu')
            dockmenu = dockmenuapp.child(utils.dock.dockmenuname)
        except:
            self.assertTrue(False, "Can't find dockmenu")

        self.assertTrue(dockmenu.position[0] > 1)
        self.assertTrue(dockmenu.position[1] > 1)
        self.assertTrue(dockmenu.size[0] > 1)
        self.assertTrue(dockmenu.size[1] > 1)

        utils.keySingle('u')

    def testCloseApp(self):
        appwin = utils.findWindow(self.filemanagerwindowname, comparetype="notequal")
        utils.closeWindow(appwin)

        appwin = utils.findWindow(self.filemanagerwindowname, mode="nowait", comparetype="notequal")
        self.assertTrue(None == appwin)

    def testAppExist(self):
        appwin = utils.findWindow(self.filemanagerwindowname, comparetype="notequal")
        self.assertTrue(None != appwin)

    def testNotExistOnDock(self):
        dockicon = self.ddedockobject.child(self.filemanagericonname)
        self.assertTrue((0, 0) == dockicon.position)
        self.assertTrue((0, 0) == dockicon.size)

    def testExistOnDock(self):
        dockicon = self.ddedockobject.child(self.filemanagericonname)
        self.assertTrue(dockicon.position[0] > 1)
        self.assertTrue(dockicon.position[1] > 1)
        self.assertTrue(dockicon.size[0] > 1)
        self.assertTrue(dockicon.size[1] > 1)

    def testSetDock(self):
        utils.keySingle(utils.k.windows_l_key)
        try:
            launcherwin = utils.findWindow("dde-launcher")
        except:
            self.assertTrue(False, "Can't open dde-launcher")

        utils.keyTypeString(self.filemanagerlauncher)

        app = launcher.getAppObj(self.filemanagericonname)
        app.click(3)

        try:
            dockmenuapp = root.application('deepin-menu', '/usr/lib/deepin-menu')
            dockmenu = dockmenuapp.child(utils.desktop.desktopmenuname)
        except:
            self.assertTrue(False, "Can't find desktopmenu")

        utils.keySingle('c')

    def testExChangeDisplayMode(self):
        if utils.getDdeDockDisplayMode() == utils.dock.displaymode_fashion:
            utils.setDdeDockDisplayMode(utils.dock.displaymode_efficient)
        elif utils.getDdeDockDisplayMode() == utils.dock.displaymode_efficient:
            utils.setDdeDockDisplayMode(utils.dock.displaymode_fashion)

    def testCloseLauncher(self):
        utils.keySingle(utils.k.windows_l_key)
        time.sleep(1)

    def suite():
        suite = unittest.TestSuite()
        suite.addTest(DockMenuUnDock('testOpenKeyU'))
        suite.addTest(DockMenuUnDock('testNotExistOnDock'))
        suite.addTest(DockMenuUnDock('testSetDock'))
        suite.addTest(DockMenuUnDock('testExistOnDock'))
        suite.addTest(DockMenuUnDock('testCloseLauncher'))

        # change display mode
        suite.addTest(DockMenuUnDock('testExChangeDisplayMode'))

        suite.addTest(DockMenuUnDock('testOpenKeyU'))
        suite.addTest(DockMenuUnDock('testNotExistOnDock'))
        suite.addTest(DockMenuUnDock('testSetDock'))
        suite.addTest(DockMenuUnDock('testExistOnDock'))
        suite.addTest(DockMenuUnDock('testCloseLauncher'))

        return suite

    class MyTestResult(runner.MyTextTestResult):
        def addError(self, test, err):
            super(DockMenuUnDock.MyTestResult, self).addError(test, err)
            global result
            result = result and False

        def addFailure(self, test, err):
            super(DockMenuUnDock.MyTestResult, self).addFailure(test, err)
            global result
            result = result and False

if __name__ == "__main__":
    unittest.TextTestRunner(resultclass=DockMenuUnDock.MyTestResult).run(DockMenuUnDock.suite())
