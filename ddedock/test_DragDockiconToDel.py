#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
import time
from subprocess import getstatusoutput
from lib import utils
from lib import runner


class DragDockiconToDel(unittest.TestCase):
    result = True
    @classmethod
    def setUpClass(cls):
        cls.caseid = '33735'
        cls.casename = "all-497:时尚模式拖动删除图标驻留"
        cls.icon_dfm = "深度文件管理器"
        cls.icon_dmusic = "深度音乐"
        if utils.dock.displaymode_fashion != utils.getDdeDockDisplayMode():
            utils.setDdeDockDisplayMode(utils.dock.displaymode_fashion)
        if utils.dock.position_bottom != utils.getDdeDockPosition():
            utils.setDdeDockPosition(utils.dock.position_bottom)

    @classmethod
    def tearDownClass(cls):
        utils.commitresult(cls.caseid, DragDockiconToDel.result)
        if utils.getDdeDockDisplayMode() != utils.dock.displaymode_fashion:
            utils.setDdeDockDisplayMode(utils.dock.displaymode_fashion)
        if utils.getDdeDockPosition() != utils.dock.position_bottom:
            utils.setDdeDockPosition(utils.dock.position_bottom)

    def test_dragtodel_dfm(self):
        dockobject_dfm = utils.getDdeDockObject()
        iconobj_dfm = dockobject_dfm.child(self.icon_dfm)
        self.assertTrue(iconobj_dfm.showing)
        starting_point = utils.getDockIconCenterPoint(iconobj_dfm)
        utils.mouseDrag(starting_point,(starting_point[0],starting_point[1]-100))
        iconobj_dfm_later = utils.getDdeDockObject().child(self.icon_dfm)
        self.assertFalse(iconobj_dfm_later.showing)

    def test_dragtodel_dmusic(self):
        # (status,output)  = getstatusoutput('google-chrome')
        # self.assertEqual(0,status)
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

    class MyTestResult(runner.MyTextTestResult):
        def addError(self, test, err):
            super(DragDockiconToDel.MyTestResult, self).addError(test, err)
            DragDockiconToDel.result = DragDockiconToDel.result and False

        def addFailure(self, test, err):
            super(DragDockiconToDel.MyTestResult, self).addFailure(test, err)
            DragDockiconToDel.result = DragDockiconToDel.result and False

if __name__ == "__main__":
    unittest.TextTestRunner(resultclass=DragDockiconToDel.MyTestResult).run(DragDockiconToDel.suite())
