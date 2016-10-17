#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import unittest
from lib import runner,utils
from lib.launcher import *


result = True

class DeepinTerminal(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.caseid = '83378'
        cls.casename = 'all-3358:运行深度终端'
        cls.appName = 'deepin-terminal'
        _, cls.username = subprocess.getstatusoutput("whoami")
        cls.winName = cls.username + ' - 深度终端'
        cls.oldWindows = getAllWindows()


    @classmethod
    def tearDownClass(cls):
        global result
        utils.commitresult(cls.caseid, result)
        newWindows = getAllWindows()
        if len(newWindows) > len(cls.oldWindows):
            newWindow = newWindows[-1]
            newWindow.close(1)

    def testDeepinTerminal(self):
        launcher.searchApp(self.appName)
        sleep(1)
        launcher.launcherObj.child('深度终端').click(3)
        pyautogui.press('down')
        pyautogui.press('enter')
        winName = getAllWindowNames()
        self.assertIn(self.winName,winName)

    def suite():
        suite = unittest.TestSuite()
        suite.addTest(DeepinTerminal('testDeepinTerminal'))
        return suite

    class MyTestResult(runner.MyTextTestResult):
        def addError(self, test, err):
            super(DeepinTerminal.MyTestResult, self).addError(test, err)
            global result
            result = result and False

        def addFailure(self, test, err):
            super(DeepinTerminal.MyTestResult, self).addFailure(test, err)
            global result
            result = result and False

if __name__ == "__main__":
    unittest.TextTestRunner(resultclass=DeepinTerminal.MyTestResult).run(DeepinTerminal.suite())