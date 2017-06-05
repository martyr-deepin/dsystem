#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import unittest
from lib import executeTestCase
from subprocess import getstatusoutput as rt
from subprocess import getoutput
from lib import utils
from lib import runner

casename = 'all-5386:文件/文件夹操作命令--验证对find命令的支持'

class Command_find(unittest.TestCase):
    caseid = '192116'
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

    def testFindCommand(self):
        (status, output) = rt('find /bin -name \"[a-b]*\"')

        for line in output.split('\n'):
            linelist = line.split('/')
            if 2 == len(linelist):
                self.assertTrue(linelist[1].startswith(('a', 'b')))

    def suite():
        suite = unittest.TestSuite()
        suite.addTest(Command_find('testFindCommand'))
        return suite

if __name__ == "__main__":
    unittest.installHandler()
    executeTestCase.runTest(Command_find)
