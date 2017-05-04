#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import unittest
import gettext
from lib import executeTestCase
from lib import dde_control_center

casename = "all-5357:首页亮度调节"

class DCC_Click_LightSlider(unittest.TestCase):
    caseid ='191667'
    @classmethod
    def setUpClass(cls):
        cls.dcc = dde_control_center.Dde_control_center()

    @classmethod
    def tearDownClass(cls):
        cls.dcc.backToIndex()
        cls.dcc.exit()

    def testClickLightSlider(self):
        lightslider = 'LightSlider'
        show_check = self.dcc.showDcc()
        self.assertTrue(show_check)
        self.dcc.dccObj.child(lightslider, roleName='slider').click()

    def suite():
        suite = unittest.TestSuite()
        suite.addTest(Click_LightSlider('testClickLightSlider'))
        return suite

if __name__ == "__main__":
    unittest.installHandler()
    LOCALE_DIR = os.path.abspath("./lib/locale")
    gettext.install('dsystem', LOCALE_DIR)
    executeTestCase.runTest(Click_LightSlider)
