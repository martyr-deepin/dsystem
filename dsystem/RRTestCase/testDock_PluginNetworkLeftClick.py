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
from lib import DaemonNetwork

casename = 'all-6238:网络插件-左键'

class Dock_PluginNetworkLeftClick(unittest.TestCase):
    caseid = '283433'
    @classmethod
    def setUpClass(cls):
        cls.daemonnetwork = DaemonNetwork()
        cls.devices = cls.daemonnetwork.getActiveDevices()
        cls.testiconname = "network-" + cls.devices[0]
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

    def testPluginNetworkLeftClick(self):
        icon = self.dock.dockObj.child(self.testiconname)
        self.assertTrue(icon)
        icon.click()
        sleep(2)

        rect = self.ddecontrolcenter.getRect()
        self.assertTrue(408 == rect[2])

        pyautogui.moveTo(400, 400, duration=1)
        pyautogui.click()

    def suite():
        suite = unittest.TestSuite()
        suite.addTest(Dock_PluginNetworkLeftClick('testPluginNetworkLeftClick'))
        return suite

if __name__ == "__main__":
    unittest.installHandler()
    LOCALE_DIR = os.path.abspath("./lib/locale")
    gettext.install('dsystem', LOCALE_DIR)
    executeTestCase.runTest(Dock_PluginNetworkLeftClick)
