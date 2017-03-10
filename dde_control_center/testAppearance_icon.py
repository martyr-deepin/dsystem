#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import gettext
import unittest
from time import sleep
from lib import executeTestCase
from lib import dde_control_center

casename = 'all-3855:图标-默认'

class AppearanceIconTheme(unittest.TestCase):
    caseid = '103610'
    @classmethod
    def setUpClass(cls):
        cls.dcc = dde_control_center.Dde_control_center()
        cls.defaultIconTheme = dde_control_center.getAppearanceIconTheme()

    @classmethod
    def tearDownClass(cls):
        if dde_control_center.getAppearanceIconTheme() != cls.defaultIconTheme:
            dde_control_center.setAppearanceIconTheme('deepin')

        dde_control_center.Dde_control_center().hideDcc()

    def testIconTheme(self):
        ret = self.dcc.showModule('Personalization')
        self.assertTrue(ret)
        self.dcc.dccObj.child('Theme').click()
        iconTheme = dde_control_center.getAppearanceIconTheme()
        self.assertEqual(iconTheme, 'deepin')

    def suite():
        suite = unittest.TestSuite()
        suite.addTest(AppearanceIconTheme('testIconTheme'))
        return suite

if __name__ == "__main__":
    unittest.installHandler()
    LOCALE_DIR = os.path.abspath("./lib/locale")
    gettext.install('dsystem', LOCALE_DIR)
    executeTestCase.runTest(AppearanceIconTheme)
