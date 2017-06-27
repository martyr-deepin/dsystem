#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import unittest
from lib import executeTestCase
from subprocess import getstatusoutput as rt

casename = 'all-5405:文件编辑命令--验证对vi命令的支持'

class Command_vi(unittest.TestCase):
    caseid = '192226'
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

    def testVi(self):
        (status, output) = rt('which vi')
        self.assertTrue(0 == status)
        self.assertTrue('/usr/bin/vi' == output)

    def suite():
        suite = unittest.TestSuite()
        suite.addTest(Command_vi('testVi'))
        return suite

if __name__ == "__main__":
    unittest.installHandler()
    executeTestCase.runTest(Command_vi)
