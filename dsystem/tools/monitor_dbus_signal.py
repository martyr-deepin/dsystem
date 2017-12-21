#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import dbus
from gi.repository import GObject
from dbus.mainloop.glib import DBusGMainLoop

def msg_cb(bus, msg):
    args = msg.get_args_list()
    print(args)

def signal_handler(string_EntryRemoved):
    print(string_EntryRemoved)

if __name__ == '__main__':
    DBusGMainLoop(set_as_default=True)
    bus = dbus.SessionBus()

    string = "type='signal',sender='com.deepin.dde.daemon.Dock',interface='com.deepin.dde.daemon.Dock'"
    bus.add_match_string(string)
    #bus.add_message_filter(msg_cb)
    bus.add_signal_receiver(signal_handler, signal_name="EntryRemoved")

    mainloop = GObject.MainLoop()
    mainloop.run()
