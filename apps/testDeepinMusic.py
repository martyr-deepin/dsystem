#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import unittest
from lib import runner,utils
from lib.launcher import *


result = True

class DeepinMusic(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.caseid = '83309'
        cls.casename = 'all-3344:运行深度音乐'
        cls.appName = 'deepin-music-player'
        cls.winName = '深度音乐'
        cls.oldWindows = getAllWindows()


    @classmethod
    def tearDownClass(cls):
        global result
        utils.commitresult(cls.caseid, result)


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

    class MyTestResult(runner.MyTextTestResult):
        def addError(self, test, err):
            super(DeepinMusic.MyTestResult, self).addError(test, err)
            global result
            result = result and False

        def addFailure(self, test, err):
            super(DeepinMusic.MyTestResult, self).addFailure(test, err)
            global result
            result = result and False

if __name__ == "__main__":
    unittest.TextTestRunner(resultclass=DeepinMusic.MyTestResult).run(DeepinMusic.suite())