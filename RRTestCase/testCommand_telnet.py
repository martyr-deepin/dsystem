#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

import unittest
from lib import executeTestCase
from subprocess import getstatusoutput,check_call
from time import sleep
from lib import runner
from lib import utils

casename = 'all-5397:使用telnet命令连接到远程主机'

class Command_telnet(unittest.TestCase):
    caseid = '192176'
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

    def test_check_telnet(self):
        return_code = check_call('sudo apt-get install telnet -y',shell=True)
        self.assertEqual(0,return_code)
        (status,output) = getstatusoutput('dpkg -l telnet')
        self.assertEqual(0,status)
        dpkg_result = output.split('\n')
        dpkg_package = dpkg_result[5].split(' ')
        self.assertTrue('ii' == dpkg_package[0], '%s' % dpkg_package)
        self.assertTrue('telnet' == dpkg_package[2], '%s' % dpkg_package)

    def test_run_telnet(self):
        (status,output) = getstatusoutput('which telnet')
        self.assertEqual(0, status)
        (status,output) = getstatusoutput('telnet error')
        self.assertNotEqual(0, status)

    def suite():
        suite = unittest.TestSuite()
        suite.addTest(Command_telnet('test_check_telnet'))
        suite.addTest(Command_telnet('test_run_telnet'))
        return suite

if __name__ == "__main__":
    unittest.installHandler()
    executeTestCase.runTest(Command_telnet)
