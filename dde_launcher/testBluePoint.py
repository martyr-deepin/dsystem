#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from lib import executeTestCase
import time
from lib import runner,utils
from lib.launcher import *

result = True
casename = "all-524:预装应用蓝点标志测试"

class BluePoint(unittest.TestCase):
    caseid = '33866'
    
    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def testBluePoint(self):
        app = launcher.getNewInstalledApps()
        print(app)
        self.assertEqual(len(app), 0)


    def suite():
        suite = unittest.TestSuite()
        suite.addTest(BluePoint('testBluePoint'))
        return suite


if __name__ == "__main__":
    executeTestCase.runTest(BluePoint)
