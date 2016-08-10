#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from time import sleep
import unittest
from lib import utils

class FashionIconsPopup(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.defaultfashioniconlist = ["Launcher",
                               "显示桌面",
                               "多任务视图",
                               "文件",
                               "深度商店",
                               "深度音乐",
                               "Google Chrome",
                               "控制中心",
                               "system-tray-fashion-mode-item",
                               "datetime-"]

        cls.ddedockobject = utils.getDdeDockObject()
        cls.defaultdisplaymode = utils.getDdeDockDisplayMode()
        cls.defaultposition    = utils.getDdeDockPosition()

        if utils.dock.position_bottom != cls.defaultposition:
            utils.setDdeDockPosition(utils.dock.position_bottom)

        if utils.dock.displaymode_fashion != cls.defaultdisplaymode:
            utils.setDdeDockDisplayMode(utils.dock.displaymode_fashion)

    @classmethod
    def tearDownClass(cls):
        utils.setDdeDockDisplayMode(cls.defaultdisplaymode)
        utils.setDdeDockPosition(cls.defaultposition)
    
    def testBottomPopupExists(self):
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

            self.assertTrue(icon_popup, "Position Bottom: Can't find the [ %s ] icon-popup in the dock region with Fashion Mode" % name)
            print("find the popup window with icon: %s" % name)

    def testTopPopupExists(self):
        utils.setDdeDockPosition(utils.dock.position_top)
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

def suite():
    suite = unittest.TestSuite()
    suite.addTest(FashionIconsPopup('testBottomPopupExists'))
    #suite.addTest(FashionIconsPopup('testTopPopupExists'))
    #suite.addTest(FashionIconsPopup('testRightPopupExists'))
    #suite.addTest(FashionIconsPopup('testLeftPopupExists'))
    return suite

if __name__ == "__main__":
    unittest.TextTestRunner(verbosity=1).run(suite())
