#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os, time
import unittest
import gettext
from lib import runTest
from lib import dde_control_center

casename = "all-5374:显示控制中心各个模块"

class DCC_ShowModules(unittest.TestCase):
    caseid ='191817'
    @classmethod
    def setUpClass(cls):
        cls.dcc = dde_control_center.Dde_control_center()

    @classmethod
    def tearDownClass(cls):
        pass

    def testShowAllModules(self):
        modules_list = ['accounts',
                        'display',
                        'defapp',
                        'personalization',
                        'network',
                        'sound',
                        'datetime',
                        'power',
                        'mouse',
                        'keyboard',
                        'update',
                        'systeminfo'
                        ]
        for i in modules_list:
            print(i)
            ret = self.dcc.showModule(i)
            self.assertTrue(ret)
            self.dcc.page_deep += 1
            self.dcc.backToIndex()
            self.dcc.exit()

    def suite():
        suite = unittest.TestSuite()
        suite.addTest(DCC_ShowModules('testShowAllModules'))
        return suite

if __name__ == "__main__":
    unittest.installHandler()
    LOCALE_DIR = os.path.abspath("./lib/locale")
    gettext.install('dsystem', LOCALE_DIR)
    runTest(DCC_ShowModules)
