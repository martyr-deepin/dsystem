#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

import unittest
from lib import executeTestCase
from subprocess import getstatusoutput,check_call
from time import sleep
from lib import runner
from lib import utils

result = True
casename = 'all-2586:使用telnet命令连接到远程主机'

class Telnet(unittest.TestCase):
    caseid = '69020'
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
        (status,output) = getstatusoutput('dpkg -l telnet')
        self.assertEqual(0,status)
        dpkg_result = output.split('\n')
        dpkg_status = (dpkg_result[5].split(' '))[0]
        if dpkg_status == 'un':
            return_code = check_call('sudo apt-get install telnet -y',shell=True)
            self.assertEqual(0,return_code)
        else:
            pass

    def test_run_telnet(self):
        (status,output) = getstatusoutput('which telnet')
        self.assertEqual(0, status)
        (status,output) = getstatusoutput('telnet error')
        self.assertNotEqual(0, status)

    def suite():
        suite = unittest.TestSuite()
        suite.addTest(Telnet('test_check_telnet'))
        suite.addTest(Telnet('test_run_telnet'))
        return suite

if __name__ == "__main__":
    executeTestCase.runTest(Telnet)
