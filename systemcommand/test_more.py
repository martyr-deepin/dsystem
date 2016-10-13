#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import unittest
from subprocess import getstatusoutput as rt
from subprocess import getoutput
from lib import runner
from lib import utils

result = True

class More(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.caseid = '39112'
        cls.casename = 'all-1468:其他命令--验证对more命令的支持'

        os.system('touch /tmp/testfile')

    @classmethod
    def tearDownClass(cls):
        global result
        utils.commitresult(cls.caseid, result)

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

    class MyTestResult(runner.MyTextTestResult):
        def addError(self, test, err):
            super(More.MyTestResult, self).addError(test, err)
            global result
            result = result and False

        def addFailure(self, test, err):
            super(More.MyTestResult, self).addError(test, err)
            global result
            result = result and False

if __name__ == "__main__":
    unittest.TextTestRunner(resultclass=More.MyTestResult).run(More.suite())
