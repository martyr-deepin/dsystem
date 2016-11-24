#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import unittest
import time
from lib import runner,utils
from lib.launcher import *
from lib.dde_dock import *

result = True
caseid = '33898'
casename = 'all-2275:第一次点击super是否显示启动器'

class LauncherStartup(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.startTime = time.time()
        cls.cmd = 'killall dde-launcher &'

    @classmethod
    def tearDownClass(cls):
        seconds = "%.3f" % (time.time() - cls.startTime)
        minutes = utils.convertToMinutes(float(seconds))
        global result
        utils.commitresult(caseid, result, minutes)
        launcher.exitLauncher()

    def testOne(self):
        subprocess.check_call(self.cmd, shell=True)
        launcher.openLauncher()
        win = getWindowName()
        self.assertEqual(win,'dde-launcher')


    def testMore(self):
        for i in range(5):
            subprocess.check_call(self.cmd, shell=True)
            launcher.openLauncher()
            win = getWindowName()
            self.assertEqual(win,'dde-launcher')

    def suite():
        suite = unittest.TestSuite()
        suite.addTest(LauncherStartup('testOne'))
        suite.addTest(LauncherStartup('testMore'))
        return suite

    class MyTestResult(runner.MyTextTestResult):
        def addError(self, test, err):
            super(LauncherStartup.MyTestResult, self).addError(test, err)
            global result
            result = result and False

        def addFailure(self, test, err):
            super(LauncherStartup.MyTestResult, self).addFailure(test, err)
            global result
            result = result and False

if __name__ == "__main__":
    unittest.TextTestRunner(resultclass=LauncherStartup.MyTestResult).run(LauncherStartup.suite())
