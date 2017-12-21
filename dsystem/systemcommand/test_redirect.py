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
casename = 'all-1469:其他命令--验证对重定向的支持'

class Redirect(unittest.TestCase):
    caseid = '39116'
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

    def testRedirect(self):
        (status, output) = rt('echo bbbb > /tmp/testfile')
        (status, output) = rt('more /tmp/testfile')
        self.assertTrue(0 == status)
        self.assertTrue('bbbb' == output)

        (status, output) = rt('echo aaaa >> /tmp/testfile')
        (status, output) = rt('more /tmp/testfile')
        self.assertTrue(0 == status)
        self.assertTrue('bbbb\naaaa' == output)

        (status, output) = rt('date -s aa > /tmp/testfile 2>&1')
        (status, output) = rt('cat /tmp/testfile')
        self.assertTrue(0 == status)
        self.assertTrue('date: 无效的日期"aa"' == output)

    def suite():
        suite = unittest.TestSuite()
        suite.addTest(Redirect('testRedirect'))
        return suite

if __name__ == "__main__":
    executeTestCase.runTest(Redirect)
