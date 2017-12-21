#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import gettext
import unittest
from time import sleep
from lib import executeTestCase
from lib import dde_control_center

casename = 'all-3849:主题-光标-默认'

class AppearanceCursorTheme(unittest.TestCase):
    caseid = '103587'
    @classmethod
    def setUpClass(cls):
        cls.dcc = dde_control_center.Dde_control_center()
        cls.defaultCursorTheme = dde_control_center.getAppearanceCursorTheme()

    @classmethod
    def tearDownClass(cls):
        if dde_control_center.getAppearanceCursorTheme() != cls.defaultCursorTheme:
            dde_control_center.setAppearanceCursorTheme('deepin')
        dde_control_center.Dde_control_center().hideDcc()

    def testCursorTheme(self):
        ret = self.dcc.showModule('personalization')
        self.assertTrue(ret)
        dde_control_center.Dde_control_center().dccObj.child('Theme').click()
        cursorTheme = dde_control_center.getAppearanceWindowTheme()
        self.assertEqual(cursorTheme, 'deepin')

    def suite():
        suite = unittest.TestSuite()
        suite.addTest(AppearanceCursorTheme('testCursorTheme'))
        return suite

if __name__ == "__main__":
    unittest.installHandler()
    LOCALE_DIR = os.path.abspath("./lib/locale")
    gettext.install('dsystem', LOCALE_DIR)
    executeTestCase.runTest(AppearanceCursorTheme)
