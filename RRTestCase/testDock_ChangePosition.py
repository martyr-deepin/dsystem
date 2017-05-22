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

casename = "all-5349:切换dock位置"

class Dock_ChangePosition(unittest.TestCase):
    caseid = '191639'

    @classmethod
    def setUpClass(cls):
        cls.daemondock = DaemonDock()
        cls.oldposition = cls.daemondock.getPosition()
        cls.dockp = properties.dockClass()

    @classmethod
    def tearDownClass(cls):
        cls.daemondock.setPosition(cls.oldposition)

    def testChangePosition(self):
        self.assertTrue(self.dockp.position_bottom ==
                self.oldposition)

        curposition = self.daemondock.getPosition()

        if curposition == self.dockp.position_bottom:
            # to top
            menuxy = utils.getScreenMiddle('bottom')
            utils.m.click(menuxy[0], menuxy[1], 2)
            time.sleep(2)
            pyautogui.press('down')
            pyautogui.press('down')
            pyautogui.press('right')
            pyautogui.press('enter')
            time.sleep(2)
            self.assertTrue(self.dockp.position_top ==
                    self.daemondock.getPosition())

            rect = self.daemondock.getFrontendWindowRect()
            print(rect)
            self.assertTrue(0 == rect[1])

            # to left
            menuxy = utils.getScreenMiddle('top')
            utils.m.click(menuxy[0], menuxy[1], 2)
            time.sleep(2)
            pyautogui.press('down')
            pyautogui.press('down')
            pyautogui.press('right')
            pyautogui.press('down')
            pyautogui.press('down')
            pyautogui.press('enter')
            time.sleep(2)
            self.assertTrue(self.dockp.position_left ==
                    self.daemondock.getPosition())

            rect = self.daemondock.getFrontendWindowRect()
            print(rect)
            self.assertTrue(0 == rect[0])

            # to right 
            menuxy = utils.getScreenMiddle('left')
            utils.m.click(menuxy[0], menuxy[1], 2)
            time.sleep(2)
            pyautogui.press('down')
            pyautogui.press('down')
            pyautogui.press('right')
            pyautogui.press('down')
            pyautogui.press('down')
            pyautogui.press('down')
            pyautogui.press('enter')
            time.sleep(2)
            self.assertTrue(self.dockp.position_right ==
                    self.daemondock.getPosition())

            rect = self.daemondock.getFrontendWindowRect()
            print(rect)
            self.assertTrue(utils.resolution.width == int(rect[0] + rect[2]))

    def suite():
        suite = unittest.TestSuite()
        suite.addTest(Dock_ChangePosition('testChangePosition'))
        return suite

if __name__ == "__main__":
    unittest.installHandler()
    LOCALE_DIR = os.path.abspath("./lib/locale")
    gettext.install('dsystem', LOCALE_DIR)
    runTest(Dock_ChangePosition)
