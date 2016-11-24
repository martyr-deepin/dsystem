#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
import time
from lib import runner,utils
from lib.launcher import *
from time import sleep

result = True
caseid = '45345'
casename = "all-2103:搜索框快捷键测试-ctrl+c"

class LauncherShotcuts_ctrl_c(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.startTime = time.time()
        cls.text = '深度商店'


    @classmethod
    def tearDownClass(cls):
        seconds = "%.3f" % (time.time() - cls.startTime)
        minutes = utils.convertToMinutes(float(seconds))
        global result
        utils.commitresult(caseid, result, minutes)

    def test_ctrl_c(self):
        launcher.openLauncher()
        launcher.launcherObj.child('search-edit').click()
        launcher.launcherObj.child('search-edit').text = self.text
        pyautogui.hotkey('ctrl','a')
        pyautogui.hotkey('ctrl','c')
        launcher.exitLauncher()
        launcher.openLauncher()
        launcher.launcherObj.child('search-edit').click()
        pyautogui.hotkey('ctrl','v')
        launcher.exitLauncher()
        self.assertEqual(launcher.launcherObj.child('search-edit').text, self.text)


    def suite():
        suite = unittest.TestSuite()
        suite.addTest(LauncherShotcuts_ctrl_c('test_ctrl_c'))
        return suite

    class MyTestResult(runner.MyTextTestResult):
        def addError(self, test, err):
            super(LauncherShotcuts_ctrl_c.MyTestResult, self).addError(test, err)
            global result
            result = result and False

        def addFailure(self, test, err):
            super(LauncherShotcuts_ctrl_c.MyTestResult, self).addFailure(test, err)
            global result
            result = result and False

if __name__ == "__main__":
    unittest.TextTestRunner(resultclass=LauncherShotcuts_ctrl_c.MyTestResult).run(LauncherShotcuts_ctrl_c.suite())
