#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import getpass
import unittest
from subprocess import getstatusoutput as rt
from subprocess import getoutput
from lib import utils
from lib import runner

result = True

class Whoami(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.caseid = '39099'
        cls.casename = 'all-1465:其他命令--验证对whoami命令的支持'
        cls.loginuser = getpass.getuser()

    @classmethod
    def tearDownClass(cls):
        global result
        utils.commitresult(cls.caseid, result)

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testWhoami(self):
        (status, output) = rt('whoami')
        self.assertTrue(0 == status)
        self.assertTrue(output == self.loginuser)

    def suite():
        suite = unittest.TestSuite()
        suite.addTest(Whoami('testWhoami'))
        return suite

    class MyTestResult(runner.MyTextTestResult):
        def addError(self, test, err):
            super(Whoami.MyTestResult, self).addError(test, err)
            global result
            result = result and False

        def addFailure(self, test, err):
            super(Whoami.MyTestResult, self).addError(test, err)
            global result
            result = result and False

if __name__ == "__main__":
    unittest.TextTestRunner(resultclass=Whoami.MyTestResult).run(Whoami.suite())
