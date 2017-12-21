#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

import unittest
from lib import executeTestCase
from subprocess import getstatusoutput
from lib import runner
from lib import utils

casename = 'all-5393:使用ping命令对IP地址的ping操作'

class Command_ping_ip(unittest.TestCase):
    caseid = '192164'
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
        suite.addTest(Command_ping_ip('test_ping_ip'))
        return suite

if __name__ == "__main__":
    unittest.installHandler()
    executeTestCase.runTest(Command_ping_ip)
