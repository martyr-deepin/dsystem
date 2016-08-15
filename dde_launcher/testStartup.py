#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from lib import runner,utils,window
from lib.launcher import *

result = True

class MyTestResult(runner.MyTextTestResult):
    def addError(self, test, err):
        super(MyTestResult, self).addError(test, err)
        global result
        result = result and False

    def addFailure(self, test, err):
        super(MyTestResult, self).addFailure(test, err)
        global result
        result = result and False

class LauncherStartupApp(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.caseid = '33832'
        cls.casename = "all-516:启动"
        cls.menuObj = root.application(appName='deepin-menu', description='/usr/lib/deepin-menu')
        cls.googleName = '打开新的标签页 - Google Chrome'
        cls.terminalName = '深度终端'
        cls.musicName = '深度音乐'

    @classmethod
    def tearDownClass(cls):
        global result
        utils.commitresult(cls.caseid, result)

    def testSartupByRightKey(self):
        pyautogui.press('winleft')
        launcher.launcherObj.child('Google Chrome').click(3)
        if self.menuObj.children[0].name == 'DesktopMenu':
            pyautogui.press('down')
            pyautogui.press('enter')
        else:
            raise Exception("Menu did not opened!")
        google = findWindow(self.googleName)
        self.assertIsNotNone(google)
        closeWindow(google)

    def testStartupByShortcuts(self):
        pyautogui.press('winleft')
        launcher.launcherObj.child('深度音乐').click(3)
        if self.menuObj.children[0].name == 'DesktopMenu':
            pyautogui.press('o')
        else:
            raise Exception("Menu did not opened!")
        terminal = findWindow(self.terminalName)
        self.assertIsNotNone(terminal)
        closeWindow(terminal)

    def testStartupByLeftKey(self):
        pyautogui.press('winleft')
        launcher.launcherObj.child('深度终端').click()
        music = findWindow(self.musicName)
        self.assertIsNotNone(music)
        closeWindow(music)

def suite():
    suite = unittest.TestSuite()
    suite.addTest(LauncherStartupApp('testSartupByRightKey'))
    suite.addTest(LauncherStartupApp('testStartupByShortcuts'))
    suite.addTest(LauncherStartupApp('testStartupByLeftKey'))
    return suite

if __name__ == "__main__":
    unittest.TextTestRunner(verbosity=1).run(suite())
