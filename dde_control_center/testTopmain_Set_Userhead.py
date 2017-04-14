#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os, time, random
import unittest
import gettext
from lib import executeTestCase
from lib import dde_control_center
from lib.com_deepin_daemon_Accounts import Accounts, User
from lib.com_deepin_SessionManager import SessionManager

casename = "all-3812:系统预置头像设置"

class Set_UserHead_Builtin(unittest.TestCase):
    caseid ='103388'

    @classmethod
    def setUpClass(cls):
        cls.session_manager = SessionManager()
        cls.dcc = dde_control_center.Dde_control_center()
        cls.accounts = Accounts()

    @classmethod
    def tearDownClass(cls):
        pass

    def get_currenthead(self):
        current_uid = self.session_manager.getCurrentUid()
        uid = self.accounts.FindUserById(current_uid)
        head = User(uid).getIconFile()
        return head

    # set another different user head
    def test_set_diffimage(self):
        show_check = self.dcc.showDcc()
        self.assertTrue(show_check)
        self.dcc.dccObj.child(self.get_currenthead()).click()
        self.dcc.dccObj.child(self.dcc.string_Modify_Avatar, roleName='label').click()

        ui_path = 'file:///var/lib/AccountsService/icons/'
        current_head = self.get_currenthead()
        used_num = ((current_head.split('/')[-1]).split('.'))[0]
        print('used_num is ', used_num)
        items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
        items.remove(int(used_num))
        print(items)
        x = random.choice(items)
        ui_icon = ui_path + ('%d.png' % (x))

        self.dcc.dccObj.child(ui_icon, roleName='label' ).click()
        changed_head = self.get_currenthead()
        self.assertTrue(current_head != changed_head)
        self.dcc.page_deep += 2
        self.dcc.backToIndex()
        self.dcc.exit()

    # set the same user head
    def test_set_sameimage(self):
        time.sleep(1)
        show_check = self.dcc.showDcc()
        self.assertTrue(show_check)
        self.dcc.dccObj.child(self.get_currenthead()).click()
        self.dcc.dccObj.child(self.dcc.string_Modify_Avatar, roleName='label').click()

        current_head = self.get_currenthead()
        self.dcc.dccObj.child(current_head, roleName='label', description='selectedIcon').click()
        changed_head = self.get_currenthead()
        self.assertTrue(current_head == changed_head)

        self.dcc.page_deep += 2
        self.dcc.backToIndex()
        self.dcc.exit()

    def suite():
        suite = unittest.TestSuite()
        suite.addTest(Set_UserHead_Builtin('test_set_diffimage'))
        suite.addTest(Set_UserHead_Builtin('test_set_sameimage'))
        return suite


if __name__ == "__main__":
    unittest.installHandler()
    LOCALE_DIR = os.path.abspath("./lib/locale")
    gettext.install('dsystem', LOCALE_DIR)
    executeTestCase.runTest(Set_UserHead_Builtin)
