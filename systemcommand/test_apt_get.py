#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import unittest
from lib import executeTestCase
from subprocess import getstatusoutput as rt
from subprocess import getoutput
from lib import utils
from lib import runner

result = True
casename = 'all-2613:apt-get命令'

class Apt_get(unittest.TestCase):
    caseid = '69085'
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

    def testApt_get(self):
        (status, output) = rt('sudo apt-get update')
        self.assertTrue(0 == status, "Error: %s" % output)

    def suite():
        suite = unittest.TestSuite()
        suite.addTest(Apt_get('testApt_get'))
        return suite

if __name__ == "__main__":
    executeTestCase.runTest(Apt_get)
