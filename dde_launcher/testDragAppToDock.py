#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from lib import runner,utils
from dogtail import rawinput
from lib.launcher import *
from lib.dde_dock import *

result = True
caseid = '33823'
casename = "all-514:拖动到任务栏驻留"

class MyTestResult(runner.MyTextTestResult):
    def addError(self, test, err):
        super(MyTestResult, self).addError(test, err)
        global result
        result = result and False

    def addFailure(self, test, err):
        super(MyTestResult, self).addFailure(test, err)
        global result
        result = result and False

class LauncherDragAppToDock(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        global result
        utils.commitresult(caseid, result)
        launcher.freeMode()
        launcher.unDock()


    def testDragToDockFree(self):
        launcher.dragAppToDockFree()
        self.assertIn('QQ',Dock().getAllDockApps())

    def testDragToDockCategory(self):
        launcher.unDock()
        launcher.dragAppToDockCategory('chat')
        self.assertIn('QQ',Dock().getAllDockApps())

def suite():
    suite = unittest.TestSuite()
    suite.addTest(LauncherDragAppToDock('testDragToDockFree'))
    suite.addTest(LauncherDragAppToDock('testDragToDockCategory'))
    return suite

if __name__ == "__main__":
    unittest.TextTestRunner(resultclass=MyTestResult).run(suite())
