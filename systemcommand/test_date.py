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
caseid = '39107'
casename = 'all-1467:其他命令--验证对date命令的支持'

class Date(unittest.TestCase):
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

    def testDateOne(self):
        (status, output) = rt('date')
        self.assertTrue(0 == status)

        for line in output.split('\n'):
            linelist = line.split()
            self.assertTrue('CST' == linelist[len(linelist)-1])
            break

    def testDateTwo(self):
        (status, tmp) = rt('date -s "2009/11/11 17:00:00"')
        self.assertFalse(0 == status)

        (status, output) = rt('date')
        self.assertTrue(0 == status)
        self.assertFalse(output.startswith('2009'))

        (status, tmp) = rt('sudo date -s "2009/11/11 17:00:00"')
        (status, output) = rt('date')
        self.assertTrue(0 == status)
        self.assertTrue(output.startswith('2009'), "output: %s" % output)

    def suite():
        suite = unittest.TestSuite()
        suite.addTest(Date('testDateOne'))
        suite.addTest(Date('testDateTwo'))
        return suite

    class MyTestResult(runner.MyTextTestResult):
        def addError(self, test, err):
            super(Date.MyTestResult, self).addError(test, err)
            global result
            result = result and False

        def addFailure(self, test, err):
            super(Date.MyTestResult, self).addError(test, err)
            global result
            result = result and False

if __name__ == "__main__":
    unittest.TextTestRunner(resultclass=Date.MyTestResult).run(Date.suite())
