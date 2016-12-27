#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import unittest
import json
import subprocess
from dogtail.tree import *
import time
from pymouse import PyMouse
from lib import executeTestCase,runner,utils,window
from lib.launcher import *
from lib.dde_dock import *


casename = 'start all launcher apps once time'

class StartAllAPP(unittest.TestCase):
    caseid = 'nocaseid'
    def ParsingJsonCn():
        with open('../data/defaultapp_cn_window.json', 'r') as f:
            data = json.load(f)
        return data

    @classmethod
    def setUpClass(cls):
        pass


    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        pass

    def run_terminate_deepinscreenshot(self,pname):
        (status,output) = subprocess.getstatusoutput('ps -ef|grep %s|grep -v grep' % pname)
        self.assertEqual(0, status)
        time.sleep(1)
        return_code = subprocess.check_call('killall %s' % pname, shell=True)
        self.assertEqual(0, return_code)

    def testRunAPP(self):
        appdict = StartAllAPP.ParsingJsonCn()
        for (k,v) in appdict.items():
            print(k,v)
            if v == 'null':
                continue
            elif k ==  '深度截图':
                StartAllAPP.run_terminate_deepinscreenshot(v)
            else:
                m = PyMouse()
                launcher.searchApp(k)
                time.sleep(1)
                (x, y) = launcher.getAppCenterCoor(k)
                print(x,y)
                m.click(int(x), int(y))
                time.sleep(3)
                window_obj = window.findWindow(v)
                print(window_obj)
                self.assertIsNotNone(window_obj)
                window.closeWindow(window_obj)

    def suite():
        suite = unittest.TestSuite()
        suite.addTest(StartAllAPP('testRunAPP'))
        return suite

if __name__ == "__main__":
    executeTestCase.runTest(StartAllAPP)
