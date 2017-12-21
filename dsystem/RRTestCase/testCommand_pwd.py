#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import unittest
from lib import executeTestCase
from subprocess import getstatusoutput as rt
from lib import utils
from lib import runner

casename = 'all-5378:文件/文件夹操作命令--验证对pwd命令的支持'

class Command_pwd(unittest.TestCase):
    caseid = '192074'
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
        suite.addTest(Command_pwd('testPath'))
        return suite

if __name__ == "__main__":
    unittest.installHandler()
    executeTestCase.runTest(Command_pwd)
