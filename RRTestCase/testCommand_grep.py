#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import unittest
from lib import executeTestCase
from subprocess import getstatusoutput as rt
from subprocess import getoutput
from lib import utils
from lib import runner

casename = 'all-5287:文件/文件夹操作命令--验证对grep命令的支持'

class Command_grep(unittest.TestCase):
    caseid = '192120'
    @classmethod
    def setUpClass(cls):
        cls.homedir = os.path.expanduser('~')

    @classmethod
    def tearDownClass(cls):
        pass
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test1GrepCommand(self):
        (status, output) = rt('ls -l %s | grep ^d' % self.homedir)

        for line in output.split('\n'):
            linelist = line.split()
            self.assertTrue(linelist[0].startswith('drwx'))

    def test2GrepCommand(self):
        (status, output) = rt('grep PATH /etc/profile')

        for line in output.split('\n'):
            self.assertIn('PATH', line)

    def test3GrepCommand(self):
        (status, output) = rt('grep PATH /etc/profile | wc -l')

        self.assertEquals(int(output), 3)

    def test4GrepCommand(self):
        (status, output) = rt('grep -n PATH /etc/profile')

        for line in output.split('\n'):
            linelist = line.split(':')
            self.assertLess(int(linelist[0]), 10000)

    def test5GrepCommand(self):
        (status, output) = rt('grep -i path /etc/profile')

        for line in output.split('\n'):
            self.assertIn('PATH', line)

    def test6GrepCommand(self):
        (status, output) = rt('grep -v PATH /etc/profile')

        for line in output.split('\n'):
            self.assertNotIn('PATH', line)

    def suite():
        suite = unittest.TestSuite()
        suite.addTest(Command_grep('test1GrepCommand'))
        suite.addTest(Command_grep('test2GrepCommand'))
        suite.addTest(Command_grep('test3GrepCommand'))
        suite.addTest(Command_grep('test4GrepCommand'))
        suite.addTest(Command_grep('test5GrepCommand'))
        suite.addTest(Command_grep('test6GrepCommand'))
        return suite

if __name__ == "__main__":
    unittest.installHandler()
    executeTestCase.runTest(Command_grep)
