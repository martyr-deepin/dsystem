#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import unittest
from lib import executeTestCase
from lib import runner,utils
from lib.launcher import *


result = True
casename = 'all-3344:运行深度音乐'

class DeepinMusic(unittest.TestCase):
    caseid = '83309'
    @classmethod
    def setUpClass(cls):
        cls.appName = 'deepin-music-player'
        cls.winName = '深度音乐'
        cls.oldWindows = getAllWindows()


    @classmethod
    def tearDownClass(cls):
        pas
    def setUp(self):
        pass

    def tearDown(self):
        subprocess.check_call("ps aux |grep music |grep -v grep |awk '{print $2}' |xargs kill -9", shell=True)

    def testDeepinMusic1(self):
        subprocess.check_call(self.appName + ' &', shell=True)
        winName = getAllWindowNames()
        self.assertIn(self.winName,winName)

    def testDeepinMusic2(self):
        launcher.searchApp(self.appName)
        sleep(1)
        pyautogui.press('enter')
        winName = getAllWindowNames()
        self.assertIn(self.winName,winName)

    def suite():
        suite = unittest.TestSuite()
        suite.addTest(DeepinMusic('testDeepinMusic1'))
        suite.addTest(DeepinMusic('testDeepinMusic2'))
        return suite

if __name__ == "__main__":
    executeTestCase.runTest(DeepinMusic)
