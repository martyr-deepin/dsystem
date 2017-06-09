#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import getpass
import unittest
from time import sleep
from lib import executeTestCase
from subprocess import getstatusoutput as rt
from subprocess import getoutput

casename = 'all-1467:其他命令--验证对date命令的支持'

class Command_date(unittest.TestCase):
    caseid = '192261'
    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass
    def setUp(self):
        pass

    def tearDown(self):
        sleep(5)

    def testDateOne(self):
        (status, output) = rt('date')
        self.assertTrue(0 == status)

        for line in output.split('\n'):
            linelist = line.split()
            self.assertTrue('CST' == linelist[len(linelist)-2])
            break

    def testDateTwo(self):
        (status, tmp) = rt('date -s "2009/11/11 17:00:00"')
        self.assertFalse(0 == status)

        (status, output) = rt('date')
        self.assertTrue(0 == status)
        self.assertFalse(output.startswith('2009'))

        (status, tmp) = rt('sudo date -s "2009/11/11 17:00:00"')
        (status, output) = rt('date')
        self.assertTrue(0 == status)
        self.assertTrue(output.endswith('2009'), "output: %s" % output)

    def suite():
        suite = unittest.TestSuite()
        suite.addTest(Command_date('testDateOne'))
        suite.addTest(Command_date('testDateTwo'))
        return suite

if __name__ == "__main__":
    unittest.installHandler()
    executeTestCase.runTest(Command_date)
