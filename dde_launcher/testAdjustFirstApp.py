#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from lib import runner,utils
from lib.launcher import *

result = True

class MyTestResult(runner.MyTextTestResult):
    def addError(self, test, err):
        super(MyTestResult, self).addError(test, err)
        global result
        result = result and False

    def addFailure(self, test, err):
        super(MyTestResult, self).addFailure(test, err)
        global result
        result = result and False

class LauncherAdjustFirstApp(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.caseid = '45878'
        cls.casename = "all-2149:调整首个程序位置"


    @classmethod
    def tearDownClass(cls):
        global result
        utils.commitresult(cls.caseid, result)


    def testDragToSecond(self):
        apps = launcher.getLauncherAllApps()
    	first = apps[0]
        launcher.dragToSecond()
        apps = launcher.getLauncherAllApps()
    	second = apps[1]
        self.assertEqual(first, second)

    def testDragToFirstRowEnd(self):
        apps = launcher.getLauncherAllApps()
    	first = apps[0]
        launcher.dragToFirstRowEnd()
        apps = launcher.getLauncherAllApps()
    	rowEnd = apps[6]
        self.assertEqual(first, rowEnd)


    def testDragToFirstColumnEnd(self):
        apps = launcher.getLauncherAllApps()
    	first = apps[0]
        launcher.dragToFirstColumnEnd()
        apps = launcher.getLauncherAllApps()
        columnEndIndex = launcher.getColumnEndIndex()
    	columnEnd = apps[columnEndIndex]
        self.assertNotEqual(first, columnEnd)

    def testDragToEnd(self):
        apps = launcher.getLauncherAllApps()
    	first = apps[0]
        launcher.dragToEnd()
        apps = launcher.getLauncherAllApps()
        endIndex = len(launcher.launcherObj.child('all',roleName='list').children)
    	end = apps[endIndex-1]
        self.assertEqual(first, end)


def suite():
    suite = unittest.TestSuite()
    suite.addTest(LauncherAdjustFirstApp('testDragToSecond'))
    suite.addTest(LauncherAdjustFirstApp('testDragToFirstRowEnd'))
    #suite.addTest(LauncherAdjustFirstApp('testDragToFirstColumnEnd'))
    #suite.addTest(LauncherAdjustFirstApp('testDragToEnd'))
    return suite

if __name__ == "__main__":
    unittest.TextTestRunner(verbosity=1).run(suite())
