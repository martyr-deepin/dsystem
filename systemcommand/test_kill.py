#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from lib import executeTestCase
from subprocess import getstatusoutput
from lib import runner
from lib import utils
from time import sleep

result = True
casename = 'all-1458:进程管理工具--验证对kill命令的支持'
listlastssh = ''

class  Kill(unittest.TestCase):
    caseid = '39066'
    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass
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

if __name__ == "__main__":
    executeTestCase.runTest(Kill)
