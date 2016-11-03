#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from lib import runner,utils
from lib.launcher import *

result = True
caseid = '52149'
casename = "all-2234:分类模式禁用拖动排序"

class LauncherDisable(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.startTime = time.time()


    @classmethod
    def tearDownClass(cls):
        global result
        seconds = '%.3f' % (time.time() - cls.startTime)
        minutes = utils.convertToMinutes(float(seconds))
        utils.commitresult(caseid, result, minutes)
        launcher.freeMode()

    def testDisableDrag(self):
        launcher.disableDrag()
        internet = launcher.launcherObj.child('internet', roleName='list').children[0].name
        new_music = launcher.launcherObj.child('video', roleName='list').children[0].name
        self.assertNotEqual(internet,new_music)

    def suite():
        suite = unittest.TestSuite()
        suite.addTest(LauncherDisable('testDisableDrag'))
        return suite

    class MyTestResult(runner.MyTextTestResult):
        def addError(self, test, err):
            super(LauncherDisable.MyTestResult, self).addError(test, err)
            global result
            result = result and False

        def addFailure(self, test, err):
            super(LauncherDisable.MyTestResult, self).addFailure(test, err)
            global result
            result = result and False


if __name__ == "__main__":
    unittest.TextTestRunner(resultclass=LauncherDisable.MyTestResult).run(LauncherDisable.suite())
