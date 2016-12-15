#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import unittest
from lib import executeTestCase
from lib import runner,utils
from lib.launcher import *
from lib.dde_dock import *

result = True
caseid = '83365'
casename = 'all-3356:有道词典开启与关闭'

class YoudaoDict(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.appName = 'youdao-dict'
        cls.winName = '有道词典'
        cls.oldWindows = getAllWindows()


    @classmethod
    def tearDownClass(cls):
        pass
    def setUp(self):
        pass

    def tearDown(self):
        subprocess.check_call("ps aux |grep youdao |grep -v grep |grep -v backend |awk '{print $2}' |xargs kill -9", shell=True)

    def testYoudao1(self):
        subprocess.check_call(self.appName + ' &', shell=True)
        winName = getAllWindowNames()
        dockApps = Dock().getAllApps()
        self.assertIn(self.winName,winName)
        self.assertIn(self.winName,dockApps)

    def testYoudao2(self):
        Dock().dockObj.child('Launcher').click()
        launcher.searchApp(self.appName)
        sleep(1)
        pyautogui.press('enter')
        winName = getAllWindowNames()
        self.assertIn(self.winName,winName)

    def suite():
        suite = unittest.TestSuite()
        suite.addTest(YoudaoDict('testYoudao1'))
        suite.addTest(YoudaoDict('testYoudao2'))
        return suite

if __name__ == "__main__":
    runTest(YoudaoDict.suite())
