#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from lib import executeTestCase
import time
from lib import runner,utils
from lib.launcher import *
from glob import glob

result = True
casename = "all-2292:鼠标右键卸载失败"

class LauncherUninstall(unittest.TestCase):
    caseid = '53249'
    @classmethod
    def setUpClass(cls):
        cls.menuObj = root.application(appName='deepin-menu', description='/usr/lib/deepin-menu')
        apps = launcher.getLauncherAllApps()
        cls.launchername = '有道词典'
        cls.appName = 'youdao-dict'
        srcfile = 'data/youdao-dict.prerm'
        destdir = '/var/lib/dpkg/info'
        cls.oldWindows = getAllWindows()
        if cls.launchername not in launcher.getLauncherAllApps():
            subprocess.check_call('sudo apt-get install -y youdao-dict', shell=True)
        subprocess.check_call('sudo cp ' + srcfile + ' ' + destdir, shell=True)



    @classmethod
    def tearDownClass(cls):
        if len(cls.newWindows) > len(cls.oldWindows):
            for win in cls.newWindows[len(cls.oldWindows):]:
                win.close(1)
        lockfile = glob('/var/lib/dpkg/lock')
        if len(lockfile) > 0:
            subprocess.check_call('sudo rm /var/lib/dpkg/lock', shell=True)
        if cls.launchername not in launcher.getLauncherAllApps():
            subprocess.check_call('sudo apt-get install -y youdao-dict', shell=True)
        cls.newWindows = getAllWindows()
        

    def testUninstallFailed(self):
        launcher.searchApp(self.launchername)
        sleep(2)
        launcher.launcherObj.child(self.launchername).click(3)
        if self.menuObj.children[0].name == 'DesktopMenu':
            for i in range(5):
                pyautogui.press('down')
                sleep(0.1)
            pyautogui.press('enter')
        else:
            raise Exception("Menu did not opened!")
        launcher.launcherObj.child('确定').click()
        launcher.exitLauncher()
        launcher.openLauncher()
        apps = launcher.getLauncherAllApps()
        self.assertIn(self.launchername, apps)

    def testOpen(self):
        launcher.searchApp(self.launchername)
        sleep(2)
        launcher.launcherObj.child(self.launchername).click()
        sleep(7)
        winname = getWindowName()
        self.assertEqual(self.launchername, winname)

    def testUninstallSuccessfully(self):
        subprocess.check_call('sudo rm /var/lib/dpkg/info/youdao-dict.prerm', shell=True)
        launcher.searchApp(self.launchername)
        sleep(2)
        launcher.launcherObj.child(self.launchername).click(3)
        if self.menuObj.children[0].name == 'DesktopMenu':
            for i in range(5):
                pyautogui.press('down')
                sleep(0.1)
            pyautogui.press('enter')
        else:
            raise Exception("Menu did not opened!")
        launcher.launcherObj.child('确定').click()
        launcher.exitLauncher()
        sleep(5)
        launcher.openLauncher()
        launcher.exitLauncher()
        apps = launcher.getLauncherAllApps()
        self.assertNotIn(self.launchername, apps)
        print ('Uninstall %s successeful' % self.launchername)

    def suite():
        suite = unittest.TestSuite()
        suite.addTest(LauncherUninstall('testUninstallFailed'))
        suite.addTest(LauncherUninstall('testOpen'))
        suite.addTest(LauncherUninstall('testUninstallSuccessfully'))
        return suite


if __name__ == "__main__":
    executeTestCase.runTest(LauncherUninstall)
