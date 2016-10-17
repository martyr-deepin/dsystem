#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import unittest
from subprocess import getstatusoutput as rt
from lib import utils
from lib import runner

result = True

class Vi(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.caseid = '39072'
        cls.casename = 'all-1459:文件编辑命令--验证对vi命令的支持'

    @classmethod
    def tearDownClass(cls):
        global result
        utils.commitresult(cls.caseid, result)

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
