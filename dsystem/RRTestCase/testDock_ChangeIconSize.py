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

casename = "all-5350:切换dock大小"

class Dock_ChangeIconSize(unittest.TestCase):
    caseid = '191641'

    @classmethod
    def setUpClass(cls):
        cls.daemondock = DaemonDock()
        cls.oldiconsize = cls.daemondock.getIconSize()
        cls.dockp = properties.dockClass()

    @classmethod
    def tearDownClass(cls):
        cls.daemondock.setIconSize(cls.oldiconsize)

    def testChangeIconSize(self):
        self.assertTrue(self.dockp.iconsize_medium ==
                self.daemondock.getIconSize())

        curposition = self.daemondock.getPosition()

        if curposition == self.dockp.position_bottom:
            # to large
            menuxy = utils.getScreenMiddle('bottom')
            utils.m.click(menuxy[0], menuxy[1], 2)
            time.sleep(2)
            pyautogui.press('down')
            pyautogui.press('down')
            pyautogui.press('down')
            pyautogui.press('right')
            pyautogui.press('enter')
            time.sleep(2)
            self.assertTrue(self.dockp.iconsize_large ==
                    self.daemondock.getIconSize())

            # to medium 
            menuxy = utils.getScreenMiddle('bottom')
            utils.m.click(menuxy[0], menuxy[1], 2)
            time.sleep(2)
            pyautogui.press('down')
            pyautogui.press('down')
            pyautogui.press('down')
            pyautogui.press('right')
            pyautogui.press('down')
            pyautogui.press('enter')
            time.sleep(2)
            self.assertTrue(self.dockp.iconsize_medium ==
                    self.daemondock.getIconSize())

            # to small
            menuxy = utils.getScreenMiddle('bottom')
            utils.m.click(menuxy[0], menuxy[1], 2)
            time.sleep(2)
            pyautogui.press('down')
            pyautogui.press('down')
            pyautogui.press('down')
            pyautogui.press('right')
            pyautogui.press('down')
            pyautogui.press('down')
            pyautogui.press('enter')
            time.sleep(2)
            self.assertTrue(self.dockp.iconsize_small ==
                    self.daemondock.getIconSize())

    def suite():
        suite = unittest.TestSuite()
        suite.addTest(Dock_ChangeIconSize('testChangeIconSize'))
        return suite

if __name__ == "__main__":
    unittest.installHandler()
    LOCALE_DIR = os.path.abspath("./lib/locale")
    gettext.install('dsystem', LOCALE_DIR)
    runTest(Dock_ChangeIconSize)
