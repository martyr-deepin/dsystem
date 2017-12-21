#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import unittest
import gettext
from lib import executeTestCase
from lib import dde_control_center

casename = "all-4013:鼠标和触控板首页"

class MouseTouchpad_UI(unittest.TestCase):
    caseid ='104612'
    @classmethod
    def setUpClass(cls):
        cls.dcc = dde_control_center.Dde_control_center()
        cls.dbus_display = dde_control_center.Display()

    @classmethod
    def tearDownClass(cls):
        cls.dcc.backToIndex()
        cls.dcc.exit()

    def testMouseTouchpad_UI(self):
        ret = self.dcc.showModule("mouse")
        self.assertTrue(ret)
        self.dcc.page_deep += 1

        mouse_label = self.dcc.dccObj.child(self.dcc.string_Mouse_and_Touchpad)
        self.assertTrue(mouse_label)

    def suite():
        suite = unittest.TestSuite()
        suite.addTest(MouseTouchpad_UI('testMouseTouchpad_UI'))

        return suite

if __name__ == "__main__":
    unittest.installHandler()
    LOCALE_DIR = os.path.abspath("./lib/locale")
    gettext.install('dsystem', LOCALE_DIR)
    executeTestCase.runTest(MouseTouchpad_UI)
