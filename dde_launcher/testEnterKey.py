#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from lib import executeTestCase
from lib import translation
from lib.launcher import *

result = True
casename = "all-533:launcher打开时对enter键的响应"

class LauncherEnterKey(unittest.TestCase):
    caseid = '33906'
    @classmethod
    def setUpClass(cls):
        cls.appName = 'Google Chrome'
        # cls.googleTitleName = '新标签页 - Google Chrome'
        cls.googleTittleName = translation.charTrans.getCharTrans('google-tittle-name')
        cls.oldWindows = getAllWindows()

    @classmethod
    def tearDownClass(cls):
        cls.newWindows = getAllWindows()
        if len(cls.newWindows) > len(cls.oldWindows):
            for win in cls.newWindows[len(cls.oldWindows):]:
                win.close(1)

    def testEnterKey(self):
        launcher.searchApp(self.appName)
        launcher.launcherObj.child(self.appName).point()
        pyautogui.press('enter')
        win = getWindowName()
        self.assertEqual(self.googleTitleName, win)


    def suite():
        suite = unittest.TestSuite()
        suite.addTest(LauncherEnterKey('testEnterKey'))
        return suite


if __name__ == "__main__":
    executeTestCase.runTest(LauncherEnterKey)
