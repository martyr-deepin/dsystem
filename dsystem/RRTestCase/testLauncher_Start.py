#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import gettext
import unittest
from lib import Dock, Launcher
from lib import DbusLauncher
from lib import runTest

casename = "all-6109:启动launcher检测"

class Launcher_Start(unittest.TestCase):
    caseid = '268816'

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def testClickLauncher(self):
        #dock = Dock()
        #dock.dockObj.child(dock.string_dock_Launcher).click()
        
        dbusLauncher = DbusLauncher()
        dbusLauncher.Show()
        launcher = Launcher()
        self.assertTrue(launcher.launcherObj)
        dbusLauncher.Hide()

    def suite():
        suite = unittest.TestSuite()
        suite.addTest(Launcher_Start('testClickLauncher'))
        return suite

if __name__ == "__main__":
    unittest.installHandler()
    LOCALE_DIR = os.path.abspath("./lib/locale")
    gettext.install('dsystem', LOCALE_DIR)
    runTest(Launcher_Start)
