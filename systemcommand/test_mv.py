#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import unittest
import time
from subprocess import getstatusoutput as rt
from subprocess import getoutput
from lib import utils
from lib import runner

result = True
caseid = '38967'
casename = 'all-1444:文件/文件夹操作命令--验证对mv命令的支持'

class Mv(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.startTime = time.time()
        cls.loginuser = getoutput("whoami")

    @classmethod
    def tearDownClass(cls):
        seconds = "%.3f" % (time.time() - cls.startTime)
        minutes = utils.convertToMinutes(float(seconds))
        global result
        utils.commitresult(caseid, result, minutes)

        if os.path.exists('/tmp/test'):
            os.system('rm /tmp/test')

        if os.path.exists('/tmp/test1'):
            os.system('rm /tmp/test1')

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test1CreateFile(self):
        self.assertFalse(os.path.exists('/tmp/test'))
        os.system("echo test >> /tmp/test")
        self.assertTrue(os.path.exists('/tmp/test'))
        self.assertTrue(os.path.isfile('/tmp/test'))

    def test2MvFile(self):
        (status, output) = rt("mv /tmp/test /tmp/test1")
        self.assertTrue(0 == status)
        self.assertFalse(os.path.exists('/tmp/test'))
        self.assertTrue(os.path.exists('/tmp/test1'))

    def suite():
        suite = unittest.TestSuite()
        suite.addTest(Mv('test1CreateFile'))
        suite.addTest(Mv('test2MvFile'))
        return suite

    class MyTestResult(runner.MyTextTestResult):
        def addError(self, test, err):
            super(Mv.MyTestResult, self).addError(test, err)
            global result
            result = result and False

        def addFailure(self, test, err):
            super(Mv.MyTestResult, self).addError(test, err)
            global result
            result = result and False

if __name__ == "__main__":
    unittest.TextTestRunner(resultclass=Mv.MyTestResult).run(Mv.suite())
