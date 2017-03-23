#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import unittest
import gettext
from lib import executeTestCase
from lib import dde_control_center

casename = "all-4222:默认程序首页"

class DefaultApplications_UI(unittest.TestCase):
    caseid ='105635'
    @classmethod
    def setUpClass(cls):
        cls.dcc = dde_control_center.Dde_control_center()
        cls.dbus_display = dde_control_center.Display()

    @classmethod
    def tearDownClass(cls):
        cls.dcc.backToIndex()
        cls.dcc.exit()

    def testDefaultApplications_UI(self):
        ret = self.dcc.showModule("defapp")
        self.assertTrue(ret)
        self.dcc.page_deep += 1

        defapp_label = self.dcc.dccObj.child(self.dcc.string_Default_Applications)
        self.assertTrue(defapp_label)

    def suite():
        suite = unittest.TestSuite()
        suite.addTest(DefaultApplications_UI('testDefaultApplications_UI'))

        return suite

if __name__ == "__main__":
    unittest.installHandler()
    LOCALE_DIR = os.path.abspath("./lib/locale")
    gettext.install('dsystem', LOCALE_DIR)
    executeTestCase.runTest(DefaultApplications_UI)
