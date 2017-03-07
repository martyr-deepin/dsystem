#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import time
import unittest
import gettext
from lib import utils
from lib import executeTestCase
from lib import dde_control_center
from lib.com_deepin_SessionManager import SessionManager
from lib.com_deepin_daemon_Accounts import Accounts
from lib.com_deepin_daemon_Accounts import User
from lib.com_deepin_dde_lock import Lock

casename = "all-3840:修改密码-取消"

class Accounts_ModifyUserPasswordCancel(unittest.TestCase):
    caseid ='103526'
    @classmethod
    def setUpClass(cls):
        cls.dcc = dde_control_center.Dde_control_center()
        cls.dbus_account = dde_control_center.Accounts()
        cls.session_manager = SessionManager()
        cls.dbus_lock = Lock()
        cls.newpw = "asdf"
        cls.oldpw = "deepin"

        cls.currentUserName = None

    @classmethod
    def tearDownClass(cls):
        cls.dcc.hideDcc()

    def testAccountsModifyUserPasswordCancel(self):
        accounts = Accounts()
        current_uid = self.session_manager.getCurrentUid()
        user_obj_path = accounts.FindUserById(current_uid)

        loginuser = User(user_obj_path)
        self.assertTrue(current_uid == loginuser.getUid())

        self.currentUserName = loginuser.getUserName()
        self.assertTrue(self.currentUserName != None)

        ret = self.dcc.showModule("accounts")
        self.assertTrue(ret)

        curUserNameWidget = self.dcc.dccObj.child(self.currentUserName, roleName='label')
        self.assertTrue(curUserNameWidget != None)
        curUserNameWidget.click()

        ModifyPasswordWidget = self.dcc.dccObj.child(self.dcc.string_Modify_Password, roleName='label')
        self.assertTrue(ModifyPasswordWidget != None)
        ModifyPasswordWidget.click()

        NewPasswordWidget = self.dcc.dccObj.child(self.dcc.string_New_Password, roleName='label')
        self.assertTrue(NewPasswordWidget != None)
        NewPasswordWidget.click()
        utils.keyTypeString(self.newpw)

        RepeatPasswordWidget = self.dcc.dccObj.child(self.dcc.string_Repeat_Password, roleName='label')
        self.assertTrue(RepeatPasswordWidget != None)
        RepeatPasswordWidget.click()
        utils.keyTypeString(self.newpw)

        ModifyCancelWidget = self.dcc.dccObj.child(self.dcc.string_Modify_Cancel)
        self.assertTrue(ModifyCancelWidget != None)
        ModifyCancelWidget.click()

        ret = self.dbus_lock.UnlockCheck(self.currentUserName, self.newpw)
        self.assertFalse(ret)
        ret = self.dbus_lock.UnlockCheck(self.currentUserName, self.oldpw)
        self.assertTrue(ret)

    def suite():
        suite = unittest.TestSuite()
        suite.addTest(Accounts_ModifyUserPasswordCancel('testAccountsModifyUserPasswordCancel'))

        return suite

if __name__ == "__main__":
    unittest.installHandler()
    LOCALE_DIR = os.path.abspath("./lib/locale")
    gettext.install('dsystem', LOCALE_DIR)
    executeTestCase.runTest(Accounts_ModifyUserPasswordCancel)
