#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import getpass
import unittest
from subprocess import getstatusoutput as rt
from subprocess import getoutput
from lib import utils
from lib import runner

result = True
caseid = '39096'
casename = 'all-1464:其他命令--验证对who命令的支持'

class Who(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.startTime = time.time()
        cls.loginuser = getpass.getuser()

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

    def testWho(self):
        (status, output) = rt('who')
        self.assertTrue(0 == status)

        for line in output.split('\n'):
            linelist = line.split()
            self.assertTrue(self.loginuser == linelist[0])
            self.assertTrue('tty7' == linelist[1])
            break

    def suite():
        suite = unittest.TestSuite()
        suite.addTest(Who('testWho'))
        return suite

    class MyTestResult(runner.MyTextTestResult):
        def addError(self, test, err):
            super(Who.MyTestResult, self).addError(test, err)
            global result
            result = result and False

        def addFailure(self, test, err):
            super(Who.MyTestResult, self).addError(test, err)
            global result
            result = result and False

if __name__ == "__main__":
    unittest.TextTestRunner(resultclass=Who.MyTestResult).run(Who.suite())
