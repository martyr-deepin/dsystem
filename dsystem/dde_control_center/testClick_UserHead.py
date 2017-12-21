#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os, time
import unittest
import gettext
from lib import executeTestCase
from lib import dde_control_center
from lib.com_deepin_daemon_Accounts import Accounts, User
from lib.com_deepin_SessionManager import SessionManager

casename = "all-3809:点击用户头像测试"

class Click_UserHead(unittest.TestCase):
    caseid ='103372'
    @classmethod
    def setUpClass(cls):
        cls.session_manager = SessionManager()
        cls.dcc = dde_control_center.Dde_control_center()
        cls.accounts = Accounts()

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        pass

    def tearDown(self):
        self.dcc.page_deep += 2
        self.dcc.backToIndex()
        self.dcc.exit()

    def testclick_head_left(self):
        show_check = self.dcc.showDcc()
        self.assertTrue(show_check)
        current_uid = self.session_manager.getCurrentUid()
        uid = self.accounts.FindUserById(current_uid)
        head = User(uid).getIconFile()
        self.dcc.dccObj.child(head).click(button = 1)
        time.sleep(1)
        show_not = self.dcc.dccObj.child(self.dcc.string_Modify_Avatar, roleName='label').showing
        print(show_not)
        self.assertTrue(show_not)



    time.sleep(2)

    def testclick_head_right(self):
        show_check = self.dcc.showDcc()
        self.assertTrue(show_check)
        current_uid = self.session_manager.getCurrentUid()
        uid = self.accounts.FindUserById(current_uid)
        head = User(uid).getIconFile()
        self.dcc.dccObj.child(head).click(button = 3)
        time.sleep(1)
        show_not = self.dcc.dccObj.child(self.dcc.string_Modify_Avatar, roleName='label').showing
        print(show_not)
        self.assertTrue(show_not)

    def suite():
        suite = unittest.TestSuite()
        suite.addTest(Click_UserHead('testclick_head_left'))
        suite.addTest(Click_UserHead('testclick_head_right'))
        return suite

if __name__ == "__main__":
    unittest.installHandler()
    LOCALE_DIR = os.path.abspath("./lib/locale")
    gettext.install('dsystem', LOCALE_DIR)
    executeTestCase.runTest(Click_UserHead)
