#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import time
import gettext
import unittest
import pyautogui
from lib import DaemonDock
from lib import DdeDock
from lib import runTest
from lib import properties
from lib import utils
from lib import DbusLauncher
from lib import DdeDock

casename = "all-6197:dock自动显示"

class Dock_AutoDisplay(unittest.TestCase):
    caseid = '280071'

    @classmethod
    def setUpClass(cls):
        cls.ddedock = DdeDock()
        cls.daemondock = DaemonDock()
        cls.oldhidemode = cls.daemondock.getHideMode()
        cls.oldhidestate = cls.daemondock.getHideState()
        cls.dockp = properties.dockClass()
        cls.dbus_launcher = DbusLauncher()

    @classmethod
    def tearDownClass(cls):
        cls.daemondock.setHideMode(cls.oldhidemode)
        cls.dbus_launcher.Hide()

    def testChangeHideToKeepHidden(self):
        self.daemondock.setHideMode(self.dockp.hidemode_keephidden)
        geometry = self.ddedock.getgeometry()
        self.assertTrue(geometry[3] == 2)
        self.dbus_launcher.Show()
        geometry = self.ddedock.getgeometry()
        self.assertTrue(geometry[3] > 2)

    def suite():
        suite = unittest.TestSuite()
        suite.addTest(Dock_AutoDisplay('testChangeHideToKeepHidden'))
        return suite

if __name__ == "__main__":
    unittest.installHandler()
    LOCALE_DIR = os.path.abspath("./lib/locale")
    gettext.install('dsystem', LOCALE_DIR)
    runTest(Dock_AutoDisplay)
