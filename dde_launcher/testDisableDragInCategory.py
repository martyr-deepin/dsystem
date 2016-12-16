#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from lib import executeTestCase
import time
from lib import runner,utils
from lib.launcher import *

result = True
casename = "all-2234:分类模式禁用拖动排序"

class LauncherDisable(unittest.TestCase):
    caseid = '52149'
    @classmethod
    def setUpClass(cls):
        pass


    @classmethod
    def tearDownClass(cls):
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



if __name__ == "__main__":
    executeTestCase.runTest(LauncherDisable)
