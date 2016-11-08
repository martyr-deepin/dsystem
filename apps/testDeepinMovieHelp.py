#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import unittest
from lib import runner,utils
from lib.launcher import *
from lib.dde_dock import *

result = True
caseid = '83265'
casename = 'up-371:打开帮助手册'

class DeepinMovieHelp(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.startTime = time.time()
        cls.appName = 'deepin-movie'
        cls.winName = '深度影院'
        cls.helpWinName = '深度影院 - 深度帮助手册'
        cls.cmd = 'dman deepin-movie &'
        cls.oldWindows = getAllWindows()


    @classmethod
    def tearDownClass(cls):
        seconds = %.3f % (time.time() - cls.startTime)
        minutes = utils.convertToMinutes(float(seconds))
        global result
        utils.commitresult(caseid, result, minutes)
        cls.newWindows = getAllWindows()
        if len(cls.newWindows) > len(cls.oldWindows):
            newWindow = cls.newWindows[-1]
            newWindow.close(1)

    def setUp(self):
        pass

    def tearDown(self):
        newWindows = getAllWindows()
        if len(newWindows) > len(self.oldWindows):
            newWindow = newWindows[-1]
            newWindow.close(1)

    def testDeepinMovieHelp1(self):
        subprocess.check_call(self.appName + ' &', shell=True)
        winNames = getAllWindowNames()
        self.assertIn(self.winName,winNames)
        if self.winName in winNames:
            pyautogui.press('f1')
            winNames = getAllWindowNames()
            self.assertIn(self.helpWinName,winNames)

    def testDeepinMovieHelp2(self):
        subprocess.check_call(self.cmd, shell=True)
        winNames = getAllWindowNames()
        self.assertIn(self.helpWinName,winNames)

    def suite():
        suite = unittest.TestSuite()
        suite.addTest(DeepinMovieHelp('testDeepinMovieHelp1'))
        suite.addTest(DeepinMovieHelp('testDeepinMovieHelp2'))
        return suite

    class MyTestResult(runner.MyTextTestResult):
        def addError(self, test, err):
            super(DeepinMovieHelp.MyTestResult, self).addError(test, err)
            global result
            result = result and False

        def addFailure(self, test, err):
            super(DeepinMovieHelp.MyTestResult, self).addFailure(test, err)
            global result
            result = result and False

if __name__ == "__main__":
    unittest.TextTestRunner(resultclass=DeepinMovieHelp.MyTestResult).run(DeepinMovieHelp.suite())
