#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

import unittest
from lib import executeTestCase
from subprocess import getstatusoutput
from lib import runner
from lib import utils

result = True
caseid = '39029'
casename = 'all-1453:使用ping命令对域名的ping操作'

class Ping(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass
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

if __name__ == "__main__":
    runTest(Ping.suite())
