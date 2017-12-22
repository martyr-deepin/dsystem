#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import dbus
from time import sleep

class DbusLauncher:
    def __init__(self):
        self.dbus_name = "com.deepin.dde.Launcher"
        self.obj_path  = "/com/deepin/dde/Launcher"
        self.interface = "com.deepin.dde.Launcher"

        self.session_bus = dbus.SessionBus()
        self.session_obj = self.session_bus.get_object(self.dbus_name,
                self.obj_path)
        self.ifc_properties = dbus.Interface(self.session_obj,
                dbus_interface=dbus.PROPERTIES_IFACE)
        self.ifc_methods    = dbus.Interface(self.session_obj,
                dbus_interface=self.interface)


    def Show(self):
        self.ifc_methods.Show()
        sleep(4)

    def Hide(self):
        self.ifc_methods.Hide()
        sleep(4)
