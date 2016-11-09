#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from lib import runner,utils
from lib.launcher import *

result = True
caseid = '33832'
casename = "all-516:启动"

class LauncherStartupApp(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.startTime = time.time()
        cls.menuObj = root.application(appName='deepin-menu', description='/usr/lib/deepin-menu')
        cls.googleName = '打开新的标签页 - Google Chrome'
        cls.terminalName = 'deepin - 深度终端'
        cls.geditName = '无标题文档 1 - gedit'
        cls.oldWindows = getAllWindows()
        launcher.freeMode()

    @classmethod
    def tearDownClass(cls):
        seconds = "%.3f" % (time.time() - cls.startTime)
        minutes = utils.convertToMinutes(float(seconds))
        global result
        utils.commitresult(caseid, result, minutes)

        cls.newWindows = getAllWindows()
        if len(cls.newWindows) - len(cls.oldWindows) == 3:
            for win in cls.newWindows[-3:]:
                win.close(1)
        launcher.freeMode()


    def testSartupByRightKey(self):
        launcher.searchApp('Google Chrome')
        sleep(2)
        launcher.launcherObj.child('Google Chrome').click(3)
        if self.menuObj.children[0].name == 'DesktopMenu':
            pyautogui.press('down')
            pyautogui.press('enter')
        else:
            raise Exception("Menu did not opened!")
        win = getWindowName()
        self.assertEqual(self.googleName, win)


    def testStartupByShortcuts(self):
        launcher.searchApp('deepin-terminal')
        sleep(2)
        launcher.launcherObj.child('深度终端').click(3)
        if self.menuObj.children[0].name == 'DesktopMenu':
            pyautogui.press('o')
        else:
            raise Exception("Menu did not opened!")
        win = getWindowName()
        self.assertEqual(self.terminalName, win)


    def testStartupByLeftKey(self):
        launcher.checkLableKids('office')
        geditCoor = launcher.getAppCenterCoorCategory('office',3)
        pyautogui.click(geditCoor)
        win = getWindowName()
        self.assertEqual(self.geditName, win)


    def suite():
        suite = unittest.TestSuite()
        suite.addTest(LauncherStartupApp('testSartupByRightKey'))
        suite.addTest(LauncherStartupApp('testStartupByShortcuts'))
        suite.addTest(LauncherStartupApp('testStartupByLeftKey'))
        return suite

    class MyTestResult(runner.MyTextTestResult):
        def addError(self, test, err):
            super(LauncherStartupApp.MyTestResult, self).addError(test, err)
            global result
            result = result and False

        def addFailure(self, test, err):
            super(LauncherStartupApp.MyTestResult, self).addFailure(test, err)
            global result
            result = result and False

if __name__ == "__main__":
    unittest.TextTestRunner(resultclass=LauncherStartupApp.MyTestResult).run(LauncherStartupApp.suite())
