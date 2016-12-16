#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

import unittest
from lib import executeTestCase
from subprocess import getstatusoutput
from lib import runner
from lib import utils

result = True
casename = 'all-2583:使用ping命令对本机地址的ping操作'

class Ping_local_ip(unittest.TestCase):
    caseid = '69011'
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

if __name__ == "__main__":
    executeTestCase.runTest(Ping_local_ip)
