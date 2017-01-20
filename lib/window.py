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

def findWindowList(windowname, comparetype="equal"):
    screen = Wnck.Screen.get_default()
    screen.force_update()

    winlist = []

    for win in screen.get_windows():
        if "equal" == comparetype:
            if windowname == win.get_name():
                winlist.append(win)
        else:
            if windowname in win.get_name():
                winlist.append(win)

    screen = None
    Wnck.shutdown()

    if len(winlist) > 0:
        return winlist

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

class WindowError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)

class WindowState(object):
    def __init__(self, name, mode="wait", comparetype="equal"):
        self.name = name
        self.mode = mode
        self.comparetype = comparetype

    def getWindow(self):
        win = findWindow(self.name, self.mode, self.comparetype)

        #if None == win:
        #    raise WindowError("Can't find the window name: %s" % self.name)

        return win

    def is_maximized(self):
        win = self.getWindow()
        return win.is_maximized()

    def is_minimized(self):
        win = self.getWindow()
        return win.is_minimized()

    def is_fullscreen(self):
        win = self.getWindow()
        return win.is_fullscreen()

    def is_active(self):
        win = self.getWindow()
        return win.is_active()

    def maximize(self):
        win = self.getWindow()
        return win.maximize()

    def minimize(self):
        win = self.getWindow()
        return win.minimize()

    def unminimize(self):
        win = self.getWindow()
        return win.unminimize(time.time())

    def activate(self):
        win = self.getWindow()
        return win.activate(time.time())

    def close(self):
        win = self.getWindow()
        win.close(time.time())
