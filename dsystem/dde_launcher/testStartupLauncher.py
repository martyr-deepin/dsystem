#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import unittest
from lib import executeTestCase
from lib.launcher import *
from lib.dde_dock import *

result = True
casename = 'all-2275:第一次点击super是否显示启动器'

class LauncherStartup(unittest.TestCase):
    caseid = '33898'
    @classmethod
    def setUpClass(cls):
        cls.cmd = 'killall dde-launcher &'

    @classmethod
    def tearDownClass(cls):
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


if __name__ == "__main__":
    executeTestCase.runTest(LauncherStartup)
