#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
import time
from lib import runner,utils
from lib.launcher import *
from time import sleep

result = True
caseid = '45362'
casename = "all-2108:搜索框快捷键测试-ctrl+x"

class LauncherShotcuts_ctrl_x(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.startTime = time.time()
        cls.text = '腾讯QQ'


    @classmethod
    def tearDownClass(cls):
        seconds = "%.3f" % (time.time() - cls.startTime)
        minutes = utils.convertToMinutes(float(seconds))
        global result
        utils.commitresult(caseid, result, minutes)

    def test_ctrl_x(self):
        launcher.openLauncher()
        launcher.launcherObj.child('search-edit').click()
        launcher.launcherObj.child('search-edit').text = self.text
        pyautogui.hotkey('ctrl','a')
        pyautogui.hotkey('ctrl','x')
        launcher.exitLauncher()
        launcher.openLauncher()
        launcher.launcherObj.child('search-edit').click()
        pyautogui.hotkey('ctrl','v')
        launcher.exitLauncher()
        self.assertEqual(launcher.launcherObj.child('search-edit').text, self.text)


    def suite():
        suite = unittest.TestSuite()
        suite.addTest(LauncherShotcuts_ctrl_x('test_ctrl_x'))
        return suite

    class MyTestResult(runner.MyTextTestResult):
        def addError(self, test, err):
            super(LauncherShotcuts_ctrl_x.MyTestResult, self).addError(test, err)
            global result
            result = result and False

        def addFailure(self, test, err):
            super(LauncherShotcuts_ctrl_x.MyTestResult, self).addFailure(test, err)
            global result
            result = result and False

if __name__ == "__main__":
    unittest.TextTestRunner(resultclass=LauncherShotcuts_ctrl_x.MyTestResult).run(LauncherShotcuts_ctrl_x.suite())
