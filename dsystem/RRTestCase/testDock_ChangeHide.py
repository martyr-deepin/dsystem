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

casename = "all-5351:切换dock状态"

class Dock_ChangeHide(unittest.TestCase):
    caseid = '191643'

    @classmethod
    def setUpClass(cls):
        cls.ddedock = DdeDock()
        cls.daemondock = DaemonDock()
        cls.oldhidemode = cls.daemondock.getHideMode()
        cls.oldhidestate = cls.daemondock.getHideState()
        cls.dockp = properties.dockClass()

    @classmethod
    def tearDownClass(cls):
        cls.daemondock.setHideMode(cls.oldhidemode)

    def testChangeHide(self):
        self.assertTrue(self.dockp.hidemode_keepshowing ==
                self.daemondock.getHideMode())
        self.assertTrue(self.dockp.hidestate_show ==
                self.daemondock.getHideState())

        curposition = self.daemondock.getPosition()

        if curposition == self.dockp.position_bottom:
            menuxy = utils.getScreenMiddle('bottom')
            utils.m.click(menuxy[0], menuxy[1], 2)
            time.sleep(2)
            pyautogui.press('down')
            pyautogui.press('down')
            pyautogui.press('down')
            pyautogui.press('down')
            pyautogui.press('right')
            pyautogui.press('down')
            pyautogui.press('enter')
            utils.m.move(100, 100)
            time.sleep(2)
            self.assertTrue(self.dockp.hidemode_keephidden ==
                    self.daemondock.getHideMode())
            self.assertTrue(self.dockp.hidestate_hide ==
                    self.daemondock.getHideState())

            rect = self.ddedock.getgeometry()
            print(rect)
            self.assertTrue((utils.resolution.height - 2) <= rect[1])

    def suite():
        suite = unittest.TestSuite()
        suite.addTest(Dock_ChangeHide('testChangeHide'))
        return suite

if __name__ == "__main__":
    unittest.installHandler()
    LOCALE_DIR = os.path.abspath("./lib/locale")
    gettext.install('dsystem', LOCALE_DIR)
    runTest(Dock_ChangeHide)
