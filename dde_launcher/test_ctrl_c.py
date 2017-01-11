#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from lib import executeTestCase
from lib.launcher import *
from time import sleep

result = True
casename = "all-2103:搜索框快捷键测试-ctrl+c"

class LauncherShotcuts_ctrl_c(unittest.TestCase):
    caseid = '45345'
    @classmethod
    def setUpClass(cls):
        cls.text = '深度商店'


    @classmethod
    def tearDownClass(cls):
        pass

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


if __name__ == "__main__":
    executeTestCase.runTest(LauncherShotcuts_ctrl_c)
