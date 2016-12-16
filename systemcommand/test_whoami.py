#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import getpass
import unittest
from lib import executeTestCase
from subprocess import getstatusoutput as rt
from subprocess import getoutput
from lib import utils
from lib import runner

result = True
casename = 'all-1465:其他命令--验证对whoami命令的支持'

class Whoami(unittest.TestCase):
    caseid = '39099'
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
        suite.addTest(Whoami('testWhoami'))
        return suite

if __name__ == "__main__":
    executeTestCase.runTest(Whoami)
