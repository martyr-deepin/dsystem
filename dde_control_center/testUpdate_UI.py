#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import unittest
import gettext
from lib import executeTestCase
from lib import dde_control_center

casename = "all-4099:更新首页"

class Update_UI(unittest.TestCase):
    caseid ='105072'
    @classmethod
    def setUpClass(cls):
        cls.dcc = dde_control_center.Dde_control_center()
        cls.dbus_display = dde_control_center.Display()

    @classmethod
    def tearDownClass(cls):
        cls.dcc.backToIndex()
        cls.dcc.exit()

    def testUpdate_UI(self):
        ret = self.dcc.showModule("update")
        self.assertTrue(ret)
        self.dcc.page_deep += 1

        update_label = self.dcc.dccObj.child(self.dcc.string_Update)
        self.assertTrue(update_label)

    def suite():
        suite = unittest.TestSuite()
        suite.addTest(Update_UI('testUpdate_UI'))

        return suite

if __name__ == "__main__":
    unittest.installHandler()
    LOCALE_DIR = os.path.abspath("./lib/locale")
    gettext.install('dsystem', LOCALE_DIR)
    executeTestCase.runTest(Update_UI)
