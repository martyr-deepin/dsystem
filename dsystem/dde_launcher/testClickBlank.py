#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from lib import executeTestCase
from lib.launcher import *

result = True
casename = "all-540:单击空白处退出"

class ClickBlank(unittest.TestCase):
    caseid = '33941'
    @classmethod
    def setUpClass(cls):
        cls.text1 = 'deepin'
        cls.text2 = 'testtest'
        launcher.freeMode()

    @classmethod
    def tearDownClass(cls):
        launcher.freeMode()
        launcher.exitLauncher()

    def testFreeMode(self):
        launcher.openLauncher()
        apps = launcher.getLauncherAllApps()
        upApp = apps[3]
        upAppPosition = launcher.launcherObj.child(upApp).position
        upBlank = (upAppPosition[0]-20, upAppPosition[1]-20)
        pyautogui.click(upBlank)
        win = getWindowName()
        self.assertNotEqual('dde-launcher', win)

        launcher.openLauncher()
        leftApp = apps[7]
        leftAppPosition = launcher.launcherObj.child(leftApp).position
        leftBlank = (leftAppPosition[0]-20, leftAppPosition[1]-20)
        pyautogui.click(leftBlank)
        win = getWindowName()
        self.assertNotEqual('dde-launcher', win)

        launcher.openLauncher()
        rightApp = apps[13]
        rightAppPosition = launcher.launcherObj.child(rightApp).position
        rightBlank = (rightAppPosition[0]+200, rightAppPosition[1]+20)
        pyautogui.click(rightBlank)
        win = getWindowName()
        self.assertNotEqual('dde-launcher', win)

        launcher.openLauncher()
        downApp = apps[17]
        downAppPosition = launcher.launcherObj.child(downApp).position
        downBlank = (downAppPosition[0]+160, downAppPosition[1]+160)
        pyautogui.click(downBlank)
        win = getWindowName()
        self.assertNotEqual('dde-launcher', win)

    def testClassifyMode(self):
        launcher.categoryMode()
        launcher.openLauncher()
        appPosition = launcher.launcherObj.child('internet',roleName='list').children[1].position
        upBlank = appPosition[0]-20, appPosition[1]-20
        pyautogui.click(upBlank)
        win = getWindowName()
        self.assertNotEqual('dde-launcher', win)

        launcher.openLauncher()
        appPosition = launcher.launcherObj.child('chat',roleName='list').children[0].position
        leftBlank = appPosition[0]-20, appPosition[1]-20
        pyautogui.click(leftBlank)
        win = getWindowName()
        self.assertNotEqual('dde-launcher', win)

        launcher.openLauncher()
        appPosition = launcher.launcherObj.child('chat',roleName='list').children[0].position
        rightBlank = appPosition[0]+200, appPosition[1]+20
        pyautogui.click(rightBlank)
        win = getWindowName()
        self.assertNotEqual('dde-launcher', win)

        launcher.openLauncher()
        appPosition = launcher.launcherObj.child('music',roleName='list').children[1].position
        downBlank = appPosition[0]+160, appPosition[1]+160
        pyautogui.click(downBlank)
        win = getWindowName()
        self.assertNotEqual('dde-launcher', win)

    def testSearch1(self):
        launcher.searchApp(self.text1)
        searchPosition = launcher.launcherObj.child('search-edit').position
        searchSize = launcher.launcherObj.child('search-edit').size
        upBlank = searchPosition[0]+searchSize[0]/2, searchPosition[1]+searchSize[1]+20
        sleep(1)
        pyautogui.click(upBlank)
        win = getWindowName()
        self.assertNotEqual('dde-launcher', win)

        launcher.searchApp(self.text1)
        leftBlank = searchPosition[0]-500, searchPosition[1]+500
        sleep(1)
        pyautogui.click(leftBlank)
        win = getWindowName()
        self.assertNotEqual('dde-launcher', win)

        launcher.searchApp(self.text1)
        rightBlank = searchPosition[0]+500, searchPosition[1]+500
        sleep(1)
        pyautogui.click(rightBlank)
        win = getWindowName()
        self.assertNotEqual('dde-launcher', win)

        launcher.searchApp(self.text1)
        downBlank = searchPosition[0]+searchSize[0]/2, searchPosition[1]+500
        sleep(1)
        pyautogui.click(downBlank)
        win = getWindowName()
        self.assertNotEqual('dde-launcher', win)

    def testSearch2(self):
        launcher.searchApp(self.text2)
        searchPosition = launcher.launcherObj.child('search-edit').position
        searchSize = launcher.launcherObj.child('search-edit').size
        upBlank = searchPosition[0]+searchSize[0]/2, searchPosition[1]+searchSize[1]+20
        sleep(1)
        pyautogui.click(upBlank)
        win = getWindowName()
        self.assertNotEqual('dde-launcher', win)

        launcher.searchApp(self.text2)
        leftBlank = searchPosition[0]-500, searchPosition[1]+500
        sleep(1)
        pyautogui.click(leftBlank)
        win = getWindowName()
        self.assertNotEqual('dde-launcher', win)

        launcher.searchApp(self.text2)
        rightBlank = searchPosition[0]+500, searchPosition[1]+500
        sleep(1)
        pyautogui.click(rightBlank)
        win = getWindowName()
        self.assertNotEqual('dde-launcher', win)

        launcher.searchApp(self.text2)
        downBlank = searchPosition[0]+searchSize[0]/2, searchPosition[1]+500
        sleep(1)
        pyautogui.click(downBlank)
        win = getWindowName()
        self.assertNotEqual('dde-launcher', win)

    def suite():
        suite = unittest.TestSuite()
        suite.addTest(ClickBlank('testFreeMode'))
        suite.addTest(ClickBlank('testClassifyMode'))
        suite.addTest(ClickBlank('testSearch1'))
        suite.addTest(ClickBlank('testSearch2'))
        return suite


if __name__ == "__main__":
    executeTestCase.runTest(ClickBlank)
