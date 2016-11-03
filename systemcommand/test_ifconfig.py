#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

import unittest
from subprocess import getstatusoutput
from lib import runner
from lib import utils

result = True
caseid = '39022'
casename = 'all-1452:验证对ifconfig命令的支持'

class Ifconfig(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        global result
        utils.commitresult(caseid,result)

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_ifconfig(self):
        (status,output) = getstatusoutput('ifconfig -a')
        self.assertEqual(0, status)

        (status,output) = getstatusoutput('ifconfig -s')
        self.assertEqual(0, status)

    def suite():
        suite = unittest.TestSuite()
        suite.addTest(Ifconfig('test_ifconfig'))
        return suite

    class MyTestResult(runner.MyTextTestResult):
        def addError(self, test, err):
            super(Ifconfig.MyTestResult, self).addError(test, err)
            global result
            result = result and False

        def addFailure(self, test, err):
            super(Ifconfig.MyTestResult, self).addError(test, err)
            global result
            result = result and False

if __name__ == "__main__":
    unittest.TextTestRunner(resultclass=Ifconfig.MyTestResult).run(Ifconfig.suite())
