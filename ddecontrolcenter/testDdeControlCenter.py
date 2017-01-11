#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
import time
from lib import executeTestCase
from lib import utils
from lib import dde_control_center
from dogtail.tree import root

casename = "all-4222:默认程序首页"

class ControlCenter(unittest.TestCase):
    caseid = '105635'
    @classmethod
    def setUpClass(cls):
        cls.dcc = dde_control_center.Dde_control_center()

    @classmethod
    def tearDownClass(cls):
        cls.dcc.clickBack()
        cls.dcc.clickBack()
        cls.dcc.clickScreenCenter()

    def testOpenDdeControlCenter(self):
        self.assertTrue(self.dcc.openGUI())
        self.assertTrue(self.dcc.openModule('Default Applications'))
        openbutton = self.dcc.dccObj.child('Default Applications', roleName='filler')
        openbutton.click()
        frame1 = self.dcc.dccObj.child('Browser', roleName='label')
        frame2 = self.dcc.dccObj.child('Mail', roleName='label')
        frame3 = self.dcc.dccObj.child('Text', roleName='label')
        frame4 = self.dcc.dccObj.child('Music', roleName='label')
        frame5 = self.dcc.dccObj.child('Video', roleName='label')
        frame6 = self.dcc.dccObj.child('Picture', roleName='label')
        frame7 = self.dcc.dccObj.child('Terminal', roleName='label')
        frame8 = self.dcc.dccObj.child('CD Audio', roleName='label')
        frame9 = self.dcc.dccObj.child('DVD Video', roleName='label')
        frame10 = self.dcc.dccObj.child('Music Player', roleName='label')
        frame11 = self.dcc.dccObj.child('Camera', roleName='label')
        frame12 = self.dcc.dccObj.child('Software', roleName='label')

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

        self.assertTrue(frame9.position[0] == frame10.position[0])
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
    executeTestCase.runTest(ControlCenter)
