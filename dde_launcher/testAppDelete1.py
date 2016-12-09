#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from lib import executeTestCase
import time
from lib import runner,utils
from lib.launcher import *
from lib.dde_dock import *

result = True
caseid = '80062'
casename = "all-3296:应用发送至任务栏/桌面后右键删除测试"

class AppDelete1(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = 'deepin-feedback'
        cls.desktopfile = 'deepin-feedback.desktop'
        cls.launchername = '深度用户反馈'


    @classmethod
    def tearDownClass(cls):
        if cls.launchername not in launcher.getLauncherAllApps():
            subprocess.check_call('sudo apt-get install -y deepin-feedback', shell=True)

    def testSendToDesktop(self):
        launcher.menuDesktop(self.launchername)
        desktopFiles = getDesktopFiles()
        self.assertIn(self.desktopfile,desktopFiles)

    def testSendToDock(self):
        launcher.menuDock(self.launchername)
        dockApps = Dock().getAllDockApps()
        self.assertIn(self.app,dockApps)

    def testDeleteFromDesktop(self):
        launcher.menuUninstall(self.launchername)
        sleep(5)
        desktopFiles = getDesktopFiles()
        self.assertNotIn(self.desktopfile,desktopFiles)

    def testDeleteFromDock(self):
        dockApps = Dock().getAllDockApps()
        self.assertNotIn(self.app,dockApps)

    def suite():
        suite = unittest.TestSuite()
        suite.addTest(AppDelete1('testSendToDesktop'))
        suite.addTest(AppDelete1('testSendToDock'))
        suite.addTest(AppDelete1('testDeleteFromDesktop'))
        suite.addTest(AppDelete1('testDeleteFromDock'))
        return suite


if __name__ == "__main__":
    runTest(AppDelete1.suite())
