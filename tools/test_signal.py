#!/usr/bin/python3
# -*- coding: utf-8 -*-

import gi
import signal
from time import sleep, time
gi.require_version('Wnck', '3.0')
gi.require_version('Gtk', '3.0')
from gi.repository import Wnck
from gi.repository import Gtk, GLib, GObject

from lib import PyMouseEvent
import threading

def application_opened_callback(WnckScreen, WnckApplication):
    print("%s opened:\n    %s" % (WnckApplication.get_name(), time()))

def application_closed_callback(WnckScreen, WnckApplication):
    print("%s closed:\n    %s" % (WnckApplication.get_name(), time()))

class WindowOpenMonitor:
    def __init__(self):
        self.screen = Wnck.Screen.get(0)
        self.screen.connect('window-opened', application_opened_callback)
        self.screen.connect('window-closed', application_closed_callback)

    def run(self):
        signal.signal(signal.SIGINT, signal.SIG_DFL)
        Gtk.main()

class MouseThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.mouse = PyMouseEvent()

    def run(self):
        self.mouse.run()

if __name__ == "__main__":
    mouseThread = MouseThread()
    mouseThread.start()

    wom = WindowOpenMonitor()
    wom.run()
