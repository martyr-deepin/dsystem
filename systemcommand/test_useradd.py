#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import unittest
import time
from subprocess import getstatusoutput as rt
from lib import utils
from lib import runner

result = True
caseid = '38924'
casename = 'all-1436:用户管理命令--验证对useradd命令的支持'


class Useradd(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.startTime = time.time()
        if os.path.exists('/home/test'):
            (status, output) = rt('sudo deluser --remove-home test')

    @classmethod
    def tearDownClass(cls):
        seconds = "%.3f" % (time.time() - cls.startTime)
        minutes = utils.convertToMinutes(float(seconds))
        global result
        utils.commitresult(caseid, result, minutes)

        if os.path.exists('/home/test'):
            (status, output) = rt('sudo deluser --remove-home test')

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def addUser(self):
        self.assertFalse(os.path.exists('/home/test'))
        (status, output) = rt('sudo useradd -m test')
        self.assertTrue(0 == status)
        self.assertTrue(os.path.exists('/home/test'))

    def suite():
        suite = unittest.TestSuite()
        suite.addTest(Useradd('addUser'))
        return suite

    class MyTestResult(runner.MyTextTestResult):
        def addError(self, test, err):
            super(Useradd.MyTestResult, self).addError(test, err)
            global result
            result = result and False

        def addFailure(self, test, err):
            super(Useradd.MyTestResult, self).addError(test, err)
            global result
            result = result and False

if __name__ == "__main__":
    unittest.TextTestRunner(resultclass=Useradd.MyTestResult).run(Useradd.suite())
