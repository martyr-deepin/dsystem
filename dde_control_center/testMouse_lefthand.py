#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import gettext
import unittest
from time import sleep
from lib import executeTestCase
from lib import dde_control_center

casename = 'all-3986:鼠标-左手使用'

class MouseSwitchLeftHand(unittest.TestCase):
    caseid = '104504'
    @classmethod
    def setUpClass(cls):
        cls.dcc = dde_control_center.Dde_control_center()
        cls.dcc.showModule('mouse')
        cls.defaultLeftHanded = dde_control_center.getMouseLeftHanded()
        cls.defaultNaturalScroll = dde_control_center.getMouseNaturalScroll()

    @classmethod
    def tearDownClass(cls):
        dde_control_center.Dde_control_center().hideDcc()

    def testSwitchMouseLeftHanded1(self):
        dde_control_center.Dde_control_center().dccObj.child(self.dcc.string_Mouse_Left_Hand).click()
        self.assertEqual(self.defaultLeftHanded, 1)

    def testSwitchMouseLeftHanded2(self):
        dde_control_center.Dde_control_center().dccObj.child(self.dcc.string_Mouse_Natural_Scrolling).click()
        self.assertEqual(self.defaultNaturalScroll, 0)

    def suite():
        suite = unittest.TestSuite()
        suite.addTest(MouseSwitchLeftHand('testSwitchMouseLeftHanded1'))
        suite.addTest(MouseSwitchLeftHand('testSwitchMouseLeftHanded2'))
        return suite

if __name__ == "__main__":
    unittest.installHandler()
    LOCALE_DIR = os.path.abspath("./lib/locale")
    gettext.install('dsystem', LOCALE_DIR)
    executeTestCase.runTest(MouseSwitchLeftHand)
