#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import unittest
from subprocess import getstatusoutput as rt
from subprocess import getoutput
from lib import utils
from lib import runner

result = True

class Cd(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.caseid = '38944'
        cls.casename = 'all-1440:文件/文件夹操作命令--验证对cd命令的支持'

    @classmethod
    def tearDownClass(cls):
        global result
        utils.commitresult(cls.caseid, result)

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

    class MyTestResult(runner.MyTextTestResult):
        def addError(self, test, err):
            super(Cd.MyTestResult, self).addError(test, err)
            global result
            result = result and False

        def addFailure(self, test, err):
            super(Cd.MyTestResult, self).addError(test, err)
            global result
            result = result and False

if __name__ == "__main__":
    unittest.TextTestRunner(resultclass=Cd.MyTestResult).run(Cd.suite())