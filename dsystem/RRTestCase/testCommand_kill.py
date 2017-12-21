#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from lib import executeTestCase
from subprocess import getstatusoutput
from time import sleep

casename = 'all-5403:进程管理工具--验证对kill命令的支持'
listddedock = ''

class  Command_kill(unittest.TestCase):
    caseid = '192212'
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

    def testCheckDdeDock(self):
        (status,output) = getstatusoutput(r'ps -ef|grep dde-dock|grep -v grep')
        self.assertTrue(0 == status)
        global listddedock
        listddedock = output.split()

    def testKillPid(self):
        global listddedock
        # self.testCheckSshd()
        (status,output) = getstatusoutput("sudo kill -9 %s" % listddedock[1])
        self.assertTrue(0 == status)
        self.assertTrue(output == '')

    def testCheckDdeDockAgain(self):
        sleep(1)
        (status,output) = getstatusoutput(r'ps -ef|grep dde-dock|grep -v grep')
        self.assertTrue(0 != status)
        sleep(14)
        global listddedock
        (status,output) = getstatusoutput(r'ps -ef|grep dde-dock|grep -v grep')
        self.assertTrue(0 ==  status)
        listnewddedock = output.split()
        self.assertTrue(listnewddedock[1] != listddedock[1])

    def suite():
        suite = unittest.TestSuite()
        suite.addTest(Command_kill('testCheckDdeDock'))
        suite.addTest(Command_kill('testKillPid'))
        suite.addTest(Command_kill('testCheckDdeDockAgain'))
        return suite

if __name__ == "__main__":
    unittest.installHandler()
    executeTestCase.runTest(Command_kill)
