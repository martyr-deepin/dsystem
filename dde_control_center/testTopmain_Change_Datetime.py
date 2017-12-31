#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os, time
from pykeyboard import PyKeyboard
from pymouse import PyMouse
from time import localtime, strftime
import unittest
import gettext
from lib import executeTestCase
from lib import dde_control_center
from lib.com_deepin_daemon_Accounts import Accounts, User
from lib.com_deepin_SessionManager import SessionManager
from lib.com_deepin_daemon_Timedate  import  Timedate

casename = "all-3823:系统时间更新之后首页显示"

class Change_Topmain_Datetime(unittest.TestCase):
    caseid ='103456'

    @classmethod
    def setUpClass(cls):
        cls.dcc = dde_control_center.Dde_control_center()
        cls.td = Timedate()

    @classmethod
    def tearDownClass(cls):
        pass

    def tearDown(self):
        self.dcc.exit()

    def test_changetime_ui(self):
        #close auto-sync
        self.td.SetNTP(0)

        k = PyKeyboard()
        m = PyMouse()
        c_hour = strftime('%H', localtime())
        new_hour = int(c_hour) + 1
        self.dcc.showModule('datetime')
        self.dcc.dccObj.child('Time Settings', roleName='frame').click()
        time.sleep(1)
        k.press_key('Tab')
        k.release_key('Tab')
        time.sleep(1)
        k.type_string(str(new_hour))
        time.sleep(1)
        (x, y) = m.position()
        print(x+95, y+69)
        m.click(x+95, y+69)
        time.sleep(2)

        changed_hour = strftime('%H', localtime())
        print(new_hour, changed_hour)
        self.assertTrue(int(new_hour) == int(changed_hour))

        self.dcc.page_deep += 2
        self.dcc.backToIndex()

    def test_changetime_backstage(self):
        update_time = 'sudo date -s "23:59:59 2017-12-31"'

        #close auto-sync
        self.td.SetNTP(0)
        os.system(update_time)
        self.dcc.showDcc()
        time.sleep(3)
        time_check = self.dcc.dccObj.child('00:00', roleName='label').showing
        self.assertTrue(time_check)

    def suite():
        suite = unittest.TestSuite()
        suite.addTest(Change_Topmain_Datetime('test_changetime_ui'))
        suite.addTest(Change_Topmain_Datetime('test_changetime_backstage'))
        return suite


if __name__ == "__main__":
    unittest.installHandler()
    LOCALE_DIR = os.path.abspath("./lib/locale")
    gettext.install('dsystem', LOCALE_DIR)
    executeTestCase.runTest(Change_Topmain_Datetime)
