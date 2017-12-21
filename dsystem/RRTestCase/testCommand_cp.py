#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import unittest
from lib import executeTestCase
from subprocess import getstatusoutput as rt
from subprocess import getoutput
from lib import runner
from lib import utils

casename = 'all-5382:文件/文件夹操作命令--验证对cp命令的支持'

class Command_cp(unittest.TestCase):
    caseid = '192094'
    @classmethod
    def setUpClass(cls):
        cls.tmptestdir = "/tmp/testdir"
        cls.copytmptestdir = "/tmp/testdir1"
        cls.filepath   = "/tmp/testdir/testfile"
        cls.copyfilepath   = "/tmp/testdir1/testfile"
        cls.tmpdir     = "/tmp"
        cls.tmpfile    = "/tmp/testfile"

    @classmethod
    def tearDownClass(cls):
        os.system("rm -rf %s %s %s" % (cls.tmptestdir, cls.copytmptestdir, cls.tmpfile))

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test1CreateDir(self):
        self.assertFalse(os.path.exists(self.tmptestdir))
        os.system("mkdir %s" % self.tmptestdir)
        self.assertTrue(os.path.exists(self.tmptestdir))
        os.system("touch %s" % self.filepath)
        os.system("echo test > %s" % self.filepath)
        self.assertTrue(os.path.exists(self.filepath))

    def test2CpFile(self):
        self.assertFalse(os.path.exists(self.tmpfile))
        os.system("cp -a %s %s" % (self.filepath, self.tmpdir))
        self.assertTrue(os.path.exists(self.tmpfile))

    def test3CpDir(self):
        self.assertFalse(os.path.exists(self.copytmptestdir))
        os.system("cp -r %s %s" %(self.tmptestdir, self.copytmptestdir))
        self.assertTrue(os.path.exists(self.copytmptestdir))
        self.assertTrue(os.path.exists(self.copyfilepath))

    def suite():
        suite = unittest.TestSuite()
        suite.addTest(Command_cp('test1CreateDir'))
        suite.addTest(Command_cp('test2CpFile'))
        suite.addTest(Command_cp('test3CpDir'))
        return suite

if __name__ == "__main__":
    unittest.installHandler()
    executeTestCase.runTest(Command_cp)
