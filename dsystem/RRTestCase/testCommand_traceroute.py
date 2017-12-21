#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

import unittest
from lib import executeTestCase
from subprocess import getstatusoutput,check_call
from time import sleep
from lib import runner
from lib import utils

casename = 'all-5398:使用命令traceroute网络节点间的通讯'

class Command_traceroute(unittest.TestCase):
    caseid = '192180'
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

    def test_check_traceroute(self):
        return_code = check_call('sudo apt-get install inetutils-traceroute traceroute  -y',shell=True)
        self.assertEqual(0,return_code)
        (status,output) = getstatusoutput('dpkg -l traceroute')
        self.assertEqual(0,status)
        dpkg_result = output.split('\n')
        dpkg_package = dpkg_result[5].split(' ')
        self.assertTrue('ii' == dpkg_package[0], '%s' % dpkg_package)
        self.assertTrue('traceroute' == dpkg_package[2], '%s' % dpkg_package)

    def test_run_traceroute(self):
        (status,output) = getstatusoutput('traceroute www.deepin.org')
        self.assertEqual(0,status)

    def suite():
        suite = unittest.TestSuite()
        suite.addTest(Command_traceroute('test_check_traceroute'))
        suite.addTest(Command_traceroute('test_run_traceroute'))
        return suite

if __name__ == "__main__":
    unittest.installHandler()
    executeTestCase.runTest(Command_traceroute)
