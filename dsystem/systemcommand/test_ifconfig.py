#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

import unittest
from lib import executeTestCase
from subprocess import getstatusoutput
from lib import runner
from lib import utils

result = True
casename = 'all-1452:验证对ifconfig命令的支持'

class Ifconfig(unittest.TestCase):
    caseid = '39022'
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

    def test_ifconfig(self):
        (status,output) = getstatusoutput('ifconfig -a')
        self.assertEqual(0, status)

        (status,output) = getstatusoutput('ifconfig -s')
        self.assertEqual(0, status)

    def suite():
        suite = unittest.TestSuite()
        suite.addTest(Ifconfig('test_ifconfig'))
        return suite

if __name__ == "__main__":
    executeTestCase.runTest(Ifconfig)
