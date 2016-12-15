#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import unittest
from lib import executeTestCase
from subprocess import getstatusoutput as rt
from subprocess import getoutput
from lib import utils
from lib import runner

result = True
caseid = '38944'
casename = 'all-1440:文件/文件夹操作命令--验证对cd命令的支持'

class Cd(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass
    def setUp(self):
        self.loginuser = getoutput("whoami")

    def tearDown(self):
        pass

    def testPath(self):
        (status, output) = rt("cd /tmp && pwd")
        self.assertTrue(0 == status)
        self.assertEqual(output, '/tmp')

    def testDoubleDot(self):
        (status, output) = rt("cd /tmp && cd .. && pwd")
        self.assertTrue(0 == status)
        self.assertEqual(output, '/')

    def testShortLine(self):
        (status, output) = rt("cd /tmp && cd .. && cd -")
        self.assertTrue(0 == status)
        self.assertEqual(output, '/tmp')

    def testTilde(self):
        (status, output) = rt("cd /tmp && cd .. && cd ~ && pwd")
        self.assertTrue(0 == status)
        self.assertEqual(output, '/home/%s' % self.loginuser)

    def testNothing(self):
        (status, output) = rt("cd /tmp && cd .. && cd && pwd")
        self.assertTrue(0 == status)
        self.assertEqual(output, '/home/%s' % self.loginuser)

    def suite():
        suite = unittest.TestSuite()
        suite.addTest(Cd('testPath'))
        suite.addTest(Cd('testDoubleDot'))
        suite.addTest(Cd('testDoubleDot'))
        suite.addTest(Cd('testTilde'))
        suite.addTest(Cd('testNothing'))
        return suite

if __name__ == "__main__":
    runTest(Cd.suite())
