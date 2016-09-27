#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import unittest
from subprocess import getstatusoutput as rt
from subprocess import getoutput
from lib import utils
from lib import runner

result = True

class Rm(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.caseid = '38975'
        cls.casename = 'all-1445:文件/文件夹操作命令--验证对rm命令的支持'
        cls.homedir = os.path.expanduser('~')
        cls.filename = "/".join((cls.homedir, 'testfile'))

    @classmethod
    def tearDownClass(cls):
        global result
        utils.commitresult(cls.caseid, result)

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
        suite.addTest(Rm('test1CreateFile'))
        suite.addTest(Rm('test2RmFile'))
        return suite

    class MyTestResult(runner.MyTextTestResult):
        def addError(self, test, err):
            super(Rm.MyTestResult, self).addError(test, err)
            global result
            result = result and False

        def addFailure(self, test, err):
            super(Rm.MyTestResult, self).addError(test, err)
            global result
            result = result and False

if __name__ == "__main__":
    unittest.TextTestRunner(resultclass=Rm.MyTestResult).run(Rm.suite())
