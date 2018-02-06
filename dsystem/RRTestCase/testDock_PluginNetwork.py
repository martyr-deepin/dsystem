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
from lib import Dock
from lib import DaemonNetwork

casename = "all-6201:网络插件隐藏和显示"

class Dock_PluginNetwork(unittest.TestCase):
    caseid = '280135'

    @classmethod
    def setUpClass(cls):
        cls.dock = Dock()
        cls.ddedock = DdeDock()
        cls.daemondock = DaemonDock()
        cls.oldhidemode = cls.daemondock.getHideMode()
        cls.oldhidestate = cls.daemondock.getHideState()
        cls.dockp = properties.dockClass()
        cls.daemonnetwork = DaemonNetwork()
        cls.device = cls.daemonnetwork.getActiveDevices()

    @classmethod
    def tearDownClass(cls):
        pass

    def testPluginNetworkHide(self):
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
            pyautogui.press('down')
            pyautogui.press('right')
            pyautogui.press('down')
            pyautogui.press('down')
            pyautogui.press('down')
            pyautogui.press('enter')
            utils.m.move(100, 100)
            time.sleep(2)

        pluginnetwork = self.dock.dockObj.child(self.dock.string_plugin_network + self.device[0])
        self.assertTrue(pluginnetwork == None)

    def testPluginNetworkDisplay(self):
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
            pyautogui.press('down')
            pyautogui.press('right')
            pyautogui.press('down')
            pyautogui.press('down')
            pyautogui.press('down')
            pyautogui.press('enter')
            utils.m.move(100, 100)
            time.sleep(2)

        pluginnetwork = self.dock.dockObj.child(self.dock.string_plugin_network + self.device[0])
        self.assertTrue(pluginnetwork != None)

    def suite():
        suite = unittest.TestSuite()
        suite.addTest(Dock_PluginNetwork('testPluginNetworkHide'))
        suite.addTest(Dock_PluginNetwork('testPluginNetworkDisplay'))
        return suite

if __name__ == "__main__":
    unittest.installHandler()
    LOCALE_DIR = os.path.abspath("./lib/locale")
    gettext.install('dsystem', LOCALE_DIR)
    runTest(Dock_PluginNetwork)
