#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import unittest
from lib import executeTestCase
from subprocess import getstatusoutput as rt
from subprocess import getoutput
from lib import utils
from lib import runner

casename = 'all-5384:文件/文件夹操作命令--验证对rm命令的支持'

class Command_rm(unittest.TestCase):
    caseid = '192108'
    @classmethod
    def setUpClass(cls):
        cls.homedir = os.path.expanduser('~')
        cls.filename = "/".join((cls.homedir, 'testfile'))

    @classmethod
    def tearDownClass(cls):
        if os.path.exists(cls.filename):
            os.system('rm %s' % cls.filename)

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test1CreateFile(self):
        self.assertFalse(os.path.exists(self.filename))
        os.system("touch %s" % self.filename)
        self.assertTrue(os.path.exists(self.filename))
        self.assertTrue(os.path.isfile(self.filename))

    def test2RmFile(self):
        (status, output) = rt("rm %s" % self.filename)
        self.assertTrue(0 == status)
        self.assertFalse(os.path.exists(self.filename))

    def suite():
        suite = unittest.TestSuite()
        suite.addTest(Command_rm('test1CreateFile'))
        suite.addTest(Command_rm('test2RmFile'))
        return suite

if __name__ == "__main__":
    unittest.installHandler()
    executeTestCase.runTest(Command_rm)
