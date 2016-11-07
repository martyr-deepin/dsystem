#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from lib import runner,utils
from lib.launcher import *
from lib.dde_dock import *

result = True
caseid = '33859'
casename = "all-523:右键菜单快捷键测试"

class LauncherShotcuts(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.menuObj = root.application(appName='deepin-menu', description='/usr/lib/deepin-menu')
        launcher.categoryMode()
        cls.appObj = launcher.launcherObj.child('internet',roleName='list').children[0]
        cls.googleTitleName = '打开新的标签页 - Google Chrome'
        cls.appDesktopName = 'google-chrome.desktop'
        cls.oldWindows = getAllWindows()
        dockApps = Dock().getAllDockApps()
        if 'google-chrome' in dockApps:
            Dock().unDockApp('Google Chrome')

    @classmethod
    def tearDownClass(cls):
        global result
        utils.commitresult(caseid, result)
        #remove from desktop
        desktopFiles = getDesktopFiles()
        if cls.appDesktopName in desktopFiles:
            launcher.launcherObj.child('internet',roleName='list').children[0].click(3)
            if cls.menuObj.children[0].name == 'DesktopMenu':
                pyautogui.press('down')
                pyautogui.press('down')
                pyautogui.press('enter')
            else:
                raise Exception('Launcher Menu did not opened!')
        #remove from dock
        dockApps = Dock().getAllDockApps()
        if 'google-chrome' not in dockApps:
            launcher.launcherObj.child('internet',roleName='list').children[0].click(3)
            if cls.menuObj.children[0].name == 'DesktopMenu':
                pyautogui.press('down')
                pyautogui.press('down')
                pyautogui.press('down')
                pyautogui.press('enter')
            else:
                raise Exception('Launcher Menu did not opened!')

        launcher.launcherObj.child('mode-toggle-button').click()
        launcher.exitLauncher()
        #close google
        cls.newWindows = getAllWindows()
        if len(cls.newWindows) - len(cls.oldWindows) == 1:
            cls.newWindows[-1].close(1)
        launcher.freeMode()

    def testOpen(self):
        pyautogui.press('winleft')
        mode = launcher.getLauncherMode()
        if mode == '\'free\'':
            launcher.launcherObj.child('mode-toggle-button').click()
        self.appObj.click(3)
        if self.menuObj.children[0].name == 'DesktopMenu':
            pyautogui.press('o')
        else:
            raise Exception("Menu did not opened!")
        win = getWindowName()
        self.assertEqual(self.googleTitleName, win)


    def testSendToDesktop(self):
        win = findWindow('dde-launcher')
        mode = launcher.getLauncherMode()
        if win == None:
            pyautogui.press('winleft')
        if mode == '\'free\'':
            launcher.launcherObj.child('mode-toggle-button').click()
        self.appObj.click(3)
        if self.menuObj.children[0].name == 'DesktopMenu':
            pyautogui.press('e')
        else:
            raise Exception("Menu did not opened!")
        desktopFiles = getDesktopFiles()
        self.assertIn(self.appDesktopName,desktopFiles)

    def testSendToDock(self):
        win = findWindow('dde-launcher')
        mode = launcher.getLauncherMode()
        if win == None:
            pyautogui.press('winleft')
        if mode == '\'free\'':
            launcher.launcherObj.child('mode-toggle-button').click()
        self.appObj.click(3)
        if self.menuObj.children[0].name == 'DesktopMenu':
            pyautogui.press('c')
        else:
            raise Exception("Menu did not opened!")
        dockApps = Dock().getAllDockApps()
        self.assertIn('google-chrome',dockApps)

    def testAddBoot(self):
        win = findWindow('dde-launcher')
        mode = launcher.getLauncherMode()
        if win == None:
            pyautogui.press('winleft')
        if mode == '\'free\'':
            launcher.launcherObj.child('mode-toggle-button').click()
        self.appObj.click(3)
        if self.menuObj.children[0].name == 'DesktopMenu':
            pyautogui.press('a')
        else:
            raise Exception("Menu did not opened!")
        googleFeild = getBootFeild(self.appDesktopName)
        self.assertEqual('Hidden=false',googleFeild)

    def testCancleBoot(self):
        win = findWindow('dde-launcher')
        mode = launcher.getLauncherMode()
        if win == None:
            pyautogui.press('winleft')
        if mode == '\'free\'':
            launcher.launcherObj.child('mode-toggle-button').click()
        self.appObj.click(3)
        if self.menuObj.children[0].name == 'DesktopMenu':
            pyautogui.press('r')
        else:
            raise Exception("Menu did not opened!")
        googleFeild = getBootFeild(self.appDesktopName)
        self.assertEqual('Hidden=true',googleFeild)

    def suite():
        suite = unittest.TestSuite()
        suite.addTest(LauncherShotcuts('testOpen'))
        suite.addTest(LauncherShotcuts('testSendToDesktop'))
        suite.addTest(LauncherShotcuts('testSendToDock'))
        suite.addTest(LauncherShotcuts('testAddBoot'))
        suite.addTest(LauncherShotcuts('testCancleBoot'))
        return suite

    class MyTestResult(runner.MyTextTestResult):
        def addError(self, test, err):
            super(LauncherShotcuts.MyTestResult, self).addError(test, err)
            global result
            result = result and False

        def addFailure(self, test, err):
            super(LauncherShotcuts.MyTestResult, self).addFailure(test, err)
            global result
            result = result and False

if __name__ == "__main__":
    unittest.TextTestRunner(resultclass=LauncherShotcuts.MyTestResult).run(LauncherShotcuts.suite())
