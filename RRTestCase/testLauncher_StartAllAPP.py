# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
import json
import subprocess
import os
import glob
import gettext
from dogtail.tree import *
from pykeyboard import PyKeyboard
from pymouse import PyMouse
import time
from lib import runTest,runner,utils,window
from lib import Launcher
from lib import do_polkit_agent

casename = 'all-5334:一次启动launcher所有应用'

class Launcher_StartAllAPP(unittest.TestCase):
    caseid = '191607'

    def ParsingJson(self, lang):
        if 'zh_CN.UTF-8' == lang:
            with open('./data/defaultapp_cn_window.json', 'r') as f:
                data = json.load(f)
        else:
            with open('./data/defaultapp_en_window.json', 'r') as f:
                data = json.load(f)

        return data

    @classmethod
    def setUpClass(cls):
        cls.launcher = Launcher()
        cls.lang = os.getenv("LANG")
        cls.time_now = ''

        if "en_US.UTF-8" == cls.lang:
            cls.name_Deepin_Screenshot = "Deepin Screenshot"
            cls.string_DeepinScreenshot = "DeepinScreenshot_Desktop_"
            cls.name_Thunderbird = "Thunderbird Mail"
            cls.string_Thunderbird_Welcome = "Welcome to Thunderbird"
            cls.name_Deepin_User_Feedback = "Deepin User Feedback"
            cls.string_Deepin_User_Feedback = "deepin-feedback - Google Chrome"
        elif "zh_CN.UTF-8" == cls.lang:
            cls.name_DeepinScreenshot = "深度截图"
            cls.string_DeepinScreenshot = "深度截图"
            cls.name_Thunderbird = "雷鸟邮件"
            cls.string_Thunderbird_Welcome = "欢迎使用 Thunderbird"
            cls.name_Deepin_User_Feedback = "深度用户反馈"
            cls.string_Deepin_User_Feedback = "deepin-用户反馈 - Google Chrome"

    @classmethod
    def tearDownClass(cls):
        picture_save_path = os.path.expandvars('$HOME') + '/Desktop/' + cls.string_DeepinScreenshot + cls.time_now + '*.png'

        if glob.glob(picture_save_path):
            os.system("rm ~/Desktop/*.png")

    def terminate_deepinscreenshot(self):
        m = PyMouse()
        time.sleep(5)
        m.click(100, 100)
        m.click(100, 100)
        time_now = time.strftime('%Y%m%d', time.localtime())
        self.time_now = time_now
        picture_save_path = os.path.expandvars('$HOME') + '/Desktop/' + self.string_DeepinScreenshot + time_now + '*.png'
        print(picture_save_path)
        time.sleep(10)
        save_bool = glob.glob(picture_save_path)
        print(save_bool)
        self.assertTrue(save_bool)

    def testRunAPP(self):
        compare_type = "equal"
        appdict = self.ParsingJson(self.lang)
        for (k,v) in appdict.items():
            print(k,v)
            if v == 'null':
                continue
            self.launcher.searchApp(k)
            time.sleep(1)
            self.launcher.launcherObj.child(k).click()

            if k == 'Deepin Clone' or k == 'GParted':
                time.sleep(5)
                do_polkit_agent()

            time.sleep(10)
            if k ==  self.name_Deepin_Screenshot:
                self.terminate_deepinscreenshot()
            else:
                if k == self.name_Thunderbird :
                    thunderbird_obj = window.findWindow(self.string_Thunderbird_Welcome)
                    window.closeWindow(thunderbird_obj)
                    window_obj = window.findWindow(v, comparetype='notequal')
                    print(window_obj)
                    closeresult = window.closeWindow(window_obj)
                    self.assertEqual(None, closeresult)
                    continue
                elif k == self.name_Deepin_User_Feedback:
                    do_polkit_agent(action="Cancel")

                if k == "Google Chrome" k == 'GParted':
                    compare_type = "notequal"

                window_obj = window.findWindow(v, comparetype=compare_type)
                if None == window_obj:
                    time.sleep(10)
                    window_obj = window.findWindow(v, comparetype=compare_type)

                closeresult = window.closeWindow(window_obj)
                self.assertEqual(None, closeresult)

    def suite():
        suite = unittest.TestSuite()
        suite.addTest(Launcher_StartAllAPP('testRunAPP'))
        return suite

if __name__ == "__main__":
    unittest.installHandler()
    LOCALE_DIR = os.path.abspath("./lib/locale")
    gettext.install('dsystem', LOCALE_DIR)
    runTest(Launcher_StartAllAPP)
