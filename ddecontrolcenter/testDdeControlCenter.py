#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import unittest
import time
from lib import executeTestCase
from lib import utils
from lib import dde_control_center
from dogtail.tree import root
import gettext

casename = "all-4222:默认程序首页"

class ControlCenter(unittest.TestCase):
    caseid = '105635'
    @classmethod
    def setUpClass(cls):
        cls.dcc = dde_control_center.Dde_control_center()
        cls.string_Default_Applications = _('Default Applications')
        cls.string_Browser = _('Browser')
        cls.string_Mail = _('Mail')
        cls.string_Text = _('Text')
        cls.string_Music = _('Music')
        cls.string_Video = _('Video')
        cls.string_Picture = _('Picture')
        cls.string_Terminal = _('Terminal')
        cls.string_CD_Audio = _('CD Audio')
        cls.string_DVD_Video = _('DVD Video')
        cls.string_Music_Player = _('Music Player')
        cls.string_Camera = _('Camera')
        cls.string_Software = _('Software')

    @classmethod
    def tearDownClass(cls):
        cls.dcc.clickBack()
        cls.dcc.clickBack()
        cls.dcc.clickScreenCenter()

    def testOpenDdeControlCenter(self):
        self.assertTrue(self.dcc.openGUI())
        self.assertTrue(self.dcc.openModule(self.string_Default_Applications))
        openbutton = self.dcc.dccObj.child(self.string_Default_Applications,
            roleName='filler')
        openbutton.click()
        frame1 = self.dcc.dccObj.child(self.string_Browser, roleName='frame')
        frame2 = self.dcc.dccObj.child(self.string_Mail, roleName='frame')
        frame3 = self.dcc.dccObj.child(self.string_Text, roleName='frame')
        frame4 = self.dcc.dccObj.child(self.string_Music, roleName='frame')
        frame5 = self.dcc.dccObj.child(self.string_Video, roleName='frame')
        frame6 = self.dcc.dccObj.child(self.string_Picture, roleName='frame')
        frame7 = self.dcc.dccObj.child(self.string_Terminal, roleName='frame')
        frame8 = self.dcc.dccObj.child(self.string_CD_Audio, roleName='frame')
        frame9 = self.dcc.dccObj.child(self.string_DVD_Video, roleName='frame')
        frame10 = self.dcc.dccObj.child(self.string_Music_Player,
                roleName='frame')
        frame11 = self.dcc.dccObj.child(self.string_Camera, roleName='frame')
        frame12 = self.dcc.dccObj.child(self.string_Software, roleName='frame')

        self.assertTrue(frame1.position[0] == frame2.position[0])
        self.assertTrue(frame1.position[1] < frame2.position[1])

        self.assertTrue(frame2.position[0] == frame3.position[0])
        self.assertTrue(frame2.position[1] < frame3.position[1])

        self.assertTrue(frame3.position[0] == frame4.position[0])
        self.assertTrue(frame3.position[1] < frame4.position[1])

        self.assertTrue(frame4.position[0] == frame5.position[0])
        self.assertTrue(frame4.position[1] < frame5.position[1])

        self.assertTrue(frame5.position[0] == frame6.position[0])
        self.assertTrue(frame5.position[1] < frame6.position[1])

        self.assertTrue(frame6.position[0] == frame7.position[0])
        self.assertTrue(frame6.position[1] < frame7.position[1])

        self.assertTrue(frame7.position[0] == frame8.position[0])
        self.assertTrue(frame7.position[1] < frame8.position[1])

        self.assertTrue(frame8.position[0] == frame9.position[0])
        self.assertTrue(frame8.position[1] < frame9.position[1])

        self.assertTrue(frame9.position[0] == frame10.position[0],
                "frame9.x = %s, frame10.x = %s" % (str(frame9.position),
                    str(frame10.position)))
        self.assertTrue(frame9.position[1] < frame10.position[1])

        self.assertTrue(frame10.position[0] == frame11.position[0])
        self.assertTrue(frame10.position[1] < frame11.position[1])

        self.assertTrue(frame11.position[0] == frame12.position[0])
        self.assertTrue(frame11.position[1] < frame12.position[1])

    def suite():
        suite = unittest.TestSuite()
        suite.addTest(ControlCenter('testOpenDdeControlCenter'))

        return suite

if __name__ == "__main__":
    LOCALE_DIR = os.path.abspath("./lib/locale")
    gettext.install('dsystem', LOCALE_DIR)
    executeTestCase.runTest(ControlCenter)
