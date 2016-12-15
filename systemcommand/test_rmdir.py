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
caseid = '38957'
casename = 'all-1442:文件/文件夹操作命令--验证对rmdir命令的支持'

class Rmdir(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.loginuser = getoutput("whoami")
        cls.curdir = getoutput("pwd")
        cls.testdir = "testdir"

    @classmethod
    def tearDownClass(cls):
        pass
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test1CreateDir(self):
        fullpath = "%s/%s" % (self.curdir, self.testdir)
        self.assertFalse(os.path.exists(fullpath))
        os.system("mkdir %s" % self.testdir)
        self.assertTrue(os.path.exists(fullpath))
        self.assertTrue(os.path.isdir(fullpath))

    def test2RmoveDir(self):
        fullpath = "%s/%s" % (self.curdir, self.testdir)
        (status, output) = rt("rmdir testdir")
        self.assertTrue(0 == status)
        self.assertFalse(os.path.exists(fullpath))
        self.assertFalse(os.path.isdir(fullpath))


    def suite():
        suite = unittest.TestSuite()
        suite.addTest(Rmdir('test1CreateDir'))
        suite.addTest(Rmdir('test2RmoveDir'))
        return suite

if __name__ == "__main__":
    runTest(Rmdir.suite())
