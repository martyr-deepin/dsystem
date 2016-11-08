#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

import unittest
from subprocess import getstatusoutput
from lib import runner
from lib import utils

result = True
caseid = '69011'
casename = 'all-2583:使用ping命令对本机地址的ping操作'

class Ping_local_ip(unittest.TestCase):
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

    def test_ping_local_ip(self):
        count = 4
        local_ip_address = '127.0.0.1'
        (status,output) = getstatusoutput('ping -c %d %s' % (count, local_ip_address))
        self.assertEqual(0,status)
        ping_result = output.split('\n')
        for i in range(1,len(ping_result)-4):
            self.assertIn('icmp_seq=%d' % i,ping_result[i])

    def suite():
        suite = unittest.TestSuite()
        suite.addTest(Ping_local_ip('test_ping_local_ip'))
        return suite

    class MyTestResult(runner.MyTextTestResult):
        def addError(self, test, err):
            super(Ping_local_ip.MyTestResult, self).addError(test, err)
            global result
            result = result and False

        def addFailure(self, test, err):
            super(Ping_local_ip.MyTestResult, self).addError(test, err)
            global result
            result = result and False

if __name__ == "__main__":
    unittest.TextTestRunner(resultclass=Ping_local_ip.MyTestResult).run(Ping_local_ip.suite())
