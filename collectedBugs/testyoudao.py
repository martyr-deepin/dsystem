#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from lib import runner,utils
from lib.launcher import *
from lib.window import findWindow

result = True
caseid = '80279'
casename = "all-2977:有道词典测试"

class Youdao(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = 'youdaocidian'
        cls.appName = '有道词典'
        cls.oldWindows = getAllWindows()


    @classmethod
    def tearDownClass(cls):
        global result
        utils.commitresult(caseid, result)
        cls.newWindows = getAllWindows()
        if len(cls.newWindows) - len(cls.oldWindows) == 1:
            cls.newWindows[-1].close(1)

    def testYoudao(self):
        launcher.openLauncher()
        launcher.searchApp(self.app)
        sleep(2)
        apps = launcher.getLauncherAllApps()
        apps = ''.join(apps)
        self.assertEqual(self.appName, apps)
        pyautogui.press('enter')
        #winname = findWindow(self.appName)
        winname = getWindowName()
        self.assertEqual(winname, self.appName)

    def suite():
        suite = unittest.TestSuite()
        suite.addTest(Youdao('testYoudao'))
        return suite

    class MyTestResult(runner.MyTextTestResult):
        def addError(self, test, err):
            super(Youdao.MyTestResult, self).addError(test, err)
            global result
            result = result and False

        def addFailure(self, test, err):
            super(Youdao.MyTestResult, self).addFailure(test, err)
            global result
            result = result and False

if __name__ == "__main__":
    unittest.TextTestRunner(resultclass=Youdao.MyTestResult).run(Youdao.suite())
