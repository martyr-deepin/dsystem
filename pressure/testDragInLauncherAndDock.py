#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
import time
from lib import runner,utils
from lib.launcher import *
from lib.dde_dock import *

result = True

class DragInLauncherAndDock(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        #cls.caseid = '33840'
        #cls.casename = 'all-518:添加到任务栏'
        cls.googleName = 'Google Chrome'
        dockApps = Dock().getAllDockApps()
        if 'google-chrome' in dockApps:
            Dock().unDockApp(cls.googleName)
        launcher.freeMode()

    @classmethod
    def tearDownClass(cls):
        '''
        global result
        utils.commitresult(cls.caseid, result)
        '''
        launcher.exitLauncher()

    def testDragInLauncherAndDock(self):
        for i in range(1000):
            launcher.dragAppToDockFree(self.googleName,quit=False)
            dockApps = Dock().getAllDockApps()
            if 'google-chrome' in dockApps:
                Dock().unDockApp(self.googleName)




    def suite():
        suite = unittest.TestSuite()
        suite.addTest(DragInLauncherAndDock('testDragInLauncherAndDock'))
        return suite
    
    class MyTestResult(runner.MyTextTestResult):
        def addError(self, test, err):
            super(DragInLauncherAndDock.MyTestResult, self).addError(test, err)
            global result
            result = result and False

        def addFailure(self, test, err):
            super(DragInLauncherAndDock.MyTestResult, self).addFailure(test, err)
            global result
            result = result and False
    
if __name__ == "__main__":
    unittest.TextTestRunner(resultclass=DragInLauncherAndDock.MyTestResult).run(DragInLauncherAndDock.suite())
