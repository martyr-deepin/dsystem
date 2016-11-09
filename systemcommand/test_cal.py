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
caseid = '39104'
casename = 'all-1466:其他命令--验证对cal命令的支持'

class Cal(unittest.TestCase):
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

    def testCal(self):
        (status, output) = rt('cal')
        self.assertTrue(0 == status)

        for line in output.split('\n'):
            linelist = line.split()
            month = getoutput('date "+%B"')
            year  = getoutput('date "+%Y"')
            self.assertTrue(month == linelist[0])
            self.assertTrue(year == linelist[1])
            break

    def suite():
        suite = unittest.TestSuite()
        suite.addTest(Cal('testCal'))
        return suite

    class MyTestResult(runner.MyTextTestResult):
        def addError(self, test, err):
            super(Cal.MyTestResult, self).addError(test, err)
            global result
            result = result and False

        def addFailure(self, test, err):
            super(Cal.MyTestResult, self).addError(test, err)
            global result
            result = result and False

if __name__ == "__main__":
    unittest.TextTestRunner(resultclass=Cal.MyTestResult).run(Cal.suite())
