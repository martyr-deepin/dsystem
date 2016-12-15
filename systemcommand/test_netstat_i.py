#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

import unittest
from lib import executeTestCase
from subprocess import getstatusoutput
from lib import runner
from lib import utils

result = True
caseid = '69014'
casename = 'all-2584:使用netstat命令显示网络分组传送信息'

class Netstat_i(unittest.TestCase):
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

    def test_netstat_i(self):
        (status,output) = getstatusoutput('netstat -i')
        self.assertEqual(0,status)
        netstat_result = output.split('\n')
        self.assertEqual('Kernel Interface table',netstat_result[0])

    def suite():
        suite = unittest.TestSuite()
        suite.addTest(Netstat_i('test_netstat_i'))
        return suite

if __name__ == "__main__":
    runTest(Netstat_i.suite())
