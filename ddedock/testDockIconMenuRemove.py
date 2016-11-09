#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
import time
from lib import utils
from lib import runner
from lib.launcher import launcher
from dogtail.tree import root
from dogtail import rawinput

result = True
caseid = '33458'
casename = "all-445:移除驻留"

class DockIconMenuRemove(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.startTime = time.time()
        cls.filemanagericonname = "深度文件管理器"
        cls.filemanagerwindowname = "深度文件管理器"
        cls.filemanagerlauncher = "dde-file-manager"
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

    def testOpenRun(self):
        try:
            iconfilemanager = self.ddedockobject.child(self.filemanagericonname)
        except:
            self.assertTrue(False, "Can't find the file manager icon on the Dock")

        iconfilemanager.click(3)

        try:
            dockmenuapp = root.application('deepin-menu', '/usr/lib/deepin-menu')
            dockmenu = dockmenuapp.child(utils.dock.dockmenuname)
        except:
            self.assertTrue(False, "Can't find dockmenu")

        self.assertTrue(dockmenu.position[0] > 1)
        self.assertTrue(dockmenu.position[1] > 1)
        self.assertTrue(dockmenu.size[0] > 1)
        self.assertTrue(dockmenu.size[1] > 1)

        utils.keySingle(utils.k.down_key)
        utils.keySingle(utils.k.enter_key)

    def testSelectMenuNewWindow(self):
        try:
            iconfilemanager = self.ddedockobject.child(self.filemanagericonname)
        except:
            self.assertTrue(False, "Can't find the file manager icon on the Dock")

        iconfilemanager.click(3)

        try:
            dockmenuapp = root.application('deepin-menu', '/usr/lib/deepin-menu')
            dockmenu = dockmenuapp.child(utils.dock.dockmenuname)
        except:
            self.assertTrue(False, "Can't find dockmenu")

        self.assertTrue(dockmenu.position[0] > 1)
        self.assertTrue(dockmenu.position[1] > 1)
        self.assertTrue(dockmenu.size[0] > 1)
        self.assertTrue(dockmenu.size[1] > 1)

        utils.keySingle(utils.k.down_key)
        utils.keySingle(utils.k.down_key)
        utils.keySingle(utils.k.enter_key)

    def testSelectMenuCloseAll(self):
        try:
            iconfilemanager = self.ddedockobject.child(self.filemanagericonname)
        except:
            self.assertTrue(False, "Can't find the file manager icon on the Dock")

        iconfilemanager.click(3)

        try:
            dockmenuapp = root.application('deepin-menu', '/usr/lib/deepin-menu')
            dockmenu = dockmenuapp.child(utils.dock.dockmenuname)
        except:
            self.assertTrue(False, "Can't find dockmenu")

        self.assertTrue(dockmenu.position[0] > 1)
        self.assertTrue(dockmenu.position[1] > 1)
        self.assertTrue(dockmenu.size[0] > 1)
        self.assertTrue(dockmenu.size[1] > 1)

        utils.keySingle(utils.k.down_key)
        utils.keySingle(utils.k.down_key)
        utils.keySingle(utils.k.down_key)
        utils.keySingle(utils.k.enter_key)

    def testSelectMenuUnDock(self):
        try:
            iconfilemanager = self.ddedockobject.child(self.filemanagericonname)
        except:
            self.assertTrue(False, "Can't find the file manager icon on the Dock")

        iconfilemanager.click(3)

        try:
            dockmenuapp = root.application('deepin-menu', '/usr/lib/deepin-menu')
            dockmenu = dockmenuapp.child(utils.dock.dockmenuname)
        except:
            self.assertTrue(False, "Can't find dockmenu")

        self.assertTrue(dockmenu.position[0] > 1)
        self.assertTrue(dockmenu.position[1] > 1)
        self.assertTrue(dockmenu.size[0] > 1)
        self.assertTrue(dockmenu.size[1] > 1)

        utils.keySingle(utils.k.down_key)
        utils.keySingle(utils.k.down_key)
        utils.keySingle(utils.k.down_key)
        utils.keySingle(utils.k.down_key)
        utils.keySingle(utils.k.down_key)
        utils.keySingle(utils.k.enter_key)

    def testFileManagerExist(self):
        filemanagerwinlist = utils.findWindowList(self.filemanagerwindowname)
        self.assertTrue(3 == len(filemanagerwinlist))

    def testCloseFileManager(self):
        filemanagerwin = utils.WindowState(self.filemanagerwindowname)
        filemanagerwin.close()
        win = utils.findWindow(self.filemanagerwindowname, mode="nowait")
        self.assertTrue(None == win)

    def minimizeWin(self):
        filemanagerwin = utils.WindowState(self.filemanagerwindowname)
        filemanagerwin.minimize()
        state = filemanagerwin.is_minimized()
        self.assertTrue(state)

    def testExpectResult(self):
        filemanagerwin = utils.findWindow(self.filemanagerwindowname, mode="nowait")
        self.assertTrue(None == filemanagerwin)

        try:
            iconfilemanager = self.ddedockobject.child(self.filemanagericonname)
            self.assertTrue((0, 0) == iconfilemanager.position)
            self.assertTrue((0, 0) == iconfilemanager.size)
        except:
            self.assertTrue(False)

    def testExChangeDisplayMode(self):
        if utils.getDdeDockDisplayMode() == utils.dock.displaymode_fashion:
            utils.setDdeDockDisplayMode(utils.dock.displaymode_efficient)
        elif utils.getDdeDockDisplayMode() == utils.dock.displaymode_efficient:
            utils.setDdeDockDisplayMode(utils.dock.displaymode_fashion)

    def testDdeFileManagerExistOnDock(self):
        try:
            iconfilemanager = self.ddedockobject.child(self.filemanagericonname)
            self.assertTrue(iconfilemanager.size[0] > 1, "size = %s" % str(iconfilemanager.size))
            self.assertTrue(iconfilemanager.size[1] > 1)
            self.assertTrue(iconfilemanager.position[0] > 1, "position = %s" % str(iconfilemanager.position))
            self.assertTrue(iconfilemanager.position[1] > 1)
        except:
            self.assertTrue(False)

    def testDragIconToDock(self):
        utils.keySingle(utils.k.windows_l_key)
        try:
            launcherwin = utils.findWindow("dde-launcher")
        except:
            self.assertTrue(False, "Can't open dde-launcher")

        utils.keyTypeString(self.filemanagerlauncher)

        try:
            launcher_icon = self.ddedockobject.child("Launcher")
        except:
            self.assertTrue(False, "Can't find launcher icon")


        apps = launcher.getLauncherAllApps()
        fromXY = launcher.getAppCenterCoor(apps[0])
        toXY = utils.getDockIconCenterPoint(launcher_icon)

        utils.mouseDragIconToDock((int(fromXY[0]), int(fromXY[1])), toXY)
        time.sleep(1)
        self.testDdeFileManagerExistOnDock()
        time.sleep(2)

    def testClickScreenCenter(self):
        rawinput.click(int(utils.resolution.width/2), int(utils.resolution.height/2))
        time.sleep(1)

    def suite():
        suite = unittest.TestSuite()
        suite.addTest(DockIconMenuRemove('testOpenRun'))
        suite.addTest(DockIconMenuRemove('testSelectMenuNewWindow'))
        suite.addTest(DockIconMenuRemove('testSelectMenuNewWindow'))
        suite.addTest(DockIconMenuRemove('testFileManagerExist'))
        suite.addTest(DockIconMenuRemove('testSelectMenuUnDock'))
        suite.addTest(DockIconMenuRemove('testSelectMenuCloseAll'))
        suite.addTest(DockIconMenuRemove('testExpectResult'))
        suite.addTest(DockIconMenuRemove('testDragIconToDock'))
        suite.addTest(DockIconMenuRemove('testClickScreenCenter'))

        # change display mode
        suite.addTest(DockIconMenuRemove('testExChangeDisplayMode'))

        suite.addTest(DockIconMenuRemove('testOpenRun'))
        suite.addTest(DockIconMenuRemove('testSelectMenuNewWindow'))
        suite.addTest(DockIconMenuRemove('testSelectMenuNewWindow'))
        suite.addTest(DockIconMenuRemove('testFileManagerExist'))
        suite.addTest(DockIconMenuRemove('testSelectMenuUnDock'))
        suite.addTest(DockIconMenuRemove('testSelectMenuCloseAll'))
        suite.addTest(DockIconMenuRemove('testExpectResult'))
        suite.addTest(DockIconMenuRemove('testDragIconToDock'))
        suite.addTest(DockIconMenuRemove('testClickScreenCenter'))

        return suite

    class MyTestResult(runner.MyTextTestResult):
        def addError(self, test, err):
            super(DockIconMenuRemove.MyTestResult, self).addError(test, err)
            global result
            result = result and False

        def addFailure(self, test, err):
            super(DockIconMenuRemove.MyTestResult, self).addFailure(test, err)
            global result
            result = result and False

if __name__ == "__main__":
    unittest.TextTestRunner(resultclass=DockIconMenuRemove.MyTestResult).run(DockIconMenuRemove.suite())
