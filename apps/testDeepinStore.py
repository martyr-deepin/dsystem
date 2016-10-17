#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import unittest
from lib import runner,utils
from lib.launcher import *


result = True

class DeepinStore(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.caseid = '83287'
        cls.casename = 'all-3339:打开深度商店'
        cls.appName = 'deepin-appstore'
        cls.winName = '深度商店 — Deepin Store'
        cls.oldWindows = getAllWindows()


    @classmethod
    def tearDownClass(cls):
        global result
        utils.commitresult(cls.caseid, result)

    def setUp(self):
        pass

    def tearDown(self):
        newWindows = getAllWindows()
        if len(newWindows) > len(self.oldWindows):
            newWindow = newWindows[-1]
            newWindow.close(1)

    def testDeepinStore1(self):
        subprocess.check_call(self.appName + ' &', shell=True)
        winName = getWindowName()
        self.assertEqual(self.winName,winName)

    def testDeepinStore2(self):
        launcher.searchApp(self.appName)
        sleep(1)
        pyautogui.press('enter')
        winName = getWindowName()
        self.assertEqual(self.winName,winName)


    def suite():
        suite = unittest.TestSuite()
        suite.addTest(DeepinStore('testDeepinStore1'))
        suite.addTest(DeepinStore('testDeepinStore2'))
        return suite

    class MyTestResult(runner.MyTextTestResult):
        def addError(self, test, err):
            super(DeepinStore.MyTestResult, self).addError(test, err)
            global result
            result = result and False

        def addFailure(self, test, err):
            super(DeepinStore.MyTestResult, self).addFailure(test, err)
            global result
            result = result and False

if __name__ == "__main__":
    unittest.TextTestRunner(resultclass=DeepinStore.MyTestResult).run(DeepinStore.suite())