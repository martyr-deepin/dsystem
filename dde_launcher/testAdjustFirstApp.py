#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from lib import runner,utils
from lib.launcher import *

result = True

class LauncherAdjustFirstApp(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.caseid = '45878'
        cls.casename = 'all-2149:调整首个程序位置'
        launcher.freeMode()


    @classmethod
    def tearDownClass(cls):
        global result
        utils.commitresult(cls.caseid, result)
        launcher.freeMode()


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

    class MyTestResult(runner.MyTextTestResult):
        def addError(self, test, err):
            super(LauncherAdjustFirstApp.MyTestResult, self).addError(test, err)
            global result
            result = result and False

        def addFailure(self, test, err):
            super(LauncherAdjustFirstApp.MyTestResult, self).addFailure(test, err)
            global result
            result = result and False

if __name__ == "__main__":
    unittest.TextTestRunner(resultclass=LauncherAdjustFirstApp.MyTestResult).run(LauncherAdjustFirstApp.suite())
