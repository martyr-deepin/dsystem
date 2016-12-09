#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from lib import executeTestCase
import time
from lib import runner,utils
from lib.launcher import *
from time import sleep

result = True
#caseid = '45362'
caseid = '33410'
casename = "all-2108:搜索框快捷键测试-ctrl+x"

class LauncherShotcuts_ctrl_x(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.text = '腾讯QQ'


    @classmethod
    def tearDownClass(cls):
        pass

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


if __name__ == "__main__":
    runTest(LauncherShotcuts_ctrl_x.suite())
