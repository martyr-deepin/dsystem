#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import unittest
from subprocess import getstatusoutput as rt
from subprocess import getoutput
from lib import runner
from lib import utils

result = True
caseid = '38961'
casename = 'all-1443:文件/文件夹操作命令--验证对cp命令的支持'

class Cp(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.startTime = time.time()
        cls.tmptestdir = "/tmp/testdir"
        cls.copytmptestdir = "/tmp/testdir1"
        cls.filepath   = "/tmp/testdir/testfile"
        cls.copyfilepath   = "/tmp/testdir1/testfile"
        cls.tmpdir     = "/tmp"
        cls.tmpfile    = "/tmp/testfile"

    @classmethod
    def tearDownClass(cls):
        seconds = "%.3f" % (time.time() - cls.startTime)
        minutes = utils.convertToMinutes(float(seconds))
        global result
        utils.commitresult(caseid, result, minutes)

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
        suite.addTest(Cp('test1CreateDir'))
        suite.addTest(Cp('test2CpFile'))
        suite.addTest(Cp('test3CpDir'))
        return suite

    class MyTestResult(runner.MyTextTestResult):
        def addError(self, test, err):
            super(Cp.MyTestResult, self).addError(test, err)
            global result
            result = result and False

        def addFailure(self, test, err):
            super(Cp.MyTestResult, self).addError(test, err)
            global result
            result = result and False

if __name__ == "__main__":
    unittest.TextTestRunner(resultclass=Cp.MyTestResult).run(Cp.suite())
