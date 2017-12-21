#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import getpass
import unittest
from lib import executeTestCase
from subprocess import getstatusoutput as rt
from subprocess import getoutput

casename = 'all-1466:其他命令--验证对cal命令的支持'

class Command_cal(unittest.TestCase):
    caseid = '192258'
    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testCal(self):
        (status, output) = rt('cal')
        self.assertTrue(0 == status)

        for line in output.split('\n'):
            linelist = line.split()
            month = getoutput('date "+%B"')
            year  = getoutput('date "+%Y"')
            self.assertTrue(month == linelist[0])
            self.assertTrue(year == linelist[1])
            break

    def suite():
        suite = unittest.TestSuite()
        suite.addTest(Command_cal('testCal'))
        return suite

if __name__ == "__main__":
    unittest.installHandler()
    executeTestCase.runTest(Command_cal)
