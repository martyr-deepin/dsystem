#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import unittest
import gettext
from lib import executeTestCase
from lib import dde_control_center

casename = "all-4193:键盘和语言设置首页"

class KeyboardLanguage_UI(unittest.TestCase):
    caseid ='105500'
    @classmethod
    def setUpClass(cls):
        cls.dcc = dde_control_center.Dde_control_center()
        cls.dbus_display = dde_control_center.Display()

    @classmethod
    def tearDownClass(cls):
        cls.dcc.backToIndex()
        cls.dcc.exit()

    def testKeyboardLanguage_UI(self):
        ret = self.dcc.showModule("keyboard")
        self.assertTrue(ret)
        self.dcc.page_deep += 1

        keyboard_label = self.dcc.dccObj.child(self.dcc.string_Keyboard_and_Language)
        self.assertTrue(keyboard_label)

    def suite():
        suite = unittest.TestSuite()
        suite.addTest(KeyboardLanguage_UI('testKeyboardLanguage_UI'))

        return suite

if __name__ == "__main__":
    unittest.installHandler()
    LOCALE_DIR = os.path.abspath("./lib/locale")
    gettext.install('dsystem', LOCALE_DIR)
    executeTestCase.runTest(KeyboardLanguage_UI)
