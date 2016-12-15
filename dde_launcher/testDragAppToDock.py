#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from lib import executeTestCase
import time
from lib import runner,utils
from dogtail import rawinput
from lib.launcher import *
from lib.dde_dock import *

result = True
caseid = '33823'
casename = "all-514:拖动到任务栏驻留"

class LauncherDragAppToDock(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.qqName = 'QQ'
        cls.dockname = 'apps.com.qq.im'

    @classmethod
    def tearDownClass(cls):
        launcher.freeMode()
        if cls.dockname in Dock().getAllDockApps():
            launcher.menuUnDock(cls.qqName)

    def setUp(self):
        pass

    def tearDown(self):
        if self.dockname in Dock().getAllDockApps():
            launcher.menuUnDock(self.qqName)

    def testDragToDockFree(self):
        launcher.freeMode()
        launcher.searchApp(self.qqName)
        launcher.dragAppToDockFree(self.qqName,quit=True)
        self.assertIn(self.dockname,Dock().getAllDockApps())

    def testDragToDockCategory(self):
        if self.qqName in Dock().getDockedApps():
            launcher.unDock()
        launcher.categoryMode()
        launcher.dragAppToDockCategory('chat')
        self.assertIn(self.dockname,Dock().getAllDockApps())

    def suite():
        suite = unittest.TestSuite()
        suite.addTest(LauncherDragAppToDock('testDragToDockFree'))
        suite.addTest(LauncherDragAppToDock('testDragToDockCategory'))
        return suite



if __name__ == "__main__":
    runTest(LauncherDragAppToDock.suite())
