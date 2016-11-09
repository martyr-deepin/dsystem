#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import unittest
from subprocess import getstatusoutput as rt
from lib import utils
from lib import runner

result = True
caseid = '39072'
casename = 'all-1459:文件编辑命令--验证对vi命令的支持'

class Vi(unittest.TestCase):
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

    def testVi(self):
        (status, output) = rt('which vi')
        self.assertTrue(0 == status)
        self.assertTrue('/usr/bin/vi' == output)

    def suite():
        suite = unittest.TestSuite()
        suite.addTest(Vi('testVi'))
        return suite

    class MyTestResult(runner.MyTextTestResult):
        def addError(self, test, err):
            super(Vi.MyTestResult, self).addError(test, err)
            global result
            result = result and False

        def addFailure(self, test, err):
            super(Vi.MyTestResult, self).addError(test, err)
            global result
            result = result and False

if __name__ == "__main__":
    unittest.TextTestRunner(resultclass=Vi.MyTestResult).run(Vi.suite())
