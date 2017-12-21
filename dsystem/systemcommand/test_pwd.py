#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import unittest
from lib import executeTestCase
from subprocess import getstatusoutput as rt
from lib import utils
from lib import runner

result = True
casename = 'all-1439:文件/文件夹操作命令--验证对pwd命令的支持'

class Pwd(unittest.TestCase):
    caseid = '38941'
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

    def testPath(self):
        (status, output) = rt("cd /tmp && pwd")
        self.assertTrue(0 == status)
        self.assertEqual(output, '/tmp')

    def suite():
        suite = unittest.TestSuite()
        suite.addTest(Pwd('testPath'))
        return suite

if __name__ == "__main__":
    executeTestCase.runTest(Pwd)
