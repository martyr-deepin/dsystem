#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
import time
from lib import runner,utils
from lib.launcher import *

result = True
caseid = '33866'
casename = "all-524:预装应用蓝点标志测试"

class BluePoint(unittest.TestCase):
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

    def testBluePoint(self):
        app = launcher.getNewInstalledApps()
        #print(app)
        self.assertListEqual(app, [])


    def suite():
        suite = unittest.TestSuite()
        suite.addTest(BluePoint('testBluePoint'))
        return suite

    class MyTestResult(runner.MyTextTestResult):
        def addError(self, test, err):
            super(BluePoint.MyTestResult, self).addError(test, err)
            global result
            result = result and False

        def addFailure(self, test, err):
            super(BluePoint.MyTestResult, self).addFailure(test, err)
            global result
            result = result and False

if __name__ == "__main__":
    unittest.TextTestRunner(resultclass=BluePoint.MyTestResult).run(BluePoint.suite())
