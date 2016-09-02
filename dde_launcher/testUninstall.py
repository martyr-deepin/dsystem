#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from lib import runner,utils
from lib.launcher import *

result = True

class LauncherUninstall(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.caseid = '33849'
        cls.casename = "all-521:鼠标右键卸载"
        cls.menuObj = root.application(appName='deepin-menu', description='/usr/lib/deepin-menu')
        apps = launcher.getLauncherAllApps()
        cls.appName = apps[17]
        print ('Ready to uninstall %s' % cls.appName)

    @classmethod
    def tearDownClass(cls):
        global result
        utils.commitresult(cls.caseid, result)
        launcher.exitLauncher()
    
    def testNotUninstall(self):
        launcher.openLauncher()
        launcher.launcherObj.child(self.appName).click(3)
        if self.menuObj.children[0].name == 'DesktopMenu':
            for i in range(5):
                pyautogui.press('down')
                sleep(0.1)
            pyautogui.press('enter')
        else:
            raise Exception("Menu did not opened!")
        launcher.launcherObj.child('取消').click()
        apps = launcher.getLauncherAllApps()
        self.assertIn(self.appName, apps)


    def testUninstall(self):
        launcher.launcherObj.child(self.appName).click(3)
        if self.menuObj.children[0].name == 'DesktopMenu':
            for i in range(5):
                pyautogui.press('down')
                sleep(0.1)
            pyautogui.press('enter')
        else:
            raise Exception("Menu did not opened!")
        launcher.launcherObj.child('确定').click()
        sleep(2)
        apps = launcher.getLauncherAllApps()
        self.assertNotIn(self.appName, apps)
        print ('Uninstall %s successeful' % self.appName)

    def suite():
        suite = unittest.TestSuite()
        suite.addTest(LauncherUninstall('testNotUninstall'))
        suite.addTest(LauncherUninstall('testUninstall'))
        return suite

    class MyTestResult(runner.MyTextTestResult):
        def addError(self, test, err):
            super(LauncherUninstall.MyTestResult, self).addError(test, err)
            global result
            result = result and False

        def addFailure(self, test, err):
            super(LauncherUninstall.MyTestResult, self).addFailure(test, err)
            global result
            result = result and False

if __name__ == "__main__":
    unittest.TextTestRunner(resultclass=LauncherUninstall.MyTestResult).run(LauncherUninstall.suite())
