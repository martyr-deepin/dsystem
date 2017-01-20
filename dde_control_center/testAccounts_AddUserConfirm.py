#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import unittest
import gettext
from lib import executeTestCase
from lib import dde_control_center

casename = "all-3766:添加账户-确定"

class Accounts_AddUserConfirm(unittest.TestCase):
    caseid ='103179'
    @classmethod
    def setUpClass(cls):
        cls.dcc = dde_control_center.Dde_control_center()
        cls.dbus_account = dde_control_center.Accounts()
        cls.newusername = 'test123'
        cls.newuserpw = 'test123'

    @classmethod
    def tearDownClass(cls):
        cls.dcc.backToIndex()
        cls.dcc.exit()

    def testAccountsAddUserConfirm(self):
        self.assertTrue(self.dcc.openGUI())
        self.assertTrue(self.dcc.openModule(self.dcc.string_Accounts))
        self.dcc.page_deep += 1
        deepinAllUserName = self.dbus_account.getDeepinAllUserName()

        for username in deepinAllUserName:
            username_widget = self.dcc.dccObj.child(username)
            self.assertTrue(username_widget)

        createaccount = self.dcc.dccObj.child(self.dcc.string_Create_Account)
        self.assertTrue(createaccount)
        createaccount.click()
        self.dcc.page_deep += 1
        self.dcc.addUser(self.newusername, self.newuserpw,
                         self.dcc.string_NewAccount_Cancel)

        newAllUserName = self.dbus_account.getDeepinAllUserName()
        self.assertTrue(self.newusername in newAllUserName)

    def suite():
        suite = unittest.TestSuite()
        suite.addTest(Accounts_AddUserConfirm('testAccountsAddUserConfirm'))

        return suite

if __name__ == "__main__":
    LOCALE_DIR = os.path.abspath("./lib/locale")
    gettext.install('dsystem', LOCALE_DIR)
    executeTestCase.runTest(Accounts_AddUserConfirm)
