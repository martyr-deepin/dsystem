#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import unittest
from lib import executeTestCase
from subprocess import getstatusoutput as rt
from lib import utils
from lib import runner

result = True
caseid = '39072'
casename = 'all-1459:文件编辑命令--验证对vi命令的支持'

class Vi(unittest.TestCase):
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
        suite.addTest(Vi('testVi'))
        return suite

if __name__ == "__main__":
    runTest(Vi.suite())
