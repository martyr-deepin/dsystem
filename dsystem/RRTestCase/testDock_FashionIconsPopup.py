#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import gettext
from time import sleep
import unittest
from lib import executeTestCase
from lib import utils
from lib import runner
from lib import DaemonNetwork

casename = 'all-6205:时尚模式tooltip检查'

class Dock_FashionIconsPopup(unittest.TestCase):
    caseid = '280257'
    @classmethod
    def setUpClass(cls):
        cls.daemonnetwork = DaemonNetwork()
        cls.devices = cls.daemonnetwork.getActiveDevices()
        cls.defaultfashioniconlist = [
                               "Show Desktop",
                               "Multitasking View",
                               "Deepin File Manager",
                               "Deepin Store",
                               "Deepin Music",
                               "Deepin Movie",
                               "Google Chrome",
                               "Control Center",
                               "system-tray-fashion-mode-item",
                               "datetime-",
                               "shutdown-shutdown",
                               "sound-",
                               "trash-"]

        cls.ddedockobject = utils.getDdeDockObject()

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


    def testBottomPopupExists(self):
        sleep(2)
        for name in self.defaultfashioniconlist:
            icon = self.ddedockobject.child(name)
            print(icon.size)
            self.assertTrue(icon, "Can't find the [ %s ] icon in the dock region with Fashion Mode" % name)
            icon.point()
            if name != "datetime-" and \
               name != "system-tray-fashion-mode-item" and \
               name != "shutdown-shutdown" and \
               name != "sound-" and \
               name != "trash-" and \
               name != "Launcher":
                icon_popup = self.ddedockobject.child(name + '-popup')
            elif name == "system-tray-fashion-mode-item":
                icon.click()
                icon_popup = self.ddedockobject.child('sys-tray-popup')
                icon.click()
            elif name == "datetime-":
                icon_popup = self.ddedockobject.child(name + 'popup')
            elif name == "Launcher":
                icon_popup = self.ddedockobject.child("launcher-popup")
            elif name == "shutdown-shutdown":
                icon_popup = self.ddedockobject.child("shutdown-popup")
            elif name == "sound-" or name == "trash-":
                continue

            self.assertTrue(icon_popup, "Position Bottom: Can't find the [ %s ] icon-popup in the dock region with Fashion Mode" % name)
            print("find the popup window with icon: %s" % name)

    def testTopPopupExists(self):
        utils.setDdeDockPosition(utils.dock.position_top)
        for name in self.defaultfashioniconlist:
            icon = self.ddedockobject.child(name)
            self.assertTrue(icon, "Can't find the [ %s ] icon in the dock region with Fashion Mode" % name)
            icon.point()
            if name != "datetime-" and \
               name != "system-tray-fashion-mode-item" and \
               name != "Launcher":
                icon_popup = self.ddedockobject.child(name + '-popup')
            elif name == "system-tray-fashion-mode-item":
                icon.click()
                icon_popup = self.ddedockobject.child('sys-tray-popup')
                icon.click()
            elif name == "datetime-":
                icon_popup = self.ddedockobject.child(name + 'popup')
            elif name == "Launcher":
                icon_popup = self.ddedockobject.child("launcher-popup")

            self.assertTrue(icon_popup, "Position Top: Can't find the [ %s ] icon-popup in the dock region with Fashion Mode" % name)
            print("find the popup window with icon: %s" % name)

    def testRightPopupExists(self):
        utils.setDdeDockPosition(utils.dock.position_right)
        for name in self.defaultfashioniconlist:
            icon = self.ddedockobject.child(name)
            self.assertTrue(icon, "Can't find the [ %s ] icon in the dock region with Efficient Mode" % name)
            icon.point()
            if name != "datetime-" and \
               name != "system-tray-fashion-mode-item" and \
               name != "Launcher":
                icon_popup = self.ddedockobject.child(name + '-popup')
            elif name == "system-tray-fashion-mode-item":
                icon.click()
                icon_popup = self.ddedockobject.child('sys-tray-popup')
                icon.click()
            elif name == "datetime-":
                icon_popup = self.ddedockobject.child(name + 'popup')
            elif name == "Launcher":
                icon_popup = self.ddedockobject.child("launcher-popup")

            self.assertTrue(icon_popup, "Position Right: Can't find the [ %s ] icon-popup in the dock region with Fashion Mode" % name)
            print("find the popup window with icon: %s" % name)

    def testLeftPopupExists(self):
        utils.setDdeDockPosition(utils.dock.position_left)
        for name in self.defaultfashioniconlist:
            icon = self.ddedockobject.child(name)
            self.assertTrue(icon, "Can't find the [ %s ] icon in the dock region with Efficient Mode" % name)
            icon.point()
            if name != "datetime-" and \
               name != "system-tray-fashion-mode-item" and \
               name != "Launcher":
                icon_popup = self.ddedockobject.child(name + '-popup')
            elif name == "system-tray-fashion-mode-item":
                icon.click()
                icon_popup = self.ddedockobject.child('sys-tray-popup')
                icon.click()
            elif name == "datetime-":
                icon_popup = self.ddedockobject.child(name + 'popup')
            elif name == "Launcher":
                icon_popup = self.ddedockobject.child("launcher-popup")

            self.assertTrue(icon_popup, "Position Left: Can't find the [ %s ] icon-popup in the dock region with Fashion Mode" % name)
            print("find the popup window with icon: %s" % name)

    def testFashionNetworkIcon(self):
        for device in self.devices:
            icon_name = "network-" + device
            icon = self.ddedockobject.child(icon_name)
            self.assertTrue(icon, "Can't find the [ %s ] icon in the dock region with Fashion Mode" % icon_name)
            icon.point()

    def suite():
        suite = unittest.TestSuite()
        suite.addTest(Dock_FashionIconsPopup('testBottomPopupExists'))
        suite.addTest(Dock_FashionIconsPopup('testFashionNetworkIcon'))
        #suite.addTest(Dock_FashionIconsPopup('testTopPopupExists'))
        #suite.addTest(Dock_FashionIconsPopup('testRightPopupExists'))
        #suite.addTest(Dock_FashionIconsPopup('testLeftPopupExists'))
        return suite

if __name__ == "__main__":
    unittest.installHandler()
    LOCALE_DIR = os.path.abspath("./lib/locale")
    gettext.install('dsystem', LOCALE_DIR)
    executeTestCase.runTest(Dock_FashionIconsPopup)
