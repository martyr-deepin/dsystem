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
from lib.polkit_agent import do_polkit_agent

casename = "all-3796:修改密码-保存"

class Accounts_ModifyUserPasswordAccept(unittest.TestCase):
    caseid ='103312'
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
        accounts = Accounts()
        current_uid = cls.session_manager.getCurrentUid()
        user_obj_path = accounts.FindUserById(current_uid)
        loginuser = User(user_obj_path)
        loginuser.SetPassword(cls.oldpw)
        do_polkit_agent(cls.newpw)
        cls.dcc.hideDcc()

    def testAccountsModifyUserPasswordAccept(self):
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

        NewPasswordWidget = self.dcc.dccObj.child(self.dcc.string_New_Password, roleName='password text')
        self.assertTrue(NewPasswordWidget != None)
        NewPasswordWidget.click()
        utils.keyTypeString(self.newpw)

        RepeatPasswordWidget = self.dcc.dccObj.child(self.dcc.string_Repeat_Password, roleName='password text')
        self.assertTrue(RepeatPasswordWidget != None)
        RepeatPasswordWidget.click()
        utils.keyTypeString(self.newpw)

        ModifyAcceptWidget = self.dcc.dccObj.child(self.dcc.string_Modify_Accept)
        self.assertTrue(ModifyAcceptWidget != None)
        ModifyAcceptWidget.click()

        do_polkit_agent()

        ret = self.dbus_lock.UnlockCheck(self.currentUserName, self.newpw)
        self.assertTrue(ret)
        ret = self.dbus_lock.UnlockCheck(self.currentUserName, self.oldpw)
        self.assertFalse(ret)

    def suite():
        suite = unittest.TestSuite()
        suite.addTest(Accounts_ModifyUserPasswordAccept('testAccountsModifyUserPasswordAccept'))

        return suite

if __name__ == "__main__":
    unittest.installHandler()
    LOCALE_DIR = os.path.abspath("./lib/locale")
    gettext.install('dsystem', LOCALE_DIR)
    executeTestCase.runTest(Accounts_ModifyUserPasswordAccept)
