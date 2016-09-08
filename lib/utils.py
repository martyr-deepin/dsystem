#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from dogtail.tree import *
from Xlib.display import Display
from pykeyboard import PyKeyboard
from pymouse import PyMouse
import dbus
from time import sleep

from lib.properties import dock, desktop
from lib.window     import *
from lib.dockmenu import dockmenu

appname = "dde-dock"
appdescription = "/usr/bin/dde-dock"
resultfile = "./result.txt"

k = PyKeyboard()
m = PyMouse()

MINIMUM_DURATION = 0.1
MINIMUM_SLEEP = 0.05

resolution = Display().screen().root.get_geometry()

def getPointOnLine(x1, y1, x2, y2, n):
    x = ((x2 - x1) * n) + x1
    y = ((y2 - y1) * n) + y1
    return (x, y)

def linear(n):
    if not 0.0 <= n <= 1.0:
        raise ValueError('Argument must be between 0.0 and 1.0.')
    return n

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

def mouseDrag(fromXY, toXY, duration=2, press=True, release=True):
    steps = []

    num_steps = int(duration / MINIMUM_SLEEP)
    sleep_amount = duration / num_steps

    steps = [
        getPointOnLine(fromXY[0], fromXY[1], toXY[0], toXY[1], linear(n / num_steps))
        for n in range(num_steps)
    ]

    steps.append((toXY[0], toXY[1]))

    if True == press:
        m.press(fromXY[0], fromXY[1])
        sleep(1)

    for lineX, lineY in steps:
        sleep(sleep_amount)

        lineX = int(round(lineX))
        lineY = int(round(lineY))
        m.move(lineX, lineY)

    if True == release:
        m.release(toXY[0], toXY[1])

def mouseDragIconToDock(fromXY, toXY):
    mouseDrag(fromXY, toXY, release=False)
    mouseDrag(toXY, (toXY[0]+50, toXY[1]), press=False)

def getDockIconCenterPoint(dockobj):
    (x, y) = dockobj.position
    (width, height) = dockobj.size
    return (x + int(width/2), y + int(height/2))

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
    properties_iface.Set(dock.dbus_interface, dock.dbus_properties_iconsize, dbus.UInt32(iconsize))
    sleep(2)

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
