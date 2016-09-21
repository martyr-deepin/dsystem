#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import unittest
from subprocess import getstatusoutput as rt
from subprocess import getoutput
from lib import utils
from lib import runner

result = True

class Rmdir(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.caseid = '38957'
        cls.casename = 'all-1442:文件/文件夹操作命令--验证对rmdir命令的支持'
        cls.loginuser = getoutput("whoami")
        cls.curdir = getoutput("pwd")
        cls.testdir = "testdir"

    @classmethod
    def tearDownClass(cls):
        global result
        utils.commitresult(cls.caseid, result)

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

    class MyTestResult(runner.MyTextTestResult):
        def addError(self, test, err):
            super(Rmdir.MyTestResult, self).addError(test, err)
            global result
            result = result and False

        def addFailure(self, test, err):
            super(Rmdir.MyTestResult, self).addError(test, err)
            global result
            result = result and False

if __name__ == "__main__":
    unittest.TextTestRunner(resultclass=Rmdir.MyTestResult).run(Rmdir.suite())
