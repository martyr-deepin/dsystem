#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import time
import gettext
import unittest
from lib import executeTestCase
from lib import utils
from lib import runner
from dogtail.tree import root
from dogtail import rawinput
from lib.dde_dock import Dock

casename = "all-6231:右键-强制退出"

class Dock_IconMenuForceQuit(unittest.TestCase):
    caseid = '282487'
    @classmethod
    def setUpClass(cls):
        cls.dock = Dock()
        cls.filemanagericonname = cls.dock.string_Deepin_File_Manager
        cls.filemanagerwindowname = cls.dock.string_Deepin_File_Manager
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

        utils.keySingle(utils.k.down_key)
        utils.keySingle(utils.k.enter_key)

        iconfilemanager.click(3)

        utils.keySingle(utils.k.down_key)
        utils.keySingle(utils.k.down_key)
        utils.keySingle(utils.k.enter_key)

        filemanagerwinlist = utils.findWindowList(self.filemanagerwindowname)
        self.assertTrue(2 == len(filemanagerwinlist))

        iconfilemanager.click(3)

        utils.keySingle(utils.k.down_key)
        utils.keySingle(utils.k.down_key)
        utils.keySingle(utils.k.down_key)
        utils.keySingle(utils.k.down_key)
        utils.keySingle(utils.k.enter_key)

        win = utils.findWindow(self.filemanagerwindowname, mode="nowait")
        self.assertTrue(None == win)

    def testSelectMenuNewWindow(self):
        try:
            iconfilemanager = self.ddedockobject.child(self.filemanagericonname)
            print(iconfilemanager.position)
        except:
            self.assertTrue(False, "Can't find the file manager icon on the Dock")

        iconfilemanager.click(3)

        utils.keySingle(utils.k.down_key)
        utils.keySingle(utils.k.down_key)
        utils.keySingle(utils.k.enter_key)

    def testSelectMenuCloseAll(self):
        try:
            iconfilemanager = self.ddedockobject.child(self.filemanagericonname)
        except:
            self.assertTrue(False, "Can't find the file manager icon on the Dock")

        iconfilemanager.click(3)

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
        suite.addTest(Dock_IconMenuForceQuit('testOpenRun'))

        return suite

if __name__ == "__main__":
    unittest.installHandler()
    LOCALE_DIR = os.path.abspath("./lib/locale")
    gettext.install('dsystem', LOCALE_DIR)
    executeTestCase.runTest(Dock_IconMenuForceQuit)
