#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import gettext
import unittest
from lib import runTest
from lib import Launcher
from lib import Dock
from lib import utils

result = True
casename = 'all-5344:发送应用到桌面'

class Launcher_SendToDesktop(unittest.TestCase):
    caseid = '191629'
    @classmethod
    def setUpClass(cls):
        cls.dock = Dock()
        cls.launcher = Launcher()

    @classmethod
    def tearDownClass(cls):
        cls.launcher.exitLauncher()
        cmdstr = 'rm ~/Desktop/' + cls.dock.DesktopFile_Deepin_Music
        os.system(cmdstr)

    def testMenuSendToDesktop(self):
        self.launcher.menuDesktop(self.dock.string_Deepin_Music)
        desktopFiles = utils.getDesktopFiles()
        self.assertIn(self.dock.DesktopFile_Deepin_Music, desktopFiles)

    def suite():
        suite = unittest.TestSuite()
        suite.addTest(Launcher_SendToDesktop('testMenuSendToDesktop'))
        return suite


if __name__ == "__main__":
    unittest.installHandler()
    LOCALE_DIR = os.path.abspath("./lib/locale")
    gettext.install('dsystem', LOCALE_DIR)
    runTest(Launcher_SendToDesktop)
