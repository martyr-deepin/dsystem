#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os, time
import unittest
import gettext
from lib import executeTestCase
from lib import dde_control_center
from lib.com_deepin_daemon_Accounts import Accounts, User
from lib.com_deepin_SessionManager import SessionManager

casename = "all-3811:系统预置头像显示"

class Check_UserHead_Display(unittest.TestCase):
    caseid ='103383'
    @classmethod
    def setUpClass(cls):
        cls.session_manager = SessionManager()
        cls.dcc = dde_control_center.Dde_control_center()
        cls.accounts = Accounts()

    @classmethod
    def tearDownClass(cls):
        cls.dcc.page_deep += 3
        cls.dcc.backToIndex()
        cls.dcc.exit()

    def get_currenthead(self):
        current_uid = self.session_manager.getCurrentUid()
        uid = self.accounts.FindUserById(current_uid)
        head = User(uid).getIconFile()
        return head

    def test_modify_avatar(self):
        show_check = self.dcc.showDcc()
        self.assertTrue(show_check)
        self.dcc.dccObj.child(self.get_currenthead()).click()
        time.sleep(1)
        self.dcc.dccObj.child(self.dcc.string_Modify_Avatar, roleName='label').click()

    def test_check_headnum(self):
        backstage_path = '/var/lib/AccountsService/icons/'
        ui_path = 'file:///var/lib/AccountsService/icons/'
        for i in range(1,15):
            print(i)
            backstage_fullpath = backstage_path +  ('%d.png' % (i))
            backstage_bool = os.path.exists(backstage_fullpath)
            self.assertTrue(backstage_bool)

            ui_icon = ui_path + ('%d.png' % (i))
            if ui_icon == self.get_currenthead():
                des = 'selectedIcon'
            else:
                des = ''
            print(des)
            ui_check = self.dcc.dccObj.child(ui_icon, roleName='label' , description=des).showing
            print(ui_check)
            self.assertTrue(ui_check)

        addicon_check = self.dcc.dccObj.child('add_avatar', roleName='image').showing
        print('addicon is', addicon_check)
        self.assertTrue(addicon_check)

    def suite():
        suite = unittest.TestSuite()
        suite.addTest(Check_UserHead_Display('get_currenthead'))
        suite.addTest(Check_UserHead_Display('test_modify_avatar'))
        suite.addTest(Check_UserHead_Display('test_check_headnum'))
        return suite

if __name__ == "__main__":
    unittest.installHandler()
    LOCALE_DIR = os.path.abspath("./lib/locale")
    gettext.install('dsystem', LOCALE_DIR)
    executeTestCase.runTest(Check_UserHead_Display)
