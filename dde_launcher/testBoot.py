#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import unittest
from lib import runner,utils
from lib.launcher import *
from lib.dde_dock import *

result = True
caseid = '33855'
casename = 'all-522:添加至开机启动项'

class MyTestResult(runner.MyTextTestResult):
    def addError(self, test, err):
        super(MyTestResult, self).addError(test, err)
        global result
        result = result and False

    def addFailure(self, test, err):
        super(MyTestResult, self).addFailure(test, err)
        global result
        result = result and False

class LauncherAddToBoot(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.menuObj = root.application(appName='deepin-menu', description='/usr/lib/deepin-menu')
        cls.googleName = 'Google Chrome'
        cls.QQname = 'QQ'
        cls.googleFile = 'google-chrome.desktop'
        cls.QQFile = 'apps.com.qq.im.desktop'

    @classmethod
    def tearDownClass(cls):
        global result
        utils.commitresult(caseid, result)
        googleFeild = getBootFeild(cls.googleFile)
        QQFeild = getBootFeild(cls.QQFile)
        if googleFeild == 'Hidden=false':
            launcher.menuBoot(cls.googleName)
            launcher.exitLauncher()
        if QQFeild == 'Hidden=false':
            launcher.menuBoot(cls.QQname)
            launcher.exitLauncher()


    def testMenuAddToBoot(self):
        launcher.menuBoot(self.googleName,self.QQname)
        launcher.exitLauncher()
        googleFeild = getBootFeild(self.googleFile)
        QQFeild = getBootFeild(self.QQFile)
        self.assertEqual('Hidden=false',googleFeild)
        self.assertEqual('Hidden=false',QQFeild)

    def testMenuRemoveFromBoot(self):
        launcher.menuBoot(self.QQname)
        launcher.exitLauncher()
        QQFeild = getBootFeild(self.QQFile)
        self.assertEqual('Hidden=true',QQFeild)


def suite():
    suite = unittest.TestSuite()
    suite.addTest(LauncherAddToBoot('testMenuAddToBoot'))
    suite.addTest(LauncherAddToBoot('testMenuRemoveFromBoot'))
    return suite

if __name__ == "__main__":
    unittest.TextTestRunner(resultclass=MyTestResult).run(suite())