#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import gettext
import unittest
from lib import DaemonDock
from lib import runTest

casename = "all-5371:检查dock是否正常启动"

class Dock_Exist(unittest.TestCase):
    caseid = '191714'

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def testExist(self):
        daemondock = DaemonDock()
        rect = daemondock.getFrontendWindowRect()
        print(rect)
        self.assertTrue(rect[0] > 1)
        self.assertTrue(rect[1] > 1)
        self.assertTrue(rect[2] > 1)
        self.assertTrue(rect[3] > 1)

    def suite():
        suite = unittest.TestSuite()
        suite.addTest(Dock_Exist('testExist'))
        return suite

if __name__ == "__main__":
    unittest.installHandler()
    LOCALE_DIR = os.path.abspath("./lib/locale")
    gettext.install('dsystem', LOCALE_DIR)
    runTest(Dock_Exist)
