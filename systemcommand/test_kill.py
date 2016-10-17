#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from subprocess import getstatusoutput
from lib import runner
from lib import utils
from time import sleep

result = True
listlastssh = ''

class  Kill(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.caseid = '39066'
        cls.casename = 'all-1458:进程管理工具--验证对kill命令的支持'

    @classmethod
    def tearDownClass(cls):
        global result
        utils.commitresult(cls.caseid, result)

    def setUp(self):
    	pass

    def tearDown(self):
    	pass

    def testCheckSshd(self):
        (status,output) = getstatusoutput(r'ps -ef|grep sshd|grep -v grep')
        self.assertTrue(0 == status)
        global listlastssh
        listlastssh = output.split()
 
    def testKillPid(self):
        global listlastssh
        # self.testCheckSshd()
        (status,output) = getstatusoutput("sudo kill -9 %s" % listlastssh[1])
        self.assertTrue(0 == status)
        self.assertTrue(output == '')

    def testCheckSshdAgain(self):
        sleep(1)
        global listlastssh
        (status,output) = getstatusoutput(r'ps -ef|grep sshd|grep -v grep')
        self.assertTrue(0 ==  status)
        listnewssh = output.split()
        self.assertTrue(listnewssh[1] != listlastssh[1])

    def suite():
        suite = unittest.TestSuite()
        suite.addTest(Kill('testCheckSshd'))
        suite.addTest(Kill('testKillPid'))
        suite.addTest(Kill('testCheckSshdAgain'))
        return suite

    class MyTestResult(runner.MyTextTestResult):
        def addError(self, test, err):
            super(Kill.MyTestResult, self).addError(test, err)
            global result
            result = result and False

        def addFailure(self, test, err):
            super(Kill.MyTestResult, self).addError(test, err)
            global result
            result = result and False

if __name__ == "__main__":
    unittest.TextTestRunner(resultclass=Kill.MyTestResult).run(Kill.suite())
