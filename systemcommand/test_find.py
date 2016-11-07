#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import unittest
from subprocess import getstatusoutput as rt
from subprocess import getoutput
from lib import utils
from lib import runner

result = True
caseid = '38983'
casename = 'all-1447:文件/文件夹操作命令--验证对find命令的支持'

class Find(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        global result
        utils.commitresult(caseid, result)

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testFindCommand(self):
        (status, output) = rt('find /bin -name \"[a-b]*\"')

        for line in output.split('\n'):
            linelist = line.split('/')
            if 2 == len(linelist):
                self.assertTrue(linelist[1].startswith(('a', 'b')))

    def suite():
        suite = unittest.TestSuite()
        suite.addTest(Find('testFindCommand'))
        return suite

    class MyTestResult(runner.MyTextTestResult):
        def addError(self, test, err):
            super(Find.MyTestResult, self).addError(test, err)
            global result
            result = result and False

        def addFailure(self, test, err):
            super(Find.MyTestResult, self).addError(test, err)
            global result
            result = result and False

if __name__ == "__main__":
    unittest.TextTestRunner(resultclass=Find.MyTestResult).run(Find.suite())
