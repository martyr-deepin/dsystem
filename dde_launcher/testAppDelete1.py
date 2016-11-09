#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from lib import runner,utils
from lib.launcher import *
from lib.dde_dock import *

result = True
caseid = '80062'
casename = "all-3296:应用发送至任务栏/桌面后右键删除测试"

class AppDelete1(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.startTime = time.time()
        cls.app = '360safeforcnos'
        cls.launchername = '360安全卫士'
        cls.desktopfile = 'start360.desktop'
        cls.dockname = 'start360'
        cls.install = 'sudo apt-get -y install ' + cls.app
        cls.remove = 'sudo apt-get -y remove ' + cls.app

    @classmethod
    def tearDownClass(cls):
        seconds = "%.3f" % (time.time() - cls.startTime)
        minutes = utils.convertToMinutes(float(seconds))
        global result
        utils.commitresult(caseid, result, minutes)

    def testSendToDesktopAndDock(self):
        subprocess.check_call(self.install, shell=True)
        launcher.menuDesktop(self.launchername)
        launcher.menuDock(self.launchername)
        desktopFiles = getDesktopFiles()
        self.assertIn(self.desktopfile,desktopFiles)
        dockApps = Dock().getAllDockApps()
        self.assertIn(self.dockname,dockApps)

    def testRemoveResult(self):
        launcher.openLauncher()
        launcher.searchApp(self.launchername)
        launcher.launcherObj.child(self.launchername).click(3)
        menuObj = root.application(appName='deepin-menu', description='/usr/lib/deepin-menu')
        print(menuObj.children)
        if menuObj.children[0].name == 'DesktopMenu':
            for i in range(5):
                pyautogui.press('down')
                sleep(0.1)
            pyautogui.press('enter')
            launcher.launcherObj.child('确定').click()
            launcher.exitLauncher()
        else:
            raise Exception("Menu did not opened!")
        sleep(2)
        desktopFiles = getDesktopFiles()
        self.assertNotIn(self.desktopfile,desktopFiles)
        dockApps = Dock().getAllDockApps()
        self.assertNotIn(self.dockname,dockApps)

    def suite():
        suite = unittest.TestSuite()
        suite.addTest(AppDelete1('testSendToDesktopAndDock'))
        suite.addTest(AppDelete1('testRemoveResult'))
        return suite

    class MyTestResult(runner.MyTextTestResult):
        def addError(self, test, err):
            super(AppDelete1.MyTestResult, self).addError(test, err)
            global result
            result = result and False

        def addFailure(self, test, err):
            super(AppDelete1.MyTestResult, self).addFailure(test, err)
            global result
            result = result and False

if __name__ == "__main__":
    unittest.TextTestRunner(resultclass=AppDelete1.MyTestResult).run(AppDelete1.suite())
