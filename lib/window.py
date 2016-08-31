#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import gi
import time
from time import sleep
gi.require_version('Wnck', '3.0')
from gi.repository import Wnck

FINDWINDOWDELAY = 5
CLOSEWINDOWDELAY = 2

def findWindow(windowname, mode="wait", comparetype="equal"):
    if "wait" == mode:
        delay = FINDWINDOWDELAY
    else:
        delay = CLOSEWINDOWDELAY

    while True:
        sleep(1)
        delay = delay - 1
        win = _findWindow(windowname, comparetype)

        if win != None and "wait" == mode:
            return win

        if None == win and "wait" != mode:
            return win

        if 0 == delay:
            return win

def _findWindow(windowname, comparetype):
    screen = Wnck.Screen.get_default()
    screen.force_update()

    for win in screen.get_windows():
        if "equal" == comparetype:
            if windowname == win.get_name():
                screen = None
                Wnck.shutdown()
                return win
        else:
            if windowname in win.get_name():
                screen = None
                Wnck.shutdown()
                return win

    screen = None
    win = None
    Wnck.shutdown()

    return None

def closeWindow(win):
    win.close(time.time())
    sleep(2)

def resizeWindow(win, x, y, width, height):
    win.set_geometry(Wnck.WindowGravity.CURRENT, Wnck.WindowMoveResizeMask.X, x, 0, 0, 0)
    win.set_geometry(Wnck.WindowGravity.CURRENT, Wnck.WindowMoveResizeMask.Y, 0, y, 0, 0)
    win.set_geometry(Wnck.WindowGravity.CURRENT, Wnck.WindowMoveResizeMask.WIDTH, 0, 0, width, 0)
    win.set_geometry(Wnck.WindowGravity.CURRENT, Wnck.WindowMoveResizeMask.HEIGHT, 0, 0, 0, height)
    sleep(2)

