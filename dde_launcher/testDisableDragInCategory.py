#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from lib import runner,utils
from lib.launcher import *

result = True
caseid = '52149'
casename = "all-2234:分类模式禁用拖动排序"

class MyTestResult(runner.MyTextTestResult):
    def addError(self, test, err):
        super(MyTestResult, self).addError(test, err)
        global result
        result = result and False

    def addFailure(self, test, err):
        super(MyTestResult, self).addFailure(test, err)
        global result
        result = result and False

class LauncherDisable(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass


    @classmethod
    def tearDownClass(cls):
        global result
        utils.commitresult(caseid, result)
        launcher.freeMode()

    def testDisableDrag(self):
        launcher.disableDrag()
        internet = launcher.launcherObj.child('internet', roleName='list').children[0].name
        new_music = launcher.launcherObj.child('music', roleName='list').children[0].name
        self.assertNotEqual(internet,new_music)

def suite():
    suite = unittest.TestSuite()
    suite.addTest(LauncherDisable('testDisableDrag'))
    return suite

if __name__ == "__main__":
    unittest.TextTestRunner(verbosity=1).run(suite())
