#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os, time
from time import localtime, strftime
import unittest
import gettext
from lib import executeTestCase, utils
from lib import dde_control_center
from lib.com_deepin_daemon_Timedate import Timedate

casename = "all-3832:切换时区之后系统时间首页显示"

class Change_Topmain_Timezone(unittest.TestCase):
    caseid ='103496'

    @classmethod
    def setUpClass(cls):
        cls.dcc = dde_control_center.Dde_control_center()
        cls.td  = Timedate()

    @classmethod
    def tearDownClass(cls):
        cls.dcc.exit()
        cls.td.SetTimezone('Asia/Shanghai')


    def test_change_timezone(self):
        self.dcc.showModule('datetime')
        self.td.SetTimezone('America/Belem')
        c_time = strftime('%H:%M', localtime())
        print(c_time)
        self.dcc.page_deep += 1
        self.dcc.backToIndex()
        time_check = self.dcc.dccObj.child(c_time, roleName='label').showing
        self.assertTrue(time_check)

    def suite():
        suite = unittest.TestSuite()
        suite.addTest(Change_Topmain_Timezone('test_change_timezone'))
        return suite

if __name__ == "__main__":
    unittest.installHandler()
    LOCALE_DIR = os.path.abspath("./lib/locale")
    gettext.install('dsystem', LOCALE_DIR)
    executeTestCase.runTest(Change_Topmain_Timezone)
