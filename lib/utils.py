#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from dogtail.tree import *
from Xlib.display import Display
from pykeyboard import PyKeyboard
from pymouse import PyMouse
import dbus
from time import sleep

from lib.properties import dock
from lib.window     import *
from lib.dockmenu import dockmenu

appname = "dde-dock"
appdescription = "/usr/bin/dde-dock"
resultfile = "./result.txt"

k = PyKeyboard()
m = PyMouse()

resolution = Display().screen().root.get_geometry()

def keySingle(key):
    k.press_key(key)
    k.release_key(key)
    if key != k.enter_key:
        sleep(0.5)
    else:
        sleep(1.5)

def keyTypeString(str):
    k.type_string(str)
    sleep(2)

def getDdeDockObject(name = appname, description = appdescription):
    return root.application(name, description)

def getDdeDockSession():
    session_bus = dbus.SessionBus()
    session_obj = session_bus.get_object(dock.dbus_dest,
                                         dock.dbus_objpath)
    return session_obj

def getDdeDockPropertiesInterface():
    session_dock = getDdeDockSession()
    interface = dbus.Interface(session_dock, 
                               dbus_interface=dbus.PROPERTIES_IFACE)
    return interface

def getDdeDockInterface():
    session_dock = getDdeDockSession()
    interface = dbus.Interface(session_dock, 
                               dbus_interface=dock.dbus_interface)

    return interface

def getDdeDockDisplayMode():
    properties_iface = getDdeDockPropertiesInterface()
    return properties_iface.Get(dock.dbus_interface, dock.dbus_properties_displaymode)
    
def setDdeDockDisplayMode(displaymode):
    properties_iface = getDdeDockPropertiesInterface()
    properties_iface.Set(dock.dbus_interface, dock.dbus_properties_displaymode, displaymode)
    sleep(2)

def getDdeDockPosition():
    properties_iface = getDdeDockPropertiesInterface()
    return properties_iface.Get(dock.dbus_interface, dock.dbus_properties_position)

def setDdeDockPosition(position):
    properties_iface = getDdeDockPropertiesInterface()
    properties_iface.Set(dock.dbus_interface, dock.dbus_properties_position, position)
    sleep(2)

def getDdeDockHideMode():
    properties_iface = getDdeDockPropertiesInterface()
    return properties_iface.Get(dock.dbus_interface, dock.dbus_properties_hidemode)

def setDdeDockHideMode(hidemode):
    properties_iface = getDdeDockPropertiesInterface()
    properties_iface.Set(dock.dbus_interface, dock.dbus_properties_hidemode, hidemode)
    sleep(2)

def getDdeDockHideState():
    properties_iface = getDdeDockPropertiesInterface()
    return properties_iface.Get(dock.dbus_interface, dock.dbus_properties_hidestate)

def setDdeDockHideState(hidestate):
    properties_iface = getDdeDockPropertiesInterface()
    properties_iface.Set(dock.dbus_interface, dock.dbus_properties_hidestate, hidestate)
    sleep(2)

def getDdeDockIconSize():
    properties_iface = getDdeDockPropertiesInterface()
    return properties_iface.Get(dock.dbus_interface, dock.dbus_properties_iconsize)

def setDdeDockIconSize(iconsize):
    properties_iface = getDdeDockPropertiesInterface()
    return properties_iface.Set(dock.dbus_interface, dock.dbus_properties_iconsize, iconsize)

def openFashionMode():
    setDdeDockDisplayMode(dock.displaymode_fashion)

def openEfficientMode():
    setDdeDockDisplayMode(dock.displaymode_efficient)

def commitresult(id, result):
    if os.path.exists(resultfile):
        with open(resultfile, 'a') as f:
            idstr = " ".join((id, str(result)))
            f.write(idstr + os.linesep)
            f.close()
    else:
        with open(resultfile, 'w') as f:
            idstr = " ".join((id, str(result)))
            f.write(idstr + os.linesep)
            f.close()
