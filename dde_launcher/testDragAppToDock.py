#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
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
        cls.startTime = time.time()
        cls.qqName = 'apps.com.qq.im'

    @classmethod
    def tearDownClass(cls):
        seconds = "%.3f" % (time.time() - cls.startTime)
        minutes = utils.convertToMinutes(float(seconds))
        global result
        utils.commitresult(caseid, result, minutes)
        launcher.freeMode()
        launcher.unDock()

    def testDragToDockFree(self):
        launcher.freeMode()
        launcher.dragAppToDockFree('QQ',quit=True)
        self.assertIn(self.qqName,Dock().getAllDockApps())

    def testDragToDockCategory(self):
        launcher.unDock()
        launcher.categoryMode()
        launcher.dragAppToDockCategory('chat')
        self.assertIn(self.qqName,Dock().getAllDockApps())

    def suite():
        suite = unittest.TestSuite()
        suite.addTest(LauncherDragAppToDock('testDragToDockFree'))
        suite.addTest(LauncherDragAppToDock('testDragToDockCategory'))
        return suite


    class MyTestResult(runner.MyTextTestResult):
        def addError(self, test, err):
            super(LauncherDragAppToDock.MyTestResult, self).addError(test, err)
            global result
            result = result and False

        def addFailure(self, test, err):
            super(LauncherDragAppToDock.MyTestResult, self).addFailure(test, err)
            global result
            result = result and False

if __name__ == "__main__":
    unittest.TextTestRunner(resultclass=LauncherDragAppToDock.MyTestResult).run(LauncherDragAppToDock.suite())
