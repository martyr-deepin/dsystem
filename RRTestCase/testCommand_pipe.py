#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import unittest
from lib import executeTestCase
from subprocess import getstatusoutput as rt
from subprocess import getoutput

casename = 'all-5416:其他命令--验证对管道的支持'

class Command_pipe(unittest.TestCase):
    caseid = '192275'
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

    def testPipe(self):
        (status, output) = rt("ifconfig lo | sed 's/://g' | grep \"inet\" | grep -v \"inet6\" | awk '{print $2}'")
        self.assertTrue('127.0.0.1' == output)

    def suite():
        suite = unittest.TestSuite()
        suite.addTest(Command_pipe('testPipe'))
        return suite

if __name__ == "__main__":
    unittest.installHandler()
    executeTestCase.runTest(Command_pipe)
