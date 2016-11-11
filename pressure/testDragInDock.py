#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
import time
from lib import runner,utils
#from lib.launcher import *
from lib.dde_dock import *

result = True

class DragInDock(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass


    def testDragInDock(self):
        apps = Dock().getDockedApps()
        src = apps[2]
        dest = apps[4]
        for i in range(1000):
            Dock().dragInDock(src,dest)
            Dock().dragInDock(dest,src)



    def suite():
        suite = unittest.TestSuite()
        suite.addTest(DragInDock('testDragInDock'))
        return suite
    
    class MyTestResult(runner.MyTextTestResult):
        def addError(self, test, err):
            super(DragInDock.MyTestResult, self).addError(test, err)
            global result
            result = result and False

        def addFailure(self, test, err):
            super(DragInDock.MyTestResult, self).addFailure(test, err)
            global result
            result = result and False
    
if __name__ == "__main__":
    unittest.TextTestRunner(resultclass=DragInDock.MyTestResult).run(DragInDock.suite())
