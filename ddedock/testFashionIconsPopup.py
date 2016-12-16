#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from time import sleep
import unittest
from lib import executeTestCase
from lib import utils
from lib import runner

result = True
casename = 'all-451:文字提示'

class FashionIconsPopup(unittest.TestCase):
    caseid = '33494'
    @classmethod
    def setUpClass(cls):
        cls.defaultfashioniconlist = ["Launcher",
                               "显示桌面",
                               "多任务视图",
                               "深度文件管理器",
                               "深度商店",
                               "深度音乐",
                               "深度影院",
                               "Google Chrome",
                               "控制中心",
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
        for name in self.defaultfashioniconlist:
            icon = self.ddedockobject.child(name)
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
                icon_popup = self.ddedockobject.child("power-popup")
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
        uuid_list = utils.getAllUuid()
        self.assertIsNotNone(uuid_list, "Can't get the network Uuid")

        for uuid in uuid_list:
            icon_name = "network-{" + uuid + "}"
            icon = self.ddedockobject.child(icon_name)
            self.assertTrue(icon, "Can't find the [ %s ] icon in the dock region with Fashion Mode" % icon_name)
            icon.point()

    def suite():
        suite = unittest.TestSuite()
        suite.addTest(FashionIconsPopup('testBottomPopupExists'))
        suite.addTest(FashionIconsPopup('testFashionNetworkIcon'))
        #suite.addTest(FashionIconsPopup('testTopPopupExists'))
        #suite.addTest(FashionIconsPopup('testRightPopupExists'))
        #suite.addTest(FashionIconsPopup('testLeftPopupExists'))
        return suite

if __name__ == "__main__":
    executeTestCase.runTest(FashionIconsPopup)
