#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from Xlib.display import Display
from Xlib import X
from Xlib.ext.xtest import fake_input
from Xlib.ext import record
from Xlib.protocol import rq

from base import PyMouseMeta, PyMouseEventMeta

class PyMouseEvent(PyMouseEventMeta):
    def __init__(self, display=None):
        PyMouseEventMeta.__init__(self)
        self.display = Display(display)
        self.display2 = Display(display)
        self.ctx = self.display2.record_create_context(
            0,
            [record.AllClients],
            [{
                    'core_requests': (0, 0),
                    'core_replies': (0, 0),
                    'ext_requests': (0, 0, 0, 0),
                    'ext_replies': (0, 0, 0, 0),
                    'delivered_events': (0, 0),
                    'device_events': (X.ButtonPressMask, X.ButtonReleaseMask),
                    'errors': (0, 0),
                    'client_started': False,
                    'client_died': False,
            }])

    def run(self):
        if self.capture:
            self.display2.screen().root.grab_pointer(True, X.ButtonPressMask | X.ButtonReleaseMask, X.GrabModeAsync, X.GrabModeAsync, 0, 0, X.CurrentTime)

        self.display2.record_enable_context(self.ctx, self.handler)
        self.display2.record_free_context(self.ctx)

    def stop(self):
        self.display.record_disable_context(self.ctx)
        self.display.ungrab_pointer(X.CurrentTime)
        self.display.flush()
        self.display2.record_disable_context(self.ctx)
        self.display2.ungrab_pointer(X.CurrentTime)
        self.display2.flush()

    def handler(self, reply):
        data = reply.data
        while len(data):
            event, data = rq.EventField(None).parse_binary_value(data, self.display.display, None, None)

            if event.type == X.ButtonPress:
                #self.click(event.root_x, event.root_y, (None, 1, 3, 2, 3, 3, 3)[event.detail], True)
                print("Press...............")
            elif event.type == X.ButtonRelease:
                #self.click(event.root_x, event.root_y, (None, 1, 3, 2, 3, 3, 3)[event.detail], False)
                print("Release.............")
            else:
                #self.move(event.root_x, event.root_y)
                pass
