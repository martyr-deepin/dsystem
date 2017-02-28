#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import time
import unittest
import gettext
from lib import executeTestCase
from lib import dde_control_center
from lib.com_deepin_SessionManager import SessionManager
from lib.com_deepin_daemon_Accounts import Accounts
from lib.com_deepin_daemon_Accounts import User

casename = "all-3786:默认头像"

class Accounts_DefaultIcon(unittest.TestCase):
    caseid ='103263'
    @classmethod
    def setUpClass(cls):
        cls.dcc = dde_control_center.Dde_control_center()
        cls.dbus_account = dde_control_center.Accounts()
        cls.session_manager = SessionManager()

    @classmethod
    def tearDownClass(cls):
        pass

    def testAccountsDefaultIcon(self):
        accounts = Accounts()
        current_uid = self.session_manager.getCurrentUid()
        user_obj_path = accounts.FindUserById(current_uid)

        loginuser = User(user_obj_path)
        self.assertTrue(current_uid == loginuser.getUid())

        ret =  self.dcc.showDcc()
        self.assertTrue(ret)

        defaulticon = loginuser.getIconFile()
        iconwidget = self.dcc.dccObj.child(defaulticon,
                description="iconMainWidget")
        self.assertTrue(iconwidget != None)

        ret = self.dcc.hideDcc()
        self.assertTrue(ret)

    def suite():
        suite = unittest.TestSuite()
        suite.addTest(Accounts_DefaultIcon('testAccountsDefaultIcon'))

        return suite

if __name__ == "__main__":
    LOCALE_DIR = os.path.abspath("./lib/locale")
    gettext.install('dsystem', LOCALE_DIR)
    executeTestCase.runTest(Accounts_DefaultIcon)
