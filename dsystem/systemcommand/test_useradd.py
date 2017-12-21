#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import unittest
from lib import executeTestCase
from subprocess import getstatusoutput as rt
from lib import utils
from lib import runner

result = True
casename = 'all-1436:用户管理命令--验证对useradd命令的支持'


class Useradd(unittest.TestCase):
    caseid = '38924'
    @classmethod
    def setUpClass(cls):
        if os.path.exists('/home/test'):
            (status, output) = rt('sudo deluser --remove-home test')

    @classmethod
    def tearDownClass(cls):
        if os.path.exists('/home/test'):
            (status, output) = rt('sudo deluser --remove-home test')

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def addUser(self):
        self.assertFalse(os.path.exists('/home/test'))
        (status, output) = rt('sudo useradd -m test')
        self.assertTrue(0 == status)
        self.assertTrue(os.path.exists('/home/test'))

    def suite():
        suite = unittest.TestSuite()
        suite.addTest(Useradd('addUser'))
        return suite

if __name__ == "__main__":
    executeTestCase.runTest(Useradd)
