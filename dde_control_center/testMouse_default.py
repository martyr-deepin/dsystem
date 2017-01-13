#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from time import sleep
from lib import executeTestCase
from lib import dde_control_center

casename = 'all-3984:鼠标和触控板默认设置'

class MouseDefault(unittest.TestCase):
    caseid = '104495'
    @classmethod
    def setUpClass(cls):
        dde_control_center.Dde_control_center().showDcc()
        cls.defaultLeftHanded = dde_control_center.getMouseLeftHanded()
        cls.defaultNaturalScroll = dde_control_center.getMouseNaturalScroll()
        cls.defaultDisableTPad = dde_control_center.getMouseDisableTpad()
        cls.defaultDisableIfTyping = dde_control_center.getTouchPadDisableIfTyping()


    @classmethod
    def tearDownClass(cls):
        dde_control_center.Dde_control_center().hideDcc()

    def testMouseLeftHanded(self):
        self.assertEqual(self.defaultLeftHanded, 0)

    def testMouseNaturalScroll(self):
        self.assertEqual(self.defaultNaturalScroll, 0)

    def testMouseDisableTpad(self):
        self.assertEqual(self.defaultDisableTPad, 0)

    def testTouchPadDisableIfTyping(self):
        self.assertEqual(self.defaultDisableIfTyping, 0)

    def suite():
        suite = unittest.TestSuite()
        suite.addTest(MouseDefault('testMouseLeftHanded'))
        suite.addTest(MouseDefault('testMouseNaturalScroll'))
        suite.addTest(MouseDefault('testMouseDisableTpad'))
        suite.addTest(MouseDefault('testTouchPadDisableIfTyping'))
        return suite

if __name__ == "__main__":
    executeTestCase.runTest(MouseDefault)
