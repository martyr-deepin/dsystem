#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import unittest
import time
from subprocess import getstatusoutput
from lib import utils
from lib import runner
from lib.launcher import *
from lib import executeTestCase
from pymouse import PyMouse
from pykeyboard import PyKeyboard
from dogtail.tree import *

casename = "all-497:时尚模式拖动删除图标驻留"

class DragDockiconToDel(unittest.TestCase):
    caseid = '33735'

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
        cls.icon_dfm = "深度文件管理器"
        cls.icon_dmusic = "深度音乐"
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
        DragDockiconToDel.AddApptoDock(cls.icon_dfm)
        DragDockiconToDel.AddApptoDock(cls.icon_dmusic)

    def test_dragtodel_dfm(self):
        dockobject_dfm = utils.getDdeDockObject()
        iconobj_dfm = dockobject_dfm.child(self.icon_dfm)
        self.assertTrue(iconobj_dfm.showing)
        starting_point = utils.getDockIconCenterPoint(iconobj_dfm)
        utils.mouseDrag(starting_point,(starting_point[0],starting_point[1]-100))
        iconobj_dfm_later = utils.getDdeDockObject().child(self.icon_dfm)
        self.assertFalse(iconobj_dfm_later.showing)

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
        self.assertFalse(iconobj_dmusic_later.showing)

    def suite():
        suite = unittest.TestSuite()
        suite.addTest(DragDockiconToDel('test_dragtodel_dfm'))
        suite.addTest(DragDockiconToDel('test_dragtodel_dmusic'))
        return suite

if __name__ == "__main__":
    executeTestCase.runTest(DragDockiconToDel)
