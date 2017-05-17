#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import unittest
from lib import executeTestCase
from subprocess import getstatusoutput as rt
from lib import utils
from lib import runner

casename = 'all-5376:用户管理命令--验证对userdel命令的支持'

class Command_userdel(unittest.TestCase):
    caseid = '192064'
    @classmethod
    def setUpClass(cls):
        if os.path.exists('/home/test'):
            (status, output) = rt('sudo deluser --remove-home test')

    @classmethod
    def tearDownClass(cls):
        if os.path.exists('/home/test'):
            (status, output) = rt('sudo deluser --remove-home test')

        if os.path.exists('/home/test/'):
            os.system('sudo rm -rf /home/test')

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def addUser(self):
        self.assertFalse(os.path.exists('/home/test'))
        (status, output) = rt('sudo useradd -m test')
        self.assertTrue(0 == status)
        self.assertTrue(os.path.exists('/home/test'))

    def delUser(self):
        (status, output) = rt('sudo userdel test')
        self.assertTrue(0 == status)
        self.assertTrue(os.path.exists('/home/test'))

    def suite():
        suite = unittest.TestSuite()
        suite.addTest(Command_userdel('addUser'))
        suite.addTest(Command_userdel('delUser'))
        return suite

if __name__ == "__main__":
    unittest.installHandler()
    executeTestCase.runTest(Command_userdel)
