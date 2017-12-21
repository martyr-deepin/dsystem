#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import unittest
from lib import executeTestCase
from subprocess import getstatusoutput as rt
from subprocess import getoutput

casename = 'all-5406:其他命令-验证对man命令的支持'

class Command_man(unittest.TestCase):
    caseid = '192233'
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

    def testManOne(self):
        (status, output) = rt('man ls')
        self.assertTrue(0 == status)

        for line in output.split('\n'):
            linelist = line.split()
            self.assertTrue(linelist[0].startswith('LS('), "linelist[0]: %s" % linelist[0])
            break

    def testManTwo(self):
        (status, output) = rt('man ssh_config')
        self.assertTrue(0 == status)

        for line in output.split('\n'):
            linelist = line.split()
            self.assertTrue(linelist[0].startswith('SSH_CONFIG('), "linelist[0]: %s" % linelist[0])
            break

    def testManThree(self):
        (status, output) = rt('whereis apt-get')
        self.assertTrue(0 == status)

        linelist = output.split()
        self.assertTrue('apt-get:' == linelist[0])
        self.assertTrue('/usr/bin/apt-get' == linelist[1])
        self.assertTrue('' != linelist[2] and None != linelist[2])

    def testManFour(self):
        (status, output) = rt('man apt-get')
        self.assertTrue(0 == status)

        for line in output.split('\n'):
            linelist = line.split()
            self.assertTrue(linelist[0].startswith('APT-GET('), "linelist[0]: %s" % linelist[0])
            break

    def suite():
        suite = unittest.TestSuite()
        suite.addTest(Command_man('testManOne'))
        suite.addTest(Command_man('testManTwo'))
        suite.addTest(Command_man('testManThree'))
        suite.addTest(Command_man('testManFour'))
        return suite

if __name__ == "__main__":
    unittest.installHandler()
    executeTestCase.runTest(Command_man)
