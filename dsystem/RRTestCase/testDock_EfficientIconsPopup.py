#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import gettext
import unittest
from lib import executeTestCase
from lib import utils
from lib import runner

casename = 'all-6206:高效模式tooltip检查'

class Dock_EfficientIconsPopup(unittest.TestCase):
    caseid = '280259'
    @classmethod
    def setUpClass(cls):
        cls.defaultefficienticonlist = [
                                        "Show Desktop",
                                        "Multitasking View",
                                        "Deepin File Manager",
                                        "Deepin Store",
                                        "Deepin Music",
                                        "Deepin Movie",
                                        "Google Chrome",
                                        "Control Center",
                                        "datetime-",
                                        "sound-",
                                        "shutdown-shutdown"]

        cls.ddedockobject = utils.getDdeDockObject()

        if utils.dock.displaymode_efficient != utils.getDdeDockDisplayMode:
            utils.setDdeDockDisplayMode(utils.dock.displaymode_efficient)

        if utils.dock.position_bottom != utils.getDdeDockPosition:
            utils.setDdeDockPosition(utils.dock.position_bottom)

    @classmethod
    def tearDownClass(cls):
        if utils.dock.displaymode_fashion != utils.getDdeDockDisplayMode():
            utils.setDdeDockDisplayMode(utils.dock.displaymode_fashion)

        if utils.dock.position_bottom != utils.getDdeDockPosition():
            utils.setDdeDockPosition(utils.dock.position_bottom)

    def testBottomPopupExists(self):
        for name in self.defaultefficienticonlist:
            icon = self.ddedockobject.child(name)
            self.assertTrue(icon, "Can't find the [ %s ] icon in the dock region with Efficient Mode" % name)
            icon.point()
            if name != "datetime-" and \
               name != "shutdown-shutdown" and \
               name != "sound-" and \
               name != "Launcher":
                icon_popup = self.ddedockobject.child(name + '-popup')
            elif name == "datetime-":
                icon_popup = self.ddedockobject.child(name + 'popup')
            elif name == "Launcher":
                icon_popup = self.ddedockobject.child("launcher-popup")
            elif name == "shutdown-shutdown":
                icon_popup = self.ddedockobject.child("shutdown-popup")
            elif name == "sound-":
                continue

            self.assertTrue(icon_popup, "Position bottom: Can't find the [ %s ] icon-popup in the dock region with Efficient Mode" % name)
            print("find the popup window with icon: %s" % name)

    def testTopPopupExists(self):
        utils.setDdeDockPosition(utils.dock.position_top)
        for name in self.defaultefficienticonlist:
            icon = self.ddedockobject.child(name)
            self.assertTrue(icon, "Can't find the [ %s ] icon in the dock region with Efficient Mode" % name)
            icon.point()
            if name != "datetime-" and \
               name != "Launcher":
                icon_popup = self.ddedockobject.child(name + '-popup')
            elif name == "datetime-":
                icon_popup = self.ddedockobject.child(name + 'popup')
            elif name == "Launcher":
                icon_popup = self.ddedockobject.child("launcher-popup")

            self.assertTrue(icon_popup, "Position Top: Can't find the [ %s ] icon-popup in the dock region with Efficient Mode" % name)
            print("find the popup window with icon: %s" % name)

    def testRightPopupExists(self):
        utils.setDdeDockPosition(utils.dock.position_right)
        for name in self.defaultefficienticonlist:
            icon = self.ddedockobject.child(name)
            self.assertTrue(icon, "Can't find the [ %s ] icon in the dock region with Efficient Mode" % name)
            icon.point()
            if name != "datetime-" and \
               name != "Launcher":
                icon_popup = self.ddedockobject.child(name + '-popup')
            elif name == "datetime-":
                icon_popup = self.ddedockobject.child(name + 'popup')
            elif name == "Launcher":
                icon_popup = self.ddedockobject.child("launcher-popup")

            self.assertTrue(icon_popup, "Position Right: Can't find the [ %s ] icon-popup in the dock region with Efficient Mode" % name)
            print("find the popup window with icon: %s" % name)

    def testLeftPopupExists(self):
        utils.setDdeDockPosition(utils.dock.position_left)
        for name in self.defaultefficienticonlist:
            icon = self.ddedockobject.child(name)
            self.assertTrue(icon, "Can't find the [ %s ] icon in the dock region with Efficient Mode" % name)
            icon.point()
            if name != "datetime-" and \
               name != "Launcher":
                icon_popup = self.ddedockobject.child(name + '-popup')
            elif name == "datetime-":
                icon_popup = self.ddedockobject.child(name + 'popup')
            elif name == "Launcher":
                icon_popup = self.ddedockobject.child("launcher-popup")

            self.assertTrue(icon_popup, "Position Left: Can't find the [ %s ] icon-popup in the dock region with Efficient Mode" % name)
            print("find the popup window with icon: %s" % name)

    def testEfficientNetworkIcon(self):
        winid_list = utils.getTrayManagerWinId()
        self.assertIsNotNone(winid_list, "Can't get the TrayManager window id.")

        for winid in winid_list:
            icon_name = "system-tray-window:" + str(winid)
            icon = self.ddedockobject.child(icon_name)
            self.assertTrue(icon, "Can't find the [ %s ] icon in the dock region with Fashion Mode" % icon_name)
            icon.point()

    def suite():
        suite = unittest.TestSuite()
        suite.addTest(Dock_EfficientIconsPopup('testBottomPopupExists'))
        suite.addTest(Dock_EfficientIconsPopup('testEfficientNetworkIcon'))
        #suite.addTest(EfficientIconsPopup('testEfficientNetworkIcon'))
        #suite.addTest(EfficientIconsPopup('testTopPopupExists'))
        #suite.addTest(EfficientIconsPopup('testRightPopupExists'))
        #suite.addTest(EfficientIconsPopup('testLeftPopupExists'))
        return suite

if __name__ == "__main__":
    unittest.installHandler()
    LOCALE_DIR = os.path.abspath("./lib/locale")
    gettext.install('dsystem', LOCALE_DIR)
    executeTestCase.runTest(Dock_EfficientIconsPopup)

