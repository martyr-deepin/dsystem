#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from lib import runner,utils
from lib.launcher import *
from time import sleep

result = True

class LauncherMutiSearch(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.caseid = '45676'
        cls.casename = "all-2136:中文和英文搜索"
        cls.text = 'wps表格'
        cls.appName = 'WPS 表格'


    @classmethod
    def tearDownClass(cls):
        global result
        utils.commitresult(cls.caseid, result)
    
        
    
    def testMutiSearch(self):
        launcher.searchApp(self.text)
        sleep(2)
        apps = launcher.getLauncherAllApps()
        apps = ''.join(apps)
        sleep(2)
        launcher.exitLauncher()
        self.assertEqual(self.appName, apps)



    def suite():
        suite = unittest.TestSuite()
        suite.addTest(LauncherMutiSearch('testMutiSearch'))
        return suite

    class MyTestResult(runner.MyTextTestResult):
        def addError(self, test, err):
            super(LauncherMutiSearch.MyTestResult, self).addError(test, err)
            global result
            result = result and False

        def addFailure(self, test, err):
            super(LauncherMutiSearch.MyTestResult, self).addFailure(test, err)
            global result
            result = result and False

if __name__ == "__main__":
    unittest.TextTestRunner(resultclass=LauncherMutiSearch.MyTestResult).run(LauncherMutiSearch.suite())
