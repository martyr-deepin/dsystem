#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import unittest
from subprocess import getstatusoutput as rt
from subprocess import getoutput
from lib import runner
from lib import utils

result = True
caseid = '39052'
casename = 'all-1456:备份、压缩和解压缩操作命令--验证对gunzip命令的支持'

class Gunzip(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.startTime = time.time()
        cls.testfile    = "testfile"
        cls.gzipfile    = "testfile.gz"

    @classmethod
    def tearDownClass(cls):
        seconds = %.3f % (time.time() - cls.startTime)
        minutes = utils.convertToMinutes(float(seconds))
        global result
        utils.commitresult(caseid, result, minutes)

        if os.path.exists(cls.testfile):
            os.remove(cls.testfile)

        if os.path.exists(cls.gzipfile):
            os.remove(cls.gzipfile)

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testGunzipOne(self):
        os.system("touch %s" % self.testfile)
        self.assertTrue(os.path.exists(self.testfile))

        os.system("gzip %s" % self.testfile)
        self.assertFalse(os.path.exists(self.testfile))
        self.assertTrue(os.path.exists(self.gzipfile))

    def testGunzipTwo(self):
        os.system("gzip -d %s" % self.gzipfile)
        self.assertTrue(os.path.exists(self.testfile))
        self.assertFalse(os.path.exists(self.gzipfile))

    def suite():
        suite = unittest.TestSuite()
        suite.addTest(Gunzip('testGunzipOne'))
        suite.addTest(Gunzip('testGunzipTwo'))
        return suite

    class MyTestResult(runner.MyTextTestResult):
        def addError(self, test, err):
            super(Gunzip.MyTestResult, self).addError(test, err)
            global result
            result = result and False

        def addFailure(self, test, err):
            super(Gunzip.MyTestResult, self).addError(test, err)
            global result
            result = result and False

if __name__ == "__main__":
    unittest.TextTestRunner(resultclass=Gunzip.MyTestResult).run(Gunzip.suite())
