#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import unittest
from subprocess import getstatusoutput as rt
from subprocess import getoutput
from lib import runner
from lib import utils

result = True
caseid = '39121'
casename = 'all-1470:其他命令--验证对管道的支持'

class Pipe(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        global result
        utils.commitresult(caseid, result)

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testPipe(self):
        (status, output) = rt("ifconfig lo | sed 's/://g' | grep \"inet\" | grep -v \"inet6\" | awk '{print $2}'")
        self.assertTrue('127.0.0.1' == output)

    def suite():
        suite = unittest.TestSuite()
        suite.addTest(Pipe('testPipe'))
        return suite

    class MyTestResult(runner.MyTextTestResult):
        def addError(self, test, err):
            super(Pipe.MyTestResult, self).addError(test, err)
            global result
            result = result and False

        def addFailure(self, test, err):
            super(Pipe.MyTestResult, self).addError(test, err)
            global result
            result = result and False

if __name__ == "__main__":
    unittest.TextTestRunner(resultclass=Pipe.MyTestResult).run(Pipe.suite())
