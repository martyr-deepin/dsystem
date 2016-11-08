#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
import time
from lib import utils
from lib import runner
from dogtail.tree import root
from dogtail import rawinput

result = True
caseid = '33447'
casename = "all-442:第一项菜单"

class DockIconMenuName(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.startTime = time.time()
        cls.filemanagericonname = "深度文件管理器"
        cls.filemanagerwindowname = "深度文件管理器"
        cls.ddedockobject = utils.getDdeDockObject()

        if utils.dock.displaymode_fashion != utils.getDdeDockDisplayMode():
            utils.setDdeDockDisplayMode(utils.dock.displaymode_fashion)

        if utils.dock.position_bottom != utils.getDdeDockPosition():
            utils.setDdeDockPosition(utils.dock.position_bottom)

    @classmethod
    def tearDownClass(cls):
        seconds = %.3f % (time.time() - cls.startTime)
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

    def testSelectMenuName(self):
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

    def testFileManagerExist(self):
        filemanagerwin = utils.findWindow(self.filemanagerwindowname)
        self.assertTrue(None != filemanagerwin)

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
        filemanagerwin = utils.WindowState(self.filemanagerwindowname)
        state = filemanagerwin.is_minimized()
        self.assertFalse(state)

    def clickScreenCenter(self):
        rawinput.click(int(utils.resolution.width/2), int(utils.resolution.height/2))
        time.sleep(1)

    def testExChangeDisplayMode(self):
        if utils.getDdeDockDisplayMode() == utils.dock.displaymode_fashion:
            utils.setDdeDockDisplayMode(utils.dock.displaymode_efficient)
        elif utils.getDdeDockDisplayMode() == utils.dock.displaymode_efficient:
            utils.setDdeDockDisplayMode(utils.dock.displaymode_fashion)

    def suite():
        suite = unittest.TestSuite()
        suite.addTest(DockIconMenuName('testOpenRun'))
        suite.addTest(DockIconMenuName('testFileManagerExist'))
        suite.addTest(DockIconMenuName('minimizeWin'))
        suite.addTest(DockIconMenuName('testSelectMenuName'))
        suite.addTest(DockIconMenuName('testExpectResult'))
        suite.addTest(DockIconMenuName('testCloseFileManager'))

        # change display mode
        suite.addTest(DockIconMenuName('testExChangeDisplayMode'))

        suite.addTest(DockIconMenuName('testOpenRun'))
        suite.addTest(DockIconMenuName('testFileManagerExist'))
        suite.addTest(DockIconMenuName('minimizeWin'))
        suite.addTest(DockIconMenuName('testSelectMenuName'))
        suite.addTest(DockIconMenuName('testExpectResult'))
        suite.addTest(DockIconMenuName('testCloseFileManager'))


        return suite

    class MyTestResult(runner.MyTextTestResult):
        def addError(self, test, err):
            super(DockIconMenuName.MyTestResult, self).addError(test, err)
            global result
            result = result and False

        def addFailure(self, test, err):
            super(DockIconMenuName.MyTestResult, self).addFailure(test, err)
            global result
            result = result and False

if __name__ == "__main__":
    unittest.TextTestRunner(resultclass=DockIconMenuName.MyTestResult).run(DockIconMenuName.suite())
