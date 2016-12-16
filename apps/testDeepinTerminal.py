#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import unittest
from lib import executeTestCase
from lib import runner,utils
from lib.launcher import *


result = True
casename = 'all-3358:运行深度终端'

class DeepinTerminal(unittest.TestCase):
    caseid = '83378'
    @classmethod
    def setUpClass(cls):
        cls.appName = 'deepin-terminal'
        status, cls.username = subprocess.getstatusoutput("whoami")
        cls.winName = cls.username + ' - 深度终端'
        cls.oldWindows = getAllWindows()


    @classmethod
    def tearDownClass(cls):
        if len(newWindows) > len(cls.oldWindows):
            for win in newWindows[len(cls.oldWindows):]:
                win.close(1)

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

if __name__ == "__main__":
    executeTestCase.runTest(DeepinTerminal)
