#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

import unittest
from subprocess import getstatusoutput
from lib import runner
from lib import utils

result = True

class Ping(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.caseid = '39029'
        cls.casename = 'all-1453:使用ping命令对域名的ping操作'

    @classmethod
    def tearDownClass(cls):
        global result
        utils.commitresult(cls.caseid,result)

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_ping(self):
        count = 3
        domain_name = 'www.baidu.com'
        (status,output) = getstatusoutput('ping -c %d %s' % (count,domain_name))
        self.assertEqual(0,status)
        ping_result = output.split('\n')
        for i in range(1,len(ping_result)-4):
            self.assertIn('icmp_seq=%d' % i,ping_result[i])

    def suite():
        suite = unittest.TestSuite()
        suite.addTest(Ping('test_ping'))
        return suite

    class MyTestResult(runner.MyTextTestResult):
        def addError(self, test, err):
            super(Ping.MyTestResult, self).addError(test, err)
            global result
            result = result and False

        def addFailure(self, test, err):
            super(Ping.MyTestResult, self).addError(test, err)
            global result
            result = result and False

if __name__ == "__main__":
    unittest.TextTestRunner(resultclass=Ping.MyTestResult).run(Ping.suite())
