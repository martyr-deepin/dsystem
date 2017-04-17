#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from time import localtime, strftime
import unittest
import gettext
from lib import executeTestCase
from lib import dde_control_center
from lib.com_deepin_daemon_Accounts import Accounts, User
from lib.com_deepin_SessionManager import SessionManager

casename = "all-3813:打开自定义头像设置对话框"

class Check_Topmain_Datetime(unittest.TestCase):
    caseid ='103388'

    @classmethod
    def setUpClass(cls):
        cls.dcc = dde_control_center.Dde_control_center()

    @classmethod
    def tearDownClass(cls):
        cls.dcc.exit()


    def test_check_time(self):
        self.dcc.showDcc()
        c_time = strftime('%H:%M', localtime())
        c_date = strftime('%A, %B %d, %Y', localtime())
        print(c_time)
        print(c_date)
        time_check = self.dcc.dccObj.child(c_time, roleName='label').showing
        date_check = self.dcc.dccObj.child(c_date, roleName='label').showing
        self.assertTrue(time_check)
        self.assertTrue(date_check)

    def suite():
        suite = unittest.TestSuite()
        suite.addTest(Check_Topmain_Datetime('test_check_time'))
        return suite


if __name__ == "__main__":
    unittest.installHandler()
    LOCALE_DIR = os.path.abspath("./lib/locale")
    gettext.install('dsystem', LOCALE_DIR)
    executeTestCase.runTest(Check_Topmain_Datetime)
