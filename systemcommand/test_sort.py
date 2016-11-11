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
caseid = '39010'
casename = 'all-1450:文件/文件夹操作命令--验证对sort命令的支持'

class Sort(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.startTime = time.time()
        cls.homedir = os.path.expanduser('~')

    @classmethod
    def tearDownClass(cls):
        seconds = "%.3f" % (time.time() - cls.startTime)
        minutes = utils.convertToMinutes(float(seconds))
        global result
        utils.commitresult(caseid, result, minutes)

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSortOne(self):
        output = getoutput('cat /etc/passwd | sort')

        line_list = output.split('\n')

        for i in range(len(line_list) - 1):
            if line_list[i].startswith('mail'):
                break

            self.assertTrue(line_list[i] < line_list[i+1], "%s and %s" % (line_list[i], line_list[i+1]))

    def testSortTwo(self):
        output = getoutput('cat /etc/passwd | sort -t \':\' -k 3 -n')

        line_list = output.split('\n')

        for i in range(len(line_list) - 1):
            up_num = int(line_list[i].split(':')[2])
            down_num = int(line_list[i+1].split(':')[2])
            self.assertTrue(up_num < down_num, "%s not little than  %s" % (up_num, down_num))

    def suite():
        suite = unittest.TestSuite()
        suite.addTest(Sort('testSortOne'))
        suite.addTest(Sort('testSortTwo'))
        return suite

    class MyTestResult(runner.MyTextTestResult):
        def addError(self, test, err):
            super(Sort.MyTestResult, self).addError(test, err)
            global result
            result = result and False

        def addFailure(self, test, err):
            super(Sort.MyTestResult, self).addError(test, err)
            global result
            result = result and False

if __name__ == "__main__":
    unittest.TextTestRunner(resultclass=Sort.MyTestResult).run(Sort.suite())
