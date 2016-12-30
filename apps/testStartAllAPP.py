# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
import json
import subprocess
import os
from dogtail.tree import *
from pykeyboard import PyKeyboard
import time
from lib import executeTestCase,runner,utils,window
from lib.launcher import *

casename = 'start all launcher apps once time'

class StartAllAPP(unittest.TestCase):
    caseid = 'nocaseid'

    def ParsingJsonCn(self):
        with open('../data/defaultapp_cn_window.json', 'r') as f:
            data = json.load(f)
        return data

    @classmethod
    def setUpClass(cls):
        pass


    @classmethod
    def tearDownClass(cls):
        pass


    def terminate_deepinscreenshot(self):
        p = PyKeyboard()
        p.press_key('Return')
        p.release_key('Return')
        time_now = time.strftime('%Y%m%d%H%M%S', time.localtime())
        picture_save_path = os.path.expandvars('$HOME') + '/Desktop/' + '深度截图' + time_now + '.png'
        print(picture_save_path)
        time.sleep(2)
        save_bool = os.path.exists(picture_save_path)
        print(save_bool)
        self.assertTrue(save_bool)

    def testRunAPP(self):
        appdict = self.ParsingJsonCn()
        for (k,v) in appdict.items():
            print(k,v)
            if v == 'null':
                continue
            launcher.searchApp(k)
            time.sleep(1)
            launcher.launcherObj.child(k).click()   
            time.sleep(10)
            if k ==  '深度截图':
                self.terminate_deepinscreenshot()
            else:
                window_obj = window.findWindow(v)
                print(window_obj)
                if k == '雷鸟邮件':
                    thunderbird_obj = window.findWindow('欢迎使用 Thunderbird')
                    window.closeWindow(thunderbird_obj)
                closeresult = window.closeWindow(window_obj)
                self.assertEqual(None, closeresult)

    def suite():
        suite = unittest.TestSuite()
        suite.addTest(StartAllAPP('testRunAPP'))
        return suite

if __name__ == "__main__":
    executeTestCase.runTest(StartAllAPP)
