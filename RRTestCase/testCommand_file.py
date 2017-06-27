#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import unittest
from lib import executeTestCase
from subprocess import getstatusoutput as rt
from subprocess import getoutput
from lib import utils
from lib import runner

casename = 'all-5385:文件/文件夹操作命令--验证对file命令的支持'

class Command_file(unittest.TestCase):
    caseid = '192113'
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

    def testFileCommand(self):
        (status_ls, output_ls) = rt("which ls")
        self.assertTrue(0 == status_ls)
        self.assertTrue('/bin/ls' == output_ls)

        (status, output) = rt("file %s" % output_ls)
        self.assertTrue(0 == status)
        resultlist = output.split()
        self.assertEquals("/bin/ls:", resultlist[0])
        self.assertEquals("ELF", resultlist[1])
        self.assertEquals("64-bit", resultlist[2])
        self.assertEquals("LSB", resultlist[3])

    def suite():
        suite = unittest.TestSuite()
        suite.addTest(Command_file('testFileCommand'))
        return suite

if __name__ == "__main__":
    unittest.installHandler()
    executeTestCase.runTest(Command_file)
