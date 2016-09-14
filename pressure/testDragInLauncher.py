#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from lib import runner,utils
from lib.launcher import *
#from lib.dde_dock import *

result = True

class DragInLauncher(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        #cls.caseid = '33840'
        #cls.casename = 'all-518:添加到任务栏'
        cls.googleName = 'Google Chrome'
        launcher.freeMode()

    @classmethod
    def tearDownClass(cls):
        launcher.exitLauncher()
        '''
        global result
        utils.commitresult(cls.caseid, result)
        '''
        

    def testDragInLauncher(self):
        for i in range(1000):
            launcher.dragSrcToDest(0,6)
            launcher.dragSrcToDest(6,0)
            launcher.dragSrcToDest(0,17)
            launcher.dragSrcToDest(17,0)



    def suite():
        suite = unittest.TestSuite()
        suite.addTest(DragInLauncher('testDragInLauncher'))
        return suite
    
    class MyTestResult(runner.MyTextTestResult):
        def addError(self, test, err):
            super(DragInLauncher.MyTestResult, self).addError(test, err)
            global result
            result = result and False

        def addFailure(self, test, err):
            super(DragInLauncher.MyTestResult, self).addFailure(test, err)
            global result
            result = result and False
    
if __name__ == "__main__":
    unittest.TextTestRunner(resultclass=DragInLauncher.MyTestResult).run(DragInLauncher.suite())
