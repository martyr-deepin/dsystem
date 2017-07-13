#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import time
import unittest
import gettext
import configparser
from lib import executeTestCase
from lib import dde_control_center
from lib.com_deepin_SessionManager import SessionManager
from lib.com_deepin_daemon_Accounts import Accounts
from lib.com_deepin_daemon_Accounts import User

casename = "all-3787:修改头像"

class Accounts_ModifyUserIcon(unittest.TestCase):
    caseid ='103268'
    @classmethod
    def setUpClass(cls):
        cls.dcc = dde_control_center.Dde_control_center()
        cls.dbus_account = dde_control_center.Accounts()
        cls.session_manager = SessionManager()

        cls.currentIcon = None
        cls.currentUserName = None
        cls.randUserIcon = None

    @classmethod
    def tearDownClass(cls):
        cls.dcc.hideDcc()

    def testAccountsModifyUserIcon(self):
        accounts = Accounts()
        current_uid = self.session_manager.getCurrentUid()
        user_obj_path = accounts.FindUserById(current_uid)

        loginuser = User(user_obj_path)
        self.assertTrue(current_uid == loginuser.getUid())

        self.currentUserName = loginuser.getUserName()
        self.currentIcon = loginuser.getIconFile()
        self.assertTrue(self.currentIcon != None)

        while self.randUserIcon == None or \
              self.randUserIcon == self.currentIcon:
            self.randUserIcon = accounts.RandUserIcon()

        ret = self.dcc.showModule("accounts")
        self.assertTrue(ret)

        IndexAvatarWidget = self.dcc.dccObj.child(self.randUserIcon, roleName='label', description=self.dcc.string_Icon)
        self.assertFalse(IndexAvatarWidget)

        curUserNameWidget = self.dcc.dccObj.child(self.currentUserName, roleName='label')
        self.assertTrue(curUserNameWidget != None)
        curUserNameWidget.click()

        ModifyAvatarWidget = self.dcc.dccObj.child(self.dcc.string_Modify_Avatar, roleName='label')
        self.assertTrue(ModifyAvatarWidget != None)
        ModifyAvatarWidget.click()
        randUserIconWidget = self.dcc.dccObj.child(self.randUserIcon)
        self.assertTrue(randUserIconWidget != None)
        randUserIconWidget.click()

        time.sleep(1)
        self.assertTrue(loginuser.getIconFile() == self.randUserIcon)
        self.assertTrue(self.randUserIcon != self.currentIcon)

        IndexAvatarWidget = self.dcc.dccObj.child(self.randUserIcon, roleName='label', description=self.dcc.string_Icon)
        self.assertTrue(IndexAvatarWidget)

        path = '/var/lib/AccountsService/users/' + self.currentUserName
        user_cfg = configparser.ConfigParser()
        user_cfg.read(path)
        usericon = user_cfg.get('User', 'Icon')
        self.assertTrue(usericon, self.randUserIcon)

    def suite():
        suite = unittest.TestSuite()
        suite.addTest(Accounts_ModifyUserIcon('testAccountsModifyUserIcon'))

        return suite

if __name__ == "__main__":
    unittest.installHandler()
    LOCALE_DIR = os.path.abspath("./lib/locale")
    gettext.install('dsystem', LOCALE_DIR)
    executeTestCase.runTest(Accounts_ModifyUserIcon)
