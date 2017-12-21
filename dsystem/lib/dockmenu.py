#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from dogtail.tree import *

class DockMenu(object):
    def __init__(self):
        self.appname = "deepin-menu"
        self.description = "/usr/lib/deepin-menu"
        self.mainwindowname = "DesktopMenu"

    def findMainWindow(self):
        dockmenu = root.application(self.appname, self.description)
        window = dockmenu.child(self.mainwindowname)
        sleep(2)
        return window

dockmenu = DockMenu()
