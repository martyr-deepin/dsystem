#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

import unittest
from lib import executeTestCase
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
        pass
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

if __name__ == "__main__":
    runTest(Ping_ip.suite())
