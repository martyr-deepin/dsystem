#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import getpass
import unittest
from lib import executeTestCase
from subprocess import getstatusoutput as rt
from subprocess import getoutput

casename = 'all-1465:其他命令--验证对whoami命令的支持'

class Command_whoami(unittest.TestCase):
    caseid = '192253'
    @classmethod
    def setUpClass(cls):
        cls.loginuser = getpass.getuser()

    @classmethod
    def tearDownClass(cls):
        pass
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testWhoami(self):
        (status, output) = rt('whoami')
        self.assertTrue(0 == status)
        self.assertTrue(output == self.loginuser)

    def suite():
        suite = unittest.TestSuite()
        suite.addTest(Command_whoami('testWhoami'))
        return suite

if __name__ == "__main__":
    unittest.installHandler()
    executeTestCase.runTest(Command_whoami)
