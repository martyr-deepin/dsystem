#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import unittest
import time
from lib import runner,utils
from lib.launcher import *
from lib.dde_dock import *

result = True
caseid = '33974'
casename = 'all-547:多次重启启动器'

class LauncherReboot(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.startTime = time.time()
        cls.cmd = 'killall dde-launcher; dde-launcher -s &'

    @classmethod
    def tearDownClass(cls):
        seconds = "%.3f" % (time.time() - cls.startTime)
        minutes = utils.convertToMinutes(float(seconds))
        global result
        utils.commitresult(caseid, result, minutes)
        launcher.exitLauncher()


    def testReboot(self):
        for i in range(5):
            subprocess.check_call(self.cmd, shell=True)
            launcher.openLauncher()
            win = getWindowName()
            self.assertEqual(win,'dde-launcher')

    def suite():
        suite = unittest.TestSuite()
        suite.addTest(LauncherReboot('testReboot'))
        return suite

    class MyTestResult(runner.MyTextTestResult):
        def addError(self, test, err):
            super(LauncherReboot.MyTestResult, self).addError(test, err)
            global result
            result = result and False

        def addFailure(self, test, err):
            super(LauncherReboot.MyTestResult, self).addFailure(test, err)
            global result
            result = result and False

if __name__ == "__main__":
    unittest.TextTestRunner(resultclass=LauncherReboot.MyTestResult).run(LauncherReboot.suite())
