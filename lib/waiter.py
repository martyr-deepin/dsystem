#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from Xlib.display import Display
from Xlib import X
from time import sleep

display = Display(':0')

root = display.screen().root

root.change_attributes(event_mask = X.SubstructureNotifyMask)

class EventWaiter(object):
    def waitMapNotify(self):
        while True:
            ev = display.next_event()
            if ev.type == X.MapNotify:
                sleep(1)
                return ev

waiter = EventWaiter()
