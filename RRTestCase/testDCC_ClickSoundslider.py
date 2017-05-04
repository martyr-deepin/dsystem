#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import unittest
import gettext
from lib import executeTestCase
from lib import dde_control_center

casename = "all-5356:首页声音调节"

class DCC_Click_SoundSlider(unittest.TestCase):
    caseid ='191665'
    @classmethod
    def setUpClass(cls):
        cls.dcc = dde_control_center.Dde_control_center()

    @classmethod
    def tearDownClass(cls):
        cls.dcc.backToIndex()
        cls.dcc.exit()

    def testClickSoundSlider(self):
        soundslider = 'SoundSlider'
        show_check = self.dcc.showDcc()
        self.assertTrue(show_check)
        self.dcc.dccObj.child(soundslider, roleName='slider').click()

    def suite():
        suite = unittest.TestSuite()
        suite.addTest(Click_SoundSlider('testClickSoundSlider'))
        return suite

if __name__ == "__main__":
    unittest.installHandler()
    LOCALE_DIR = os.path.abspath("./lib/locale")
    gettext.install('dsystem', LOCALE_DIR)
    executeTestCase.runTest(Click_SoundSlider)
