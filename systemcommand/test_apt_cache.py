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
casename = 'all-2614:apt-cache命令'

class Apt_cache(unittest.TestCase):
    caseid = '69087'
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

    def testApt_cache(self):
        (status, output) = rt('apt-cache policy dde')
        self.assertTrue(0 == status, "Error: %s" % output)

    def suite():
        suite = unittest.TestSuite()
        suite.addTest(Apt_cache('testApt_cache'))
        return suite

if __name__ == "__main__":
    executeTestCase.runTest(Apt_cache)
