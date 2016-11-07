#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

import unittest
from subprocess import getstatusoutput
from lib import runner
from lib import utils

result = True
caseid = '69008'
casename = 'all-2582:使用ping命令对IP地址的ping操作'

class Ping_ip(unittest.TestCase):
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

    def test_ping_ip(self):
        count = 3
        ip_address = '10.0.0.1'
        (status,output) = getstatusoutput('ping -c %d %s' % (count, ip_address))
        self.assertEqual(0,status)
        ping_result = output.split('\n')
        for i in range(1,len(ping_result)-4):
            self.assertIn('icmp_seq=%d' % i,ping_result[i])

    def suite():
        suite = unittest.TestSuite()
        suite.addTest(Ping_ip('test_ping_ip'))
        return suite

    class MyTestResult(runner.MyTextTestResult):
        def addError(self, test, err):
            super(Ping_ip.MyTestResult, self).addError(test, err)
            global result
            result = result and False

        def addFailure(self, test, err):
            super(Ping_ip.MyTestResult, self).addError(test, err)
            global result
            result = result and False

if __name__ == "__main__":
    unittest.TextTestRunner(resultclass=Ping_ip.MyTestResult).run(Ping_ip.suite())
