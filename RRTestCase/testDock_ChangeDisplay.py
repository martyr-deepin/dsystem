#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import time
import gettext
import unittest
import pyautogui
from lib import DaemonDock
from lib import runTest
from lib import properties
from lib import utils

casename = "all-5348:切换dock模式"

class Dock_ChangeDisplay(unittest.TestCase):
    caseid = '191637'

    @classmethod
    def setUpClass(cls):
        cls.daemondock = DaemonDock()
        cls.olddisplaymode = cls.daemondock.getDisplayMode()
        cls.dockp = properties.dockClass()

    @classmethod
    def tearDownClass(cls):
        cls.daemondock.setDisplayMode(cls.olddisplaymode)

    def testChangeDisplay(self):
        self.assertTrue(self.dockp.displaymode_fashion ==
                self.daemondock.getDisplayMode())

        curposition = self.daemondock.getPosition()

        if curposition == self.dockp.position_bottom:
            menuxy = utils.getScreenMiddle('bottom')
            utils.m.click(menuxy[0], menuxy[1], 2)
            time.sleep(2)
            pyautogui.press('down')
            pyautogui.press('right')
            pyautogui.press('down')
            pyautogui.press('enter')
            time.sleep(2)
            self.assertTrue(self.dockp.displaymode_efficient ==
                    self.daemondock.getDisplayMode())

            rect = self.daemondock.getFrontendWindowRect()
            print(rect)
            self.assertTrue(0 == rect[0])
            self.assertTrue(utils.resolution.width == rect[2])
            self.assertTrue(utils.resolution.height == (rect[1] + rect[3]))

    def suite():
        suite = unittest.TestSuite()
        suite.addTest(Dock_ChangeDisplay('testChangeDisplay'))
        return suite

if __name__ == "__main__":
    unittest.installHandler()
    LOCALE_DIR = os.path.abspath("./lib/locale")
    gettext.install('dsystem', LOCALE_DIR)
    runTest(Dock_ChangeDisplay)
