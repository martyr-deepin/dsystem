#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import gi
import time
from time import sleep
gi.require_version('Wnck', '3.0')
from gi.repository import Wnck

def findWindow(windowname):
    screen = Wnck.Screen.get_default()
    screen.force_update()

    for win in screen.get_windows():
        if windowname == win.get_name():
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

