#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import unittest
from subprocess import getstatusoutput as rt
from subprocess import getoutput
from lib import utils
from lib import runner

result = True
caseid = '38980'
casename = 'all-1446:文件/文件夹操作命令--验证对file命令的支持'

class File(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.startTime = time.time()
        pass

    @classmethod
    def tearDownClass(cls):
        seconds = "%.3f" % (time.time() - cls.startTime)
        minutes = utils.convertToMinutes(float(seconds))
        global result
        utils.commitresult(caseid, result, minutes)

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

    class MyTestResult(runner.MyTextTestResult):
        def addError(self, test, err):
            super(File.MyTestResult, self).addError(test, err)
            global result
            result = result and False

        def addFailure(self, test, err):
            super(File.MyTestResult, self).addError(test, err)
            global result
            result = result and False

if __name__ == "__main__":
    unittest.TextTestRunner(resultclass=File.MyTestResult).run(File.suite())
