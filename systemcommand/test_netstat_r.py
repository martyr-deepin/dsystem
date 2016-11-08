#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

import unittest
from subprocess import getstatusoutput
from lib import runner
from lib import utils

result = True
caseid = '69017'
casename = 'all-2585:使用netstat命令显示网络路由信息'

class Netstat_r(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.startTime = time.time()
        pass

    @classmethod
    def tearDownClass(cls):
        seconds = %.3f % (time.time() - cls.startTime)
        minutes = utils.convertToMinutes(float(seconds))
        global result
        utils.commitresult(caseid, result, minutes)

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_netstat_r(self):
        (status,output) = getstatusoutput('netstat -r')
        self.assertEqual(0,status)
        netstat_result = output.split('\n')
        self.assertEqual('Kernel IP routing table',netstat_result[0])

    def suite():
        suite = unittest.TestSuite()
        suite.addTest(Netstat_r('test_netstat_r'))
        return suite

    class MyTestResult(runner.MyTextTestResult):
        def addError(self, test, err):
            super(Netstat_r.MyTestResult, self).addError(test, err)
            global result
            result = result and False

        def addFailure(self, test, err):
            super(Netstat_r.MyTestResult, self).addError(test, err)
            global result
            result = result and False

if __name__ == "__main__":
    unittest.TextTestRunner(resultclass=Netstat_r.MyTestResult).run(Netstat_r.suite())
