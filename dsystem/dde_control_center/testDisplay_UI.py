#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import unittest
import gettext
from lib import executeTestCase
from lib import dde_control_center

casename = "all-4126:分辨率--显示"

class Display_UI(unittest.TestCase):
    caseid ='105206'
    @classmethod
    def setUpClass(cls):
        cls.dcc = dde_control_center.Dde_control_center()
        cls.dbus_display = dde_control_center.Display()

    @classmethod
    def tearDownClass(cls):
        cls.dcc.backToIndex()
        cls.dcc.exit()

    def testDisplay_UI(self):
        ret = self.dcc.showModule("display")
        self.assertTrue(ret)
        self.dcc.page_deep += 1

        display_label = self.dcc.dccObj.child(self.dcc.string_Display)
        self.assertTrue(display_label)
        resolution_label = self.dcc.dccObj.child(self.dcc.string_Resolution)
        self.assertTrue(resolution_label)
        rotate_label = self.dcc.dccObj.child(self.dcc.string_Rotate)
        self.assertTrue(rotate_label)

    def suite():
        suite = unittest.TestSuite()
        suite.addTest(Display_UI('testDisplay_UI'))

        return suite

if __name__ == "__main__":
    unittest.installHandler()
    LOCALE_DIR = os.path.abspath("./lib/locale")
    gettext.install('dsystem', LOCALE_DIR)
    executeTestCase.runTest(Display_UI)
