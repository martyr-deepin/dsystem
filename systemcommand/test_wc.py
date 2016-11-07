#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import unittest
from subprocess import getstatusoutput as rt
from subprocess import getoutput
from lib import utils
from lib import runner

result = True
caseid = '39014'
casename = 'all-1451:文件/文件夹操作命令--验证对wc命令的支持'

class Wc(unittest.TestCase):
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
        global result
        utils.commitresult(caseid, result)

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
        suite.addTest(Wc('testWcOne'))
        suite.addTest(Wc('testWcTwo'))
        suite.addTest(Wc('testWcThree'))
        suite.addTest(Wc('testWcFour'))
        suite.addTest(Wc('testWcFive'))
        return suite

    class MyTestResult(runner.MyTextTestResult):
        def addError(self, test, err):
            super(Wc.MyTestResult, self).addError(test, err)
            global result
            result = result and False

        def addFailure(self, test, err):
            super(Wc.MyTestResult, self).addError(test, err)
            global result
            result = result and False

if __name__ == "__main__":
    unittest.TextTestRunner(resultclass=Wc.MyTestResult).run(Wc.suite())
