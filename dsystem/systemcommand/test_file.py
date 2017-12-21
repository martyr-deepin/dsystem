#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import unittest
from lib import executeTestCase
from subprocess import getstatusoutput as rt
from subprocess import getoutput
from lib import utils
from lib import runner

result = True
casename = 'all-1446:文件/文件夹操作命令--验证对file命令的支持'

class File(unittest.TestCase):
    caseid = '38980'
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
        self.assertEquals("executable,", resultlist[4])

    def suite():
        suite = unittest.TestSuite()
        suite.addTest(File('testFileCommand'))
        return suite

if __name__ == "__main__":
    executeTestCase.runTest(File)
