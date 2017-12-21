#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import gettext
import unittest
from lib import runTest 
from lib import Launcher
from lib import Dock

casename = 'all-5346:将应用添加至开机自启动'

class Launcher_AutoStart(unittest.TestCase):
    caseid = '191633'
    @classmethod
    def setUpClass(cls):
        cls.launcher = Launcher()
        cls.dock = Dock()
        cls.googleName = cls.dock.string_Google_Chrome
        cls.QQname = cls.dock.string_QQ
        cls.googleFile = cls.dock.DesktopFile_Google_Chrome
        cls.QQFile = cls.dock.DesktopFile_QQ
        cls.launcher.freeMode()

    @classmethod
    def tearDownClass(cls):
        googleFeild = cls.launcher.getBootFeild(cls.googleFile)
        QQFeild = cls.launcher.getBootFeild(cls.QQFile)
        if googleFeild == 'Hidden=false':
            cls.launcher.menuBoot(cls.googleName)
            cls.launcher.exitLauncher()
        if QQFeild == 'Hidden=false':
            self.launcher.menuBoot(cls.QQname)
            self.launcher.exitLauncher()


    def testMenuAutoStart(self):
        self.launcher.menuBoot(self.googleName, self.QQname)
        #launcher.exitLauncher()
        googleFeild = self.launcher.getBootFeild(self.googleFile)
        QQFeild = self.launcher.getBootFeild(self.QQFile)
        self.assertEqual('Hidden=false',googleFeild)
        self.assertEqual('Hidden=false',QQFeild)

    def testMenuRemoveFromBoot(self):
        self.launcher.menuBoot(self.googleName, self.QQname)
        #launcher.exitLauncher()
        QQFeild = self.launcher.getBootFeild(self.QQFile)
        self.assertEqual('Hidden=true',QQFeild)


    def suite():
        suite = unittest.TestSuite()
        suite.addTest(Launcher_AutoStart('testMenuAutoStart'))
        suite.addTest(Launcher_AutoStart('testMenuRemoveFromBoot'))
        return suite

if __name__ == "__main__":
    unittest.installHandler()
    LOCALE_DIR = os.path.abspath("./lib/locale")
    gettext.install('dsystem', LOCALE_DIR)
    runTest(Launcher_AutoStart)
