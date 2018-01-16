#!/usr/bin/evn python3
# -*- coding: utf-8 -*-

import dbus
import json

class DaemonNetwork:
    def __init__(self):
        self.dbus_name = "com.deepin.daemon.Network"
        self.obj_path  = "/com/deepin/daemon/Network"
        self.interface = "com.deepin.daemon.Network"

        self.session_bus = dbus.SessionBus()
        self.session_obj = self.session_bus.get_object(self.dbus_name,
                self.obj_path)
        self.ifc_properties = dbus.Interface(self.session_obj,
                dbus_interface=dbus.PROPERTIES_IFACE)
        self.ifc_methods    = dbus.Interface(self.session_obj,
                dbus_interface=self.interface)

    def getActiveConnections(self):
        return self.ifc_properties.Get(self.interface,
                "ActiveConnections")

    def getActiveDevices(self):
        jsondata = json.loads(self.getActiveConnections())
        devices = []
        for key in jsondata.keys():
            devicePath = jsondata[key]['Devices'][0]
            if devicePath != '':
                devices.append(devicePath)

        if len(devices) == 0:
            return None

        return devices
