#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

import unittest
from lib import executeTestCase
from subprocess import getstatusoutput
from lib import runner
from lib import utils

result = True
caseid = '69017'
casename = 'all-2585:使用netstat命令显示网络路由信息'

class Netstat_r(unittest.TestCase):
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

    def test_netstat_r(self):
        (status,output) = getstatusoutput('netstat -r')
        self.assertEqual(0,status)
        netstat_result = output.split('\n')
        self.assertEqual('Kernel IP routing table',netstat_result[0])

    def suite():
        suite = unittest.TestSuite()
        suite.addTest(Netstat_r('test_netstat_r'))
        return suite

if __name__ == "__main__":
    runTest(Netstat_r.suite())
