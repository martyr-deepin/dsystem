#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import unittest
from lib import executeTestCase
from lib import runner,utils
from lib.launcher import *
from lib.dde_dock import *

result = True
casename = 'all-3348:深度影院启动'

class DeepinMovie(unittest.TestCase):
    caseid = '83329'
    @classmethod
    def setUpClass(cls):
        cls.appName = 'deepin-movie'
        cls.winName = '深度影院'
        cls.oldWindows = getAllWindows()


    @classmethod
    def tearDownClass(cls):
        if len(cls.newWindows) > len(cls.oldWindows):
            newWindow = cls.newWindows[-1]
            newWindow.close(1)

    def setUp(self):
        pass

    def tearDown(self):
        newWindows = getAllWindows()
        if len(newWindows) > len(self.oldWindows):
            newWindow = newWindows[-1]
            newWindow.close(1)

    def tearDown(self):
        newWindows = getAllWindows()
        if len(newWindows) > len(self.oldWindows):
            newWindow = newWindows[-1]
            newWindow.close(1)
    def testDeepinMovie1(self):
        subprocess.check_call(self.appName + ' &', shell=True)
        winNames = getAllWindowNames()
        self.assertIn(self.winName,winNames)

    def testDeepinMovie2(self):
        Dock().dockObj.child('深度影院').click()
        winNames = getAllWindowNames()
        self.assertIn(self.winName,winNames)

    def testDeepinMovie3(self):
        launcher.searchApp(self.appName)
        sleep(1)
        pyautogui.press('enter')
        winName = getWindowName()
        self.assertEqual(self.winName,winName)

    def suite():
        suite = unittest.TestSuite()
        suite.addTest(DeepinMovie('testDeepinMovie1'))
        suite.addTest(DeepinMovie('testDeepinMovie2'))
        suite.addTest(DeepinMovie('testDeepinMovie3'))
        return suite

if __name__ == "__main__":
    executeTestCase.runTest(DeepinMovie)
