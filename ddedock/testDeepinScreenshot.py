#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import glob
import unittest
import time
from lib import utils
from lib import runner
from lib.launcher import launcher
from dogtail import rawinput
from subprocess import getstatusoutput as rt

result = True

class DeepinScreenshot(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.caseid = '33434'
        cls.casename = "all-440:深度截图"
        cls.screenshoticonname = "深度截图"
        cls.ddedockobject = utils.getDdeDockObject()

        if utils.dock.displaymode_fashion != utils.getDdeDockDisplayMode():
            utils.setDdeDockDisplayMode(utils.dock.displaymode_fashion)

        if utils.dock.position_bottom != utils.getDdeDockPosition():
            utils.setDdeDockPosition(utils.dock.position_bottom)

    @classmethod
    def tearDownClass(cls):
        global result
        utils.commitresult(cls.caseid, result)

        if utils.dock.displaymode_fashion != utils.getDdeDockDisplayMode():
            utils.setDdeDockDisplayMode(utils.dock.displaymode_fashion)

        if utils.dock.position_bottom != utils.getDdeDockPosition():
            utils.setDdeDockPosition(utils.dock.position_bottom)

    def testDragIconToDock(self):
        utils.keySingle(utils.k.windows_l_key)
        try:
            launcherwin = utils.findWindow("dde-launcher")
        except:
            self.assertTrue(False, "Can't open dde-launcher")

        utils.keyTypeString("deepin-screenshot")

        try:
            launcher_icon = self.ddedockobject.child("Launcher")
        except:
            self.assertTrue(False, "Can't find launcher icon")


        apps = launcher.getLauncherAllApps()
        fromXY = launcher.getAppCenterCoor(apps[0])
        toXY = utils.getDockIconCenterPoint(launcher_icon)

        utils.mouseDragIconToDock((int(fromXY[0]), int(fromXY[1])), toXY)
        time.sleep(1)
        self.testDeepinScreenshotExistOnDock()
        time.sleep(1)

    def testDragDockIconToDesktop(self):
        icongedit_icon = self.ddedockobject.child(self.gediticonname)
        fromXY = utils.getDockIconCenterPoint(icongedit_icon)
        utils.mouseDrag(fromXY, (fromXY[0], fromXY[1] - 100))

        ddedock = utils.getDdeDockObject()
        icongedit_icon_later = ddedock.child(self.gediticonname)
        self.assertTrue((0, 0) == icongedit_icon_later.position)
        self.assertTrue((0, 0) == icongedit_icon_later.size)

    def testOpenDeepinScreenshotRun(self):
        iconscreenshot = self.ddedockobject.child(self.screenshoticonname)
        iconscreenshot.click(3)
        utils.keySingle(utils.k.down_key)
        utils.keySingle(utils.k.enter_key)

    def testOpenDeepinScreenshotDelay(self):
        iconscreenshot = self.ddedockobject.child(self.screenshoticonname)
        iconscreenshot.click(3)
        utils.keySingle(utils.k.down_key)
        utils.keySingle(utils.k.down_key)
        utils.keySingle(utils.k.down_key)
        utils.keySingle(utils.k.enter_key)
        time.sleep(5)

    def testOpenDeepinScreenshotFullScreen(self):
        home = os.path.expanduser("~")
        desktoppath = home + "/桌面"

        pngscreen = glob.glob(desktoppath + "/深度截图*.png")

        for png in pngscreen:
            os.remove(png)

        iconscreenshot = self.ddedockobject.child(self.screenshoticonname)
        iconscreenshot.click(3)
        utils.keySingle(utils.k.down_key)
        utils.keySingle(utils.k.down_key)
        utils.keySingle(utils.k.enter_key)

        max_delay = 10

        while True:
            time.sleep(1)
            max_delay = max_delay - 1
            png = glob.glob(desktoppath + "/深度截图*.png")

            if len(png) > 0:
                self.assertTrue(True)
                for f in png:
                    os.remove(f)

                break

            if 0 == max_delay and 0 == len(png):
                self.assertTrue(False, "Icon Menu FullScreen doesn't work")
                break


    def testOpenDeepinScreenshotKeyPrint(self):
        utils.keySingle(utils.k.print_screen_key)
        max_delay = 10

        home = os.path.expanduser("~")
        desktoppath = home + "/桌面"

        pngscreen = glob.glob(desktoppath + "/深度截图*.png")

        for png in pngscreen:
            os.remove(png)

        while True:
            time.sleep(1)
            max_delay = max_delay - 1
            png = glob.glob(desktoppath + "/深度截图*.png")

            if len(png) > 0:
                self.assertTrue(True)
                for f in png:
                    os.remove(f)

                break

            if 0 == max_delay and 0 == len(png):
                self.assertTrue(False, "Key Printscreen doesn't work")
                break

    def testDeepinScreenshotExistOnDock(self):
        try:
            iconscreenshot = self.ddedockobject.child(self.screenshoticonname)
            self.assertTrue(iconscreenshot.size[0] > 1, "size = %s" % str(iconscreenshot.size))
            self.assertTrue(iconscreenshot.size[1] > 1)
            self.assertTrue(iconscreenshot.position[0] > 1)
            self.assertTrue(iconscreenshot.position[1] > 1)
        except:
            self.assertTrue(False, "Icon Screenshot doesn't exist on Dock")


    def testCloseDeepinScreenshot(self):
        time.sleep(1)
        rawinput.click(int(utils.resolution.width/2), int(utils.resolution.height/2), 3)
        (status, output) = rt("ps -ef | grep /usr/bin/deepin-screenshot | grep -v grep | awk '{print $9}'")
        time.sleep(1)
        self.assertTrue('' == output)


    def testTaskExist(self):
        max_delay = 10

        while True:
            time.sleep(1)
            max_delay = max_delay - 1
            (status, output) = rt("ps -ef | grep /usr/bin/deepin-screenshot | grep -v grep | awk '{print $9}'")
            if '' == output and 0 != max_delay:
                continue

            if ('' == output and 0 == max_delay) or ('/usr/bin/deepin-screen-shot' != output and 0 == max_delay):
                self.assertTrue(False, "Icon Menu delay screenshot doesn't work")
                break

            if '/usr/bin/deepin-screenshot' == output:
                self.assertTrue('/usr/bin/deepin-screenshot' == output)
                break

    def testDragDockIconToDesktop(self):
        iconscreenshot = self.ddedockobject.child(self.screenshoticonname)
        fromXY = utils.getDockIconCenterPoint(iconscreenshot)
        utils.mouseDrag(fromXY, (fromXY[0], fromXY[1] - 100))

        ddedock = utils.getDdeDockObject()
        iconscreenshot_later = ddedock.child(self.screenshoticonname)
        self.assertTrue((0, 0) == iconscreenshot_later.position)
        self.assertTrue((0, 0) == iconscreenshot_later.size)

    def testExChangeDisplayMode(self):
        if utils.getDdeDockDisplayMode() == utils.dock.displaymode_fashion:
            utils.setDdeDockDisplayMode(utils.dock.displaymode_efficient)
        elif utils.getDdeDockDisplayMode() == utils.dock.displaymode_efficient:
            utils.setDdeDockDisplayMode(utils.dock.displaymode_fashion)

    def suite():
        suite = unittest.TestSuite()
        suite.addTest(DeepinScreenshot('testDragIconToDock'))
        suite.addTest(DeepinScreenshot('testDeepinScreenshotExistOnDock'))
        suite.addTest(DeepinScreenshot('testOpenDeepinScreenshotRun'))
        suite.addTest(DeepinScreenshot('testTaskExist'))
        suite.addTest(DeepinScreenshot('testCloseDeepinScreenshot'))
        suite.addTest(DeepinScreenshot('testOpenDeepinScreenshotKeyPrint'))
        suite.addTest(DeepinScreenshot('testOpenDeepinScreenshotFullScreen'))
        suite.addTest(DeepinScreenshot('testOpenDeepinScreenshotDelay'))
        suite.addTest(DeepinScreenshot('testTaskExist'))
        suite.addTest(DeepinScreenshot('testCloseDeepinScreenshot'))
        suite.addTest(DeepinScreenshot('testDragDockIconToDesktop'))

        # Change Display Mode
        suite.addTest(DeepinScreenshot('testExChangeDisplayMode'))

        suite.addTest(DeepinScreenshot('testDragIconToDock'))
        suite.addTest(DeepinScreenshot('testDeepinScreenshotExistOnDock'))
        suite.addTest(DeepinScreenshot('testOpenDeepinScreenshotRun'))
        suite.addTest(DeepinScreenshot('testTaskExist'))
        suite.addTest(DeepinScreenshot('testCloseDeepinScreenshot'))
        suite.addTest(DeepinScreenshot('testOpenDeepinScreenshotKeyPrint'))
        suite.addTest(DeepinScreenshot('testOpenDeepinScreenshotFullScreen'))
        suite.addTest(DeepinScreenshot('testOpenDeepinScreenshotDelay'))
        suite.addTest(DeepinScreenshot('testTaskExist'))
        suite.addTest(DeepinScreenshot('testCloseDeepinScreenshot'))
        suite.addTest(DeepinScreenshot('testDragDockIconToDesktop'))

        return suite

    class MyTestResult(runner.MyTextTestResult):
        def addError(self, test, err):
            super(DeepinScreenshot.MyTestResult, self).addError(test, err)
            global result
            result = result and False

        def addFailure(self, test, err):
            super(DeepinScreenshot.MyTestResult, self).addFailure(test, err)
            global result
            result = result and False

if __name__ == "__main__":
    unittest.TextTestRunner(resultclass=DeepinScreenshot.MyTestResult).run(DeepinScreenshot.suite())
