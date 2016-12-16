#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import unittest
from lib import executeTestCase
import time
from lib import runner,utils
from lib.launcher import *
from lib.dde_dock import *

result = True
casename = 'all-520:发送到桌面'

class LauncherSendToDesktop(unittest.TestCase):
    caseid = '33846'
    @classmethod
    def setUpClass(cls):
        cls.menuObj = root.application(appName='deepin-menu', description='/usr/lib/deepin-menu')
        cls.QQName = 'QQ'

    @classmethod
    def tearDownClass(cls):
        launcher.exitLauncher()

    def testMenuSendToDesktop(self):
        launcher.menuDesktop(self.QQName)
        desktopFiles = getDesktopFiles()
        QQdesktopFile = 'apps.com.qq.im.desktop'
        self.assertIn(QQdesktopFile,desktopFiles)

    def suite():
        suite = unittest.TestSuite()
        suite.addTest(LauncherSendToDesktop('testMenuSendToDesktop'))
        return suite


if __name__ == "__main__":
    executeTestCase.runTest(LauncherSendToDesktop)
