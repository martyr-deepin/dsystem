#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import unittest
from lib import executeTestCase
from lib.launcher import *
from lib.dde_dock import *

result = True
casename = 'all-531:应用卸载之后左侧分类更新测试'

class LauncherUpdateUninstall(unittest.TestCase):
    caseid = '33898'
    @classmethod
    def setUpClass(cls):
        cls.appdict = {'deepin-feedback':'深度用户反馈', 
                        'crossover-15':'CrossOver', 
                        'deepin-music':'深度音乐', 
                        'netease-cloud-music':'网易云音乐', 
                        'deepin-movie':'深度影音',
                        'apps.com.qq.im':'QQ'}

    @classmethod
    def tearDownClass(cls):
        for app in list(cls.appdict.keys()):
            if app not in launcher.getLauncherAllApps():
                subprocess.check_call('sudo apt-get install -y ' + app, shell=True)


    def testOther(self):
        subprocess.check_call('sudo apt-get remove -y deepin-feedback', shell=True)
        subprocess.check_call('sudo apt-get remove -y crossover-15', shell=True)
        kids = launcher.getKidsCategory('others')
        self.assertEqual(len(kids),0)


    def testMusic(self):
        subprocess.check_call('sudo apt-get remove -y deepin-music', shell=True)
        subprocess.check_call('sudo apt-get remove -y netease-cloud-music', shell=True)
        music_kids = launcher.getKidsCategory('music')
        self.assertEqual(len(music_kids),0)

    def testVideo(self):
        subprocess.check_call('sudo apt-get remove -y deepin-movie', shell=True)
        video_kids = launcher.getKidsCategory('video')
        self.assertEqual(len(video_kids),0)



    def suite():
        suite = unittest.TestSuite()
        suite.addTest(LauncherUpdateUninstall('testOther'))
        suite.addTest(LauncherUpdateUninstall('testMusic'))
        suite.addTest(LauncherUpdateUninstall('testVideo'))
        return suite


if __name__ == "__main__":
    executeTestCase.runTest(LauncherUpdateUninstall)
