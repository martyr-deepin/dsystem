#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import time
import unittest
import gettext
from lib import executeTestCase
from lib import dde_control_center

casename = "all-4485:添加删除多个账户"

class Accounts_AddMultiUserOperation(unittest.TestCase):
    caseid ='107317'
    @classmethod
    def setUpClass(cls):
        cls.dcc = dde_control_center.Dde_control_center()
        cls.dbus_account = dde_control_center.Accounts()

    @classmethod
    def tearDownClass(cls):
        cls.dcc.backToIndex()
        cls.dcc.exit()

    def addOneUser(self, username, userpw):
        createaccount = self.dcc.dccObj.child(self.dcc.string_Create_Account)
        self.assertTrue(createaccount)
        createaccount.click()
        self.dcc.page_deep += 1
        self.dcc.addUser(username, userpw, self.dcc.string_NewAccount_Create)
        time.sleep(4)

    def testAccountsAddMultiUserOperation(self):
        self.assertTrue(self.dcc.openGUI())
        self.assertTrue(self.dcc.openModule(self.dcc.string_Accounts))
        self.dcc.page_deep += 1
        deepinAllUserName = self.dbus_account.getDeepinAllUserName()

        for username in deepinAllUserName:
            username_widget = self.dcc.dccObj.child(username)
            self.assertTrue(username_widget)

        userlist = ["test01", "test02"]

        for user in userlist:
            self.addOneUser(user, user)

        newAllUserName = self.dbus_account.getDeepinAllUserName()
        for user in userlist:
            self.assertTrue(user in newAllUserName)

    def suite():
        suite = unittest.TestSuite()
        suite.addTest(Accounts_AddMultiUserOperation('testAccountsAddMultiUserOperation'))

        return suite

if __name__ == "__main__":
    LOCALE_DIR = os.path.abspath("./lib/locale")
    gettext.install('dsystem', LOCALE_DIR)
    executeTestCase.runTest(Accounts_AddMultiUserOperation)
