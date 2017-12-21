#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import unittest
from lib import executeTestCase
from lib.launcher import *
from lib.dde_dock import *

result = True
casename = 'all-547:多次重启启动器'

class LauncherReboot(unittest.TestCase):
    caseid = '33974'
    @classmethod
    def setUpClass(cls):
        cls.cmd = 'killall dde-launcher; dde-launcher -s &'

    @classmethod
    def tearDownClass(cls):
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


if __name__ == "__main__":
    executeTestCase.runTest(LauncherReboot)
