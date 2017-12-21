#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import unittest
import gettext
from lib import executeTestCase
from lib import dde_control_center

casename = "all-4099:更新首页"

class Network_UI(unittest.TestCase):
    caseid ='999999'
    @classmethod
    def setUpClass(cls):
        cls.dcc = dde_control_center.Dde_control_center()
        cls.dbus_display = dde_control_center.Display()

    @classmethod
    def tearDownClass(cls):
        cls.dcc.backToIndex()
        cls.dcc.exit()

    def testNetwork_UI(self):
        ret = self.dcc.showModule("network")
        self.assertTrue(ret)
        self.dcc.page_deep += 1

        network_label = self.dcc.dccObj.child(self.dcc.string_Network)
        self.assertTrue(network_label)

    def suite():
        suite = unittest.TestSuite()
        suite.addTest(Network_UI('testNetwork_UI'))

        return suite

if __name__ == "__main__":
    unittest.installHandler()
    LOCALE_DIR = os.path.abspath("./lib/locale")
    gettext.install('dsystem', LOCALE_DIR)
    executeTestCase.runTest(Network_UI)
