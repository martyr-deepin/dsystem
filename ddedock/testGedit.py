#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
import time
from lib import utils
from lib import runner
from lib.launcher import launcher
from dogtail import rawinput

result = True
caseid = '33428'
casename = "all-439:gedit"

class Gedit(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.startTime = time.time()
        cls.gediticonname = "文本编辑器"
        cls.ddedockobject = utils.getDdeDockObject()

        if utils.dock.displaymode_fashion != utils.getDdeDockDisplayMode():
            utils.setDdeDockDisplayMode(utils.dock.displaymode_fashion)

        if utils.dock.position_bottom != utils.getDdeDockPosition():
            utils.setDdeDockPosition(utils.dock.position_bottom)

    @classmethod
    def tearDownClass(cls):
        seconds = "%.3f" % (time.time() - cls.startTime)
        minutes = utils.convertToMinutes(float(seconds))
        global result
        utils.commitresult(caseid, result, minutes)

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

        utils.keyTypeString("gedit")

        try:
            launcher_icon = self.ddedockobject.child("Launcher")
        except:
            self.assertTrue(False, "Can't find launcher icon")


        apps = launcher.getLauncherAllApps()
        fromXY = launcher.getAppCenterCoor(apps[0])
        toXY = utils.getDockIconCenterPoint(launcher_icon)

        utils.mouseDragIconToDock((int(fromXY[0]), int(fromXY[1])), toXY)
        time.sleep(1)
        self.testGeditExistOnDock()
        time.sleep(1)

    def testDragDockIconToDesktop(self):
        icongedit_icon = self.ddedockobject.child(self.gediticonname)
        fromXY = utils.getDockIconCenterPoint(icongedit_icon)
        utils.mouseDrag(fromXY, (fromXY[0], fromXY[1] - 100))

        ddedock = utils.getDdeDockObject()
        icongedit_icon_later = ddedock.child(self.gediticonname)
        self.assertTrue((0, 0) == icongedit_icon_later.position)
        self.assertTrue((0, 0) == icongedit_icon_later.size)

    def testOpenGedit(self):
        icongedit = self.ddedockobject.child(self.gediticonname)
        icongedit.click()
        geditwin1 = utils.findWindow("无标题文档 1 - gedit")
        self.assertTrue(geditwin1 != None)

        icongedit.click(3)
        utils.keySingle(utils.k.down_key)
        utils.keySingle(utils.k.enter_key)
        geditwin2 = utils.findWindow("无标题文档 2 - gedit")
        self.assertTrue(geditwin2 != None)

        icongedit.click(3)
        utils.keySingle(utils.k.down_key)
        utils.keySingle(utils.k.down_key)
        utils.keySingle(utils.k.enter_key)
        geditwin3 = utils.findWindow("无标题文档 3 - gedit")
        self.assertTrue(geditwin3 != None)

        icongedit.click(3)
        utils.keySingle(utils.k.down_key)
        utils.keySingle(utils.k.down_key)
        utils.keySingle(utils.k.down_key)
        utils.keySingle(utils.k.enter_key)
        geditwin4 = utils.findWindow("无标题文档 4 - gedit")
        self.assertTrue(geditwin4 != None)

    def testCloseGedit(self):
        icongedit = self.ddedockobject.child(self.gediticonname)
        icongedit.click(3)
        utils.keySingle(utils.k.down_key)
        utils.keySingle(utils.k.down_key)
        utils.keySingle(utils.k.down_key)
        utils.keySingle(utils.k.down_key)
        utils.keySingle(utils.k.enter_key)
        geditwin1 = utils.findWindow("无标题文档 1 - gedit", mode="nowait")
        geditwin2 = utils.findWindow("无标题文档 2 - gedit", mode="nowait")
        geditwin3 = utils.findWindow("无标题文档 3 - gedit", mode="nowait")
        geditwin4 = utils.findWindow("无标题文档 4 - gedit", mode="nowait")
        self.assertTrue(None == geditwin1)
        self.assertTrue(None == geditwin2)
        self.assertTrue(None == geditwin3)
        self.assertTrue(None == geditwin4)

    def testGeditExistOnDock(self):
        try:
            icongedit = self.ddedockobject.child(self.gediticonname)
            self.assertTrue(icongedit.size[0] > 1)
            self.assertTrue(icongedit.size[1] > 1)
            self.assertTrue(icongedit.position[0] > 1)
            self.assertTrue(icongedit.position[1] > 1)
        except:
            self.assertTrue(False, "Icon Gedit doesn't exist on Dock")


    def suite():
        suite = unittest.TestSuite()
        suite.addTest(Gedit('testDragIconToDock'))
        suite.addTest(Gedit('testOpenGedit'))
        suite.addTest(Gedit('testCloseGedit'))
        suite.addTest(Gedit('testDragDockIconToDesktop'))

        return suite

    class MyTestResult(runner.MyTextTestResult):
        def addError(self, test, err):
            super(Gedit.MyTestResult, self).addError(test, err)
            global result
            result = result and False

        def addFailure(self, test, err):
            super(Gedit.MyTestResult, self).addFailure(test, err)
            global result
            result = result and False

if __name__ == "__main__":
    unittest.TextTestRunner(resultclass=Gedit.MyTestResult).run(Gedit.suite())
