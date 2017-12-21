#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import unittest
from lib import executeTestCase
from subprocess import getstatusoutput as rt
from subprocess import getoutput
from lib import runner
from lib import utils

result = True
casename = 'all-1468:其他命令--验证对more命令的支持'

class More(unittest.TestCase):
    caseid = '39112'
    @classmethod
    def setUpClass(cls):
        os.system('touch /tmp/testfile')

    @classmethod
    def tearDownClass(cls):
        os.system('rm /tmp/testfile')

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testMore(self):
        (status, output) = rt('more /tmp/testfile')
        self.assertTrue(0 == status)
        self.assertTrue('' == output)

        (status, output) = rt('echo aaaa > /tmp/testfile')
        (status, output) = rt('more /tmp/testfile')
        self.assertTrue(0 == status)
        self.assertTrue('aaaa' == output)

        (status, output) = rt('echo bbbb > /tmp/testfile')
        (status, output) = rt('more /tmp/testfile')
        self.assertTrue(0 == status)
        self.assertTrue('bbbb' == output)

        (status, output) = rt('echo aaaa >> /tmp/testfile')
        (status, output) = rt('more /tmp/testfile')
        self.assertTrue(0 == status)
        self.assertTrue('bbbb\naaaa' == output)

    def suite():
        suite = unittest.TestSuite()
        suite.addTest(More('testMore'))
        return suite

if __name__ == "__main__":
    executeTestCase.runTest(More)
