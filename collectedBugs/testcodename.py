#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from lib import runner,utils
from subprocess import getoutput
from lib.filesystemutils import getDevInfo
import platform

result = True
caseid = '80301'
casename = "all-3149:codename测试"

class CodeName(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.startTime = time.time()
        cls.codename = getDevInfo('codename','code')
        cls.lsbcode = 'DISTRIB_CODENAME=' + cls.codename
        cls.lsb = "cat /etc/lsb-release |grep DISTRIB_CODENAME"
        cls.csvInfo = "cat /usr/share/distro-info/deepin.csv |awk 'END{print $1}'"


    @classmethod
    def tearDownClass(cls):
        seconds = %.3f % (time.time() - cls.startTime)
        minutes = utils.convertToMinutes(float(seconds))
        global result
        utils.commitresult(caseid, result, minutes)


    def testlsb(self):
        lsb = getoutput(self.lsb)
        self.assertEqual(lsb, self.lsbcode)
    def testcsv(self):
        csvInfo = getoutput(self.csvInfo)
        _, csv, *_ = csvInfo.split(',')
        self.assertEqual(csv.lower(), self.codename)
    def testdist(self):
        dist = platform.dist()
        self.assertEqual(dist[2], self.codename)


    def suite():
        suite = unittest.TestSuite()
        suite.addTest(CodeName('testlsb'))
        suite.addTest(CodeName('testcsv'))
        suite.addTest(CodeName('testdist'))
        return suite

    class MyTestResult(runner.MyTextTestResult):
        def addError(self, test, err):
            super(CodeName.MyTestResult, self).addError(test, err)
            global result
            result = result and False

        def addFailure(self, test, err):
            super(CodeName.MyTestResult, self).addFailure(test, err)
            global result
            result = result and False

if __name__ == "__main__":
    unittest.TextTestRunner(resultclass=CodeName.MyTestResult).run(CodeName.suite())
