#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import gettext
import unittest
from lib import DaemonDock
from lib import runTest
from lib import properties

casename = "all-5337:检查dock默认显示模式、位置、大小、状态"

class Dock_DefaultSetting(unittest.TestCase):
    caseid = '191614'

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def testDefaultSetting(self):
        daemondock = DaemonDock()
        rect = daemondock.getFrontendWindowRect()

        dockp = properties.dockClass()

        self.assertTrue(dockp.displaymode_fashion == daemondock.getDisplayMode())
        self.assertTrue(dockp.hidemode_keepshowing == daemondock.getHideMode())
        self.assertTrue(dockp.hidestate_show == daemondock.getHideState())
        self.assertTrue(dockp.iconsize_medium == daemondock.getIconSize())
        self.assertTrue(dockp.position_bottom == daemondock.getPosition())

    def suite():
        suite = unittest.TestSuite()
        suite.addTest(Dock_DefaultSetting('testDefaultSetting'))
        return suite

if __name__ == "__main__":
    unittest.installHandler()
    LOCALE_DIR = os.path.abspath("./lib/locale")
    gettext.install('dsystem', LOCALE_DIR)
    runTest(Dock_DefaultSetting)
