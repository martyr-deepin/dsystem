#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import unittest
from lib import executeTestCase
from subprocess import getstatusoutput as rt
from subprocess import getoutput

casename = 'all-5415:其他命令--验证对重定向的支持'

class Command_redirect(unittest.TestCase):
    caseid = '192270'
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
        self.assertTrue(output.startswith('date: invalid date'))

    def suite():
        suite = unittest.TestSuite()
        suite.addTest(Command_redirect('testRedirect'))
        return suite

if __name__ == "__main__":
    unittest.installHandler()
    executeTestCase.runTest(Command_redirect)
