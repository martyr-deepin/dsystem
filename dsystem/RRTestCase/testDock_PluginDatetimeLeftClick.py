#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import gettext
import unittest
import pyautogui
from time import sleep
from lib import executeTestCase
from lib import utils
from lib import runner
from lib import Dock
from lib import Dde_control_center
from lib import window

casename = 'all-6240:时间插件-左键'

class Dock_PluginDatetimeLeftClick(unittest.TestCase):
    caseid = '283437'
    @classmethod
    def setUpClass(cls):
        cls.testiconname = "datetime-"
        cls.dock = Dock()
        cls.ddecontrolcenter = Dde_control_center()

        if utils.dock.displaymode_fashion != utils.getDdeDockDisplayMode():
            utils.setDdeDockDisplayMode(utils.dock.displaymode_fashion)

        if utils.dock.position_bottom != utils.getDdeDockPosition():
            utils.setDdeDockPosition(utils.dock.position_bottom)

    @classmethod
    def tearDownClass(cls):
        if utils.dock.displaymode_fashion != utils.getDdeDockDisplayMode():
            utils.setDdeDockDisplayMode(utils.dock.displaymode_fashion)

        if utils.dock.position_bottom != utils.getDdeDockPosition():
            utils.setDdeDockPosition(utils.dock.position_bottom)

    def testPluginDatetimeLeftClick(self):
        icon = self.dock.dockObj.child(self.testiconname)
        self.assertTrue(icon)
        icon.click()
        sleep(2)

        deepin_calendar = "Deepin Calendar"
        w = window.findWindow(deepin_calendar)
        self.assertTrue(w != None)
        window.closeWindow(w)
        w = window.findWindow(deepin_calendar, mode="nowait")
        self.assertTrue(w == None)

        pyautogui.moveTo(400, 400, duration=1)
        pyautogui.click()

    def suite():
        suite = unittest.TestSuite()
        suite.addTest(Dock_PluginDatetimeLeftClick('testPluginDatetimeLeftClick'))
        return suite

if __name__ == "__main__":
    unittest.installHandler()
    LOCALE_DIR = os.path.abspath("./lib/locale")
    gettext.install('dsystem', LOCALE_DIR)
    executeTestCase.runTest(Dock_PluginDatetimeLeftClick)
