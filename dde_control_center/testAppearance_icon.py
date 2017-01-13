#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from time import sleep
from lib import executeTestCase
from lib import dde_control_center

casename = 'all-3855:图标-默认'

class AppearanceIconTheme(unittest.TestCase):
    caseid = '103610'
    @classmethod
    def setUpClass(cls):
        cls.defaultIconTheme = dde_control_center.getAppearanceIconTheme()

    @classmethod
    def tearDownClass(cls):
        if dde_control_center.getAppearanceIconTheme() != cls.defaultIconTheme:
            dde_control_center.setAppearanceIconTheme('deepin')
        dde_control_center.Dde_control_center().hideDcc()

    def testIconTheme(self):
        dde_control_center.Dde_control_center().showModule('Personalization')
        sleep(1)
        dde_control_center.Dde_control_center().dccObj.child('Theme').click()
        iconTheme = dde_control_center.getAppearanceIconTheme()
        self.assertEqual(iconTheme, 'deepin')

    def suite():
        suite = unittest.TestSuite()
        suite.addTest(AppearanceIconTheme('testIconTheme'))
        return suite

if __name__ == "__main__":
    executeTestCase.runTest(AppearanceIconTheme)
