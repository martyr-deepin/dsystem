#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import gettext
import unittest
import pyautogui
from time import sleep
from lib import Dock
from lib import runTest
from lib import translation
from lib import Launcher
from lib import runTest
from lib import NotificationsDB

casename = "all-6199:同步删除图标"

class Dock_Uninstall(unittest.TestCase):
    caseid = '280080'
    @classmethod
    def setUpClass(cls):
        cls.homepath = os.path.expanduser('~')
        cls.dbpath = cls.homepath + '/.local/share/deepin-notifications/data.db'
        cls.conn = NotificationsDB(cls.dbpath)
        cls.conn.deleteAll()
        cls.launcher = Launcher()
        cls.launchername = translation.charTrans.getCharTrans('deepin-music')
        cls.appName = 'deepin-music'
        cls.dock = Dock()


    @classmethod
    def tearDownClass(cls):
        if cls.launchername not in cls.launcher.getLauncherAllApps():
            os.system('sudo apt-get install -y deepin-music')

            cls.launcher.exitLauncher()

            cls.launcher.searchApp(cls.launchername)
            sleep(2)
            cls.launcher.launcherObj.child(cls.launchername).click(3)
            sleep(1)
            for i in range(3):
                pyautogui.press('down')
                sleep(0.2)

            pyautogui.press('enter')
            cls.launcher.exitLauncher()

    def testNotUninstall(self):
        self.assertTrue(0 == self.conn.rowcount())
        self.launcher.searchApp(self.launchername)
        sleep(2)
        self.launcher.launcherObj.child(self.launchername).click(3)
        for i in range(5):
            pyautogui.press('down')
            sleep(0.1)

        pyautogui.press('enter')

        self.launcher.launcherObj.child(self.launcher.string_Cancel).click()
        apps = self.launcher.getLauncherAllApps()
        self.assertIn(self.launchername, apps)


    def testUninstall(self):
        self.assertTrue(0 == self.conn.rowcount())
        self.launcher.launcherObj.child(self.launchername).click(3)
        for i in range(5):
            pyautogui.press('down')
            sleep(0.1)
        pyautogui.press('enter')
        self.launcher.launcherObj.child(self.launcher.string_Confirm).click()
        sleep(2)
        apps = self.launcher.getLauncherAllApps()
        self.assertNotIn(self.launchername, apps)
        print ('Uninstall %s successeful' % self.launchername)

        waittime = 30
        while True:
            if 0 == self.conn.rowcount():
                sleep(1)
                waittime = waittime - 1
                print(waittime)
                continue
            elif 1 == self.conn.rowcount():
                self.assertTrue(True)
                print(waittime)
                break

        icon = self.dock.dockObj.child(self.dock.string_Deepin_Music)
        self.assertTrue(None == icon)

    def suite():
        suite = unittest.TestSuite()
        suite.addTest(Dock_Uninstall('testNotUninstall'))
        suite.addTest(Dock_Uninstall('testUninstall'))
        return suite


if __name__ == "__main__":
    unittest.installHandler()
    LOCALE_DIR = os.path.abspath("./lib/locale")
    gettext.install('dsystem', LOCALE_DIR)
    runTest(Dock_Uninstall)
