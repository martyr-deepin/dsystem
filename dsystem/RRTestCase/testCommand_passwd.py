#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import unittest
from lib import executeTestCase
from subprocess import getstatusoutput as rt
from subprocess import getoutput
from lib import utils
from lib import runner
import pexpect

casename = 'all-5377:用户管理命令--验证对passwd命令的支持'

class Command_passwd(unittest.TestCase):
    caseid = '192068'
    @classmethod
    def setUpClass(cls):
        if os.path.exists('/home/test'):
            (status, output) = rt('sudo deluser --remove-home test')

        if os.getenv("LANG") == "en_US.UTF-8":
            cls.passwd_one = "UNIX password:"
            cls.passwd_two = "UNIX password:"
            cls.su_passwd = "Password:"
        elif os.getenv("LANG") == "zh_CN.UTF-8":
            cls.passwd_one = "UNIX 密码："
            cls.passwd_two = "UNIX 密码："
            cls.su_passwd = "密码："

    @classmethod
    def tearDownClass(cls):
        if os.path.exists('/home/test'):
            (status, output) = rt('sudo deluser --remove-home test')

        if os.path.exists('/home/test'):
            os.system('sudo rm -rf /home/test')

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def addUser(self):
        self.assertFalse(os.path.exists('/home/test'))
        (status, output) = rt('sudo useradd -m test')
        self.assertTrue(0 == status)
        self.assertTrue(os.path.exists('/home/test'))

    def passwd(self):
        childerr = pexpect.spawn('su - test')
        childerr.expect(self.su_passwd)
        childerr.sendline("deepin")
        outputerr = getoutput('echo $?')
        self.assertFalse(int(outputerr) == 1)

        child = pexpect.spawn('sudo passwd test')
        child.expect(self.passwd_one)
        child.sendline("deepin")
        child.expect(self.passwd_two)
        child.sendline("deepin")

        childok = pexpect.spawn('su - test')
        childok.expect(self.su_passwd)
        childok.sendline("deepin")
        outputok = getoutput('echo $?')
        self.assertTrue(int(outputok) == 0)

    def delUser(self):
        (status, output) = rt('sudo userdel test')
        self.assertTrue(0 == status)
        self.assertTrue(os.path.exists('/home/test'))

    def suite():
        suite = unittest.TestSuite()
        suite.addTest(Command_passwd('addUser'))
        suite.addTest(Command_passwd('passwd'))
        suite.addTest(Command_passwd('delUser'))
        return suite

if __name__ == "__main__":
    unittest.installHandler()
    executeTestCase.runTest(Command_passwd)
