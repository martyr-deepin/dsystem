#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import gettext
import unittest
import time
from subprocess import getstatusoutput
from lib import utils
from lib import runner
from lib.launcher import *
from lib import Dock
from lib import runTest
from pymouse import PyMouse
from pykeyboard import PyKeyboard
from dogtail.tree import *

casename = "all-5352:将dock上的应用图标拖拽到桌面丢弃"

class Dock_DragDockiconToDel(unittest.TestCase):
    caseid = '191645'

    def  AddApptoDock(appname):
        m = PyMouse()
        p = PyKeyboard()
        launcher.searchApp(appname)
        sleep(1)
        lc = root.application('dde-launcher','/usr/bin/dde-launcher')
        child_dfm = lc.child(appname)
        #print(lc.get_child_count)
        x,y = child_dfm.position
        m.click(x,y,2)
        time.sleep(1)
        p.press_key('Down')
        p.release_key('Down')
        time.sleep(1)
        p.press_key('Down')
        p.release_key('Down')
        time.sleep(1)
        p.press_key('Down')
        p.release_key('Down')
        time.sleep(1)
        p.press_key('Return')
        p.release_key('Return')
        launcher.exitLauncher()

    @classmethod
    def setUpClass(cls):
        cls.ddedock = Dock()
        cls.icon_dfm = cls.ddedock.string_Deepin_File_Manager
        cls.icon_dmusic = cls.ddedock.string_Deepin_Music
        if utils.dock.displaymode_fashion != utils.getDdeDockDisplayMode():
            utils.setDdeDockDisplayMode(utils.dock.displaymode_fashion)
        if utils.dock.position_bottom != utils.getDdeDockPosition():
            utils.setDdeDockPosition(utils.dock.position_bottom)

    @classmethod
    def tearDownClass(cls):
        if utils.getDdeDockDisplayMode() != utils.dock.displaymode_fashion:
            utils.setDdeDockDisplayMode(utils.dock.displaymode_fashion)
        if utils.getDdeDockPosition() != utils.dock.position_bottom:
            utils.setDdeDockPosition(utils.dock.position_bottom)
        os.system('killall chrome')
        Dock_DragDockiconToDel.AddApptoDock(cls.icon_dfm)
        Dock_DragDockiconToDel.AddApptoDock(cls.icon_dmusic)

    def test_dragtodel_dfm(self):
        dockobject_dfm = utils.getDdeDockObject()
        iconobj_dfm = dockobject_dfm.child(self.icon_dfm)
        self.assertTrue(iconobj_dfm.showing)
        starting_point = utils.getDockIconCenterPoint(iconobj_dfm)
        utils.mouseDrag(starting_point,(starting_point[0],starting_point[1]-100))
        iconobj_dfm_later = utils.getDdeDockObject().child(self.icon_dfm)
        self.assertTrue(None == iconobj_dfm_later)

    def test_dragtodel_dmusic(self):
        pid = os.fork()
        if 0 == pid:
            (status,output)  = getstatusoutput('google-chrome')
            os._exit(0)
        dockobject_dmusic = utils.getDdeDockObject()
        iconobj_dmusic = dockobject_dmusic.child(self.icon_dmusic)
        self.assertTrue(iconobj_dmusic.showing)
        # iconobj_dmusic.click()
        starting_point = utils.getDockIconCenterPoint(iconobj_dmusic)
        utils.mouseDrag(starting_point,(starting_point[0],starting_point[1]-100))
        iconobj_dmusic_later = utils.getDdeDockObject().child(self.icon_dmusic)
        self.assertTrue(None == iconobj_dmusic_later)

    def suite():
        suite = unittest.TestSuite()
        suite.addTest(Dock_DragDockiconToDel('test_dragtodel_dfm'))
        suite.addTest(Dock_DragDockiconToDel('test_dragtodel_dmusic'))
        return suite

if __name__ == "__main__":
    unittest.installHandler()
    LOCALE_DIR = os.path.abspath("./lib/locale")
    gettext.install('dsystem', LOCALE_DIR)
    runTest(Dock_DragDockiconToDel)
