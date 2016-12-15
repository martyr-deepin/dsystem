#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from lib import executeTestCase
from lib import utils
from lib import runner
from dogtail.tree import root
from dogtail import rawinput

result = True
caseid = '33451'
casename = "all-443:关闭所有"

class DockIconMenuMultiClose(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.filemanagericonname = "深度文件管理器"
        cls.filemanagerwindowname = "深度文件管理器"
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

    def testOpenRun(self):
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

        utils.keySingle(utils.k.down_key)
        utils.keySingle(utils.k.enter_key)

    def testSelectMenuNewWindow(self):
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

        utils.keySingle(utils.k.down_key)
        utils.keySingle(utils.k.down_key)
        utils.keySingle(utils.k.enter_key)

    def testSelectMenuCloseAll(self):
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

        utils.keySingle(utils.k.down_key)
        utils.keySingle(utils.k.down_key)
        utils.keySingle(utils.k.down_key)
        utils.keySingle(utils.k.enter_key)

    def testFileManagerExist(self):
        filemanagerwinlist = utils.findWindowList(self.filemanagerwindowname)
        self.assertTrue(3 == len(filemanagerwinlist))

    def testCloseFileManager(self):
        filemanagerwin = utils.WindowState(self.filemanagerwindowname)
        filemanagerwin.close()
        win = utils.findWindow(self.filemanagerwindowname, mode="nowait")
        self.assertTrue(None == win)

    def minimizeWin(self):
        filemanagerwin = utils.WindowState(self.filemanagerwindowname)
        filemanagerwin.minimize()
        state = filemanagerwin.is_minimized()
        self.assertTrue(state)

    def testExpectResult(self):
        filemanagerwin = utils.findWindow(self.filemanagerwindowname, mode="nowait")
        self.assertTrue(None == filemanagerwin)

    def testExChangeDisplayMode(self):
        if utils.getDdeDockDisplayMode() == utils.dock.displaymode_fashion:
            utils.setDdeDockDisplayMode(utils.dock.displaymode_efficient)
        elif utils.getDdeDockDisplayMode() == utils.dock.displaymode_efficient:
            utils.setDdeDockDisplayMode(utils.dock.displaymode_fashion)

    def suite():
        suite = unittest.TestSuite()
        suite.addTest(DockIconMenuMultiClose('testOpenRun'))
        suite.addTest(DockIconMenuMultiClose('testSelectMenuNewWindow'))
        suite.addTest(DockIconMenuMultiClose('testSelectMenuNewWindow'))
        suite.addTest(DockIconMenuMultiClose('testFileManagerExist'))
        suite.addTest(DockIconMenuMultiClose('testSelectMenuCloseAll'))
        suite.addTest(DockIconMenuMultiClose('testExpectResult'))

        # change display mode
        suite.addTest(DockIconMenuMultiClose('testExChangeDisplayMode'))

        suite.addTest(DockIconMenuMultiClose('testOpenRun'))
        suite.addTest(DockIconMenuMultiClose('testSelectMenuNewWindow'))
        suite.addTest(DockIconMenuMultiClose('testSelectMenuNewWindow'))
        suite.addTest(DockIconMenuMultiClose('testFileManagerExist'))
        suite.addTest(DockIconMenuMultiClose('testSelectMenuCloseAll'))
        suite.addTest(DockIconMenuMultiClose('testExpectResult'))

        return suite

if __name__ == "__main__":
    runTest(DockIconMenuMultiClose.suite())
