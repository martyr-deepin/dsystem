#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import unittest
import gettext
from lib import executeTestCase
from lib import dde_control_center
from lib.com_deepin_daemon_Accounts import Accounts, User
from lib.com_deepin_SessionManager import SessionManager

casename = "all-3828:查看用户头像位置显示"

class User_Head(unittest.TestCase):
    caseid ='103472'
    @classmethod
    def setUpClass(cls):
        cls.session_manager = SessionManager()
        cls.dcc = dde_control_center.Dde_control_center()
        cls.accounts = Accounts()

    @classmethod
    def tearDownClass(cls):
        cls.dcc.backToIndex()
        cls.dcc.exit()

    def testCheckUserHead(self):
        show_check = self.dcc.showDcc()
        self.assertTrue(show_check)
        current_uid = self.session_manager.getCurrentUid()
        uid = self.accounts.FindUserById(current_uid)
        head = User(uid).getIconFile()
        head_size = self.dcc.dccObj.child(head).size
        self.assertTrue(head_size != (0, 0))

    def suite():
        suite = unittest.TestSuite()
        suite.addTest(User_Head('testCheckUserHead'))
        return suite

if __name__ == "__main__":
    unittest.installHandler()
    LOCALE_DIR = os.path.abspath("./lib/locale")
    gettext.install('dsystem', LOCALE_DIR)
    executeTestCase.runTest(User_Head)
