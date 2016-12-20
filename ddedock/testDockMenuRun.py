#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
import time
from lib import executeTestCase
from lib import utils
from lib import runner
from lib.launcher import launcher
from dogtail.tree import root
from dogtail import rawinput

casename = "all-2415:运行"

class DockMenuRun(unittest.TestCase):
    caseid = '63328'
    @classmethod
    def setUpClass(cls):
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

    def testOpenKeyC(self):
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

        utils.keySingle('c')

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
        self.testOpenKeyC()

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
        suite.addTest(DockMenuRun('testOpenKeyR'))
        suite.addTest(DockMenuRun('testAppExist'))
        suite.addTest(DockMenuRun('testCloseApp'))
        suite.addTest(DockMenuRun('testExistOnDock'))

        # change display mode
        suite.addTest(DockMenuRun('testExChangeDisplayMode'))

        suite.addTest(DockMenuRun('testOpenKeyR'))
        suite.addTest(DockMenuRun('testAppExist'))
        suite.addTest(DockMenuRun('testCloseApp'))
        suite.addTest(DockMenuRun('testExistOnDock'))

        return suite

if __name__ == "__main__":
    executeTestCase.runTest(DockMenuRun)
