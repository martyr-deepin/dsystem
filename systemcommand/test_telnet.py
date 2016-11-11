#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

import unittest
import time
from subprocess import getstatusoutput,check_call
from time import sleep
from lib import runner
from lib import utils

result = True
caseid = '69020'
casename = 'all-2586:使用telnet命令连接到远程主机'

class Telnet(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.startTime = time.time()
        pass

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

    def test_check_telnet(self):
        (status,output) = getstatusoutput('dpkg -l telnet')
        self.assertEqual(0,status)
        dpkg_result = output.split('\n')
        dpkg_status = (dpkg_result[5].split(' '))[0]
        if dpkg_status == 'un':
            return_code = check_call('sudo apt-get install telnet -y',shell=True)
            self.assertEqual(0,return_code)
        else:
            pass

    def test_run_telnet(self):
        (status,output) = getstatusoutput('telnet')
        self.assertEqual(127,status)

    def suite():
        suite = unittest.TestSuite()
        suite.addTest(Telnet('test_check_telnet'))
        suite.addTest(Telnet('test_run_telnet'))
        return suite

    class MyTestResult(runner.MyTextTestResult):
        def addError(self, test, err):
            super(Telnet.MyTestResult, self).addError(test, err)
            global result
            result = result and False

        def addFailure(self, test, err):
            super(Telnet.MyTestResult, self).addError(test, err)
            global result
            result = result and False

if __name__ == "__main__":
    unittest.TextTestRunner(resultclass=Telnet.MyTestResult).run(Telnet.suite())
