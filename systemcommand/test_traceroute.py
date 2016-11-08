#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

import unittest
from subprocess import getstatusoutput,check_call
from time import sleep
from lib import runner
from lib import utils

result = True
caseid = '69024'
casename = 'all-2587:使用命令traceroute网络节点间的通讯'

class Traceroute(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.startTime = time.time()
        pass

    @classmethod
    def tearDownClass(cls):
        seconds = %.3f % (time.time() - cls.startTime)
        minutes = utils.convertToMinutes(float(seconds))
        global result
        utils.commitresult(caseid, result, minutes)

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_check_traceroute(self):
        (status,output) = getstatusoutput('dpkg -l traceroute')
        self.assertEqual(0,status)
        dpkg_result = output.split('\n')
        dpkg_status = (dpkg_result[5].split(' '))[0]
        if dpkg_status != 'ii':
            return_code = check_call('sudo apt-get install inetutils-traceroute traceroute  -y',shell=True)
            self.assertEqual(0,return_code)
        else:
            pass

    def test_run_traceroute(self):
        (status,output) = getstatusoutput('traceroute www.baidu.com')
        self.assertEqual(0,status)

    def suite():
        suite = unittest.TestSuite()
        suite.addTest(Traceroute('test_check_traceroute'))
        suite.addTest(Traceroute('test_run_traceroute'))
        return suite

    class MyTestResult(runner.MyTextTestResult):
        def addError(self, test, err):
            super(Traceroute.MyTestResult, self).addError(test, err)
            global result
            result = result and False

        def addFailure(self, test, err):
            super(Traceroute.MyTestResult, self).addError(test, err)
            global result
            result = result and False

if __name__ == "__main__":
    unittest.TextTestRunner(resultclass=Traceroute.MyTestResult).run(Traceroute.suite())
