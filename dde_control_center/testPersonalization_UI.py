#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import unittest
import gettext
from lib import executeTestCase
from lib import dde_control_center

casename = "all-3847:主题-窗口-默认"

class Personalization_UI(unittest.TestCase):
    caseid ='103580'
    @classmethod
    def setUpClass(cls):
        cls.dcc = dde_control_center.Dde_control_center()
        cls.dbus_display = dde_control_center.Display()

    @classmethod
    def tearDownClass(cls):
        cls.dcc.backToIndex()
        cls.dcc.exit()

    def testPersonalization_UI(self):
        ret = self.dcc.showModule("personalization")
        self.assertTrue(ret)
        self.dcc.page_deep += 1

        personalization_label = self.dcc.dccObj.child(self.dcc.string_Personalization)
        self.assertTrue(personalization_label)

    def suite():
        suite = unittest.TestSuite()
        suite.addTest(Personalization_UI('testPersonalization_UI'))

        return suite

if __name__ == "__main__":
    unittest.installHandler()
    LOCALE_DIR = os.path.abspath("./lib/locale")
    gettext.install('dsystem', LOCALE_DIR)
    executeTestCase.runTest(Personalization_UI)
