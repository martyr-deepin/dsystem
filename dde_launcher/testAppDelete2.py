#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from lib import executeTestCase
import time
from lib import runner,utils
from lib.launcher import *
from lib.dde_dock import *
from glob import glob

result = True
caseid = '80064'
casename = "all-3297:应用发送至任务栏/桌面后命令行删除测试"

class AppDelete2(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = 'lovewallpaper'
        cls.launchername = '爱壁纸HD'
        cls.desktopfile = 'love-wallpaper.desktop'
        cls.dockname = 'love-wallpaper'
        cls.install = 'sudo apt-get -y install ' + cls.app
        cls.remove = 'sudo apt-get -y remove ' + cls.app
        lockfile = glob('/var/lib/dpkg/lock')
        if len(lockfile) > 0:
            subprocess.check_call('sudo rm /var/lib/dpkg/lock', shell=True)

    @classmethod
    def tearDownClass(cls):
        pass

    def testSendToDesktopAndDock(self):
        subprocess.check_call(self.install, shell=True)
        launcher.menuDesktop(self.launchername)
        launcher.menuDock(self.launchername)
        desktopFiles = getDesktopFiles()
        self.assertIn(self.desktopfile,desktopFiles)
        dockApps = Dock().getAllDockApps()
        self.assertIn(self.dockname,dockApps)

    def testRemoveResult(self):
        subprocess.check_call(self.remove, shell=True)
        launcher.exitLauncher()
        desktopFiles = getDesktopFiles()
        self.assertNotIn(self.desktopfile,desktopFiles)
        dockApps = Dock().getAllDockApps()
        self.assertNotIn(self.dockname,dockApps)

    def suite():
        suite = unittest.TestSuite()
        suite.addTest(AppDelete2('testSendToDesktopAndDock'))
        suite.addTest(AppDelete2('testRemoveResult'))
        return suite


if __name__ == "__main__":
    runTest(AppDelete2.suite())
