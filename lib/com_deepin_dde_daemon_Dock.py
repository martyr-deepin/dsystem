#!/usr/bin/evn python3
# -*- coding: utf-8 -*-

import dbus

class DaemonDock:
    def __init__(self):
        self.dbus_name = "com.deepin.dde.daemon.Dock"
        self.obj_path  = "/com/deepin/dde/daemon/Dock"
        self.interface = "com.deepin.dde.daemon.Dock"

        self.session_bus = dbus.SessionBus()
        self.session_obj = self.session_bus.get_object(self.dbus_name,
                self.obj_path)
        self.ifc_properties = dbus.Interface(self.session_obj,
                dbus_interface=dbus.PROPERTIES_IFACE)
        self.ifc_methods    = dbus.Interface(self.session_obj,
                dbus_interface=self.interface)

    def getDockedApps(self):
        return self.ifc_properties.Get(self.interface,
                "DockedApps")

    def getFrontendWindowRect(self):
        return self.ifc_properties.Get(self.interface,
                "FrontendWindowRect")
