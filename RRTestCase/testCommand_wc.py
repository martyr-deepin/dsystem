#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import unittest
from lib import executeTestCase
from subprocess import getstatusoutput as rt
from subprocess import getoutput
from lib import utils
from lib import runner

casename = 'all-5390:文件/文件夹操作命令--验证对wc命令的支持'

class Command_wc(unittest.TestCase):
    caseid = '192147'
    @classmethod
    def setUpClass(cls):
        if os.path.exists('/tmp/testfile'):
            os.system('sudo rm -rf /tmp/testfile')

        os.system('touch /tmp/testfile')
        os.system('echo longest >> /tmp/testfile')
        os.system('echo short >> /tmp/testfile')
        os.system('echo one two>> /tmp/testfile')

    @classmethod
    def tearDownClass(cls):
        if os.path.exists('/tmp/testfile'):
            os.system('sudo rm -rf /tmp/testfile')

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testWcOne(self):
        (status, output) = rt('wc -c /tmp/testfile')
        self.assertTrue('22 /tmp/testfile' == output)

    def testWcTwo(self):
        (status, output) = rt('wc -l /tmp/testfile')
        self.assertTrue('3 /tmp/testfile' == output)

    def testWcThree(self):
        (status, output) = rt('wc -m /tmp/testfile')
        self.assertTrue('22 /tmp/testfile' == output)

    def testWcFour(self):
        (status, output) = rt('wc -w /tmp/testfile')
        self.assertTrue('4 /tmp/testfile' == output)

    def testWcFive(self):
        (status, output) = rt('wc -L /tmp/testfile')
        self.assertTrue('7 /tmp/testfile' == output)

    def suite():
        suite = unittest.TestSuite()
        suite.addTest(Command_wc('testWcOne'))
        suite.addTest(Command_wc('testWcTwo'))
        suite.addTest(Command_wc('testWcThree'))
        suite.addTest(Command_wc('testWcFour'))
        suite.addTest(Command_wc('testWcFive'))
        return suite

if __name__ == "__main__":
    unittest.installHandler()
    executeTestCase.runTest(Command_wc)
