#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from time import localtime, strftime
import unittest
import gettext
from lib import executeTestCase
from lib import dde_control_center
from lib import LangSelector

casename = "all-4608:不同语言地区系统时间首页显示测试"

class Change_Topmain_Languge(unittest.TestCase):
    caseid ='113391'

    @classmethod
    def setUpClass(cls):
        cls.dcc = dde_control_center.Dde_control_center()
        cls.ls  = LangSelector()

    @classmethod
    def tearDownClass(cls):
        # set languge using '简体中文'
        cls.ls.SetLocale('zh_CN.UTF-8')
        cls.dcc.exit()

    def test_change_languge(self):
        self.dcc.showModule('keyboard')

        # set languge using 'Suomi'
        self.ls.SetLocale('fi_FI.UTF-8')

        self.dcc.page_deep += 1
        self.dcc.backToIndex()

    def suite():
        suite = unittest.TestSuite()
        suite.addTest(Change_Topmain_Languge('test_change_languge'))
        return suite

if __name__ == "__main__":
    unittest.installHandler()
    LOCALE_DIR = os.path.abspath("./lib/locale")
    gettext.install('dsystem', LOCALE_DIR)
    executeTestCase.runTest(Change_Topmain_Languge)
