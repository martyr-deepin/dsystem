#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import unittest
import gettext
from lib import executeTestCase
from lib import dde_control_center

casename = "all-3824:账户首页界面"

class Accounts_UI(unittest.TestCase):
    caseid ='103460'
    @classmethod
    def setUpClass(cls):
        cls.dcc = dde_control_center.Dde_control_center()
        cls.dbus_account = dde_control_center.Accounts()

    @classmethod
    def tearDownClass(cls):
        cls.dcc.backToIndex()
        cls.dcc.exit()

    def testAccountsLayout(self):
        self.assertTrue(self.dcc.openGUI())
        self.assertTrue(self.dcc.openModule(self.dcc.string_Accounts))
        self.dcc.page_deep += 1
        deepinAllUserName = self.dbus_account.getDeepinAllUserName()

        for username in deepinAllUserName:
            username_widget = self.dcc.dccObj.child(username)
            self.assertTrue(username_widget)

        createaccount = self.dcc.dccObj.child(self.dcc.string_Create_Account)
        self.assertTrue(createaccount)

    def suite():
        suite = unittest.TestSuite()
        suite.addTest(Accounts_UI('testAccountsLayout'))

        return suite

if __name__ == "__main__":
    LOCALE_DIR = os.path.abspath("./lib/locale")
    gettext.install('dsystem', LOCALE_DIR)
    executeTestCase.runTest(Accounts_UI)

