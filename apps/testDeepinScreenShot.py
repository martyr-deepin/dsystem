#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import unittest
from lib import runner,utils
from lib.launcher import *
from lib.dde_dock import *
from fnmatch import fnmatch
from glob import glob

result = True
homePath = os.path.expanduser('~')

class DeepinScreenshot(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.caseid = '83352'
        cls.casename = 'all-3353:启动与截图保存'
        cls.appName = 'deepin-screenshot'
        cls.cmd = "ps aux |grep /usr/bin/deepin-screenshot |grep -v grep |awk '{print $12}'"

    @classmethod
    def tearDownClass(cls):
        global result
        utils.commitresult(cls.caseid, result)
        pngfiles = glob(homePath + '/Desktop/深度截图*.png')
        for pngfile in pngfiles:
            os.remove(pngfile)
        

    def testDeepinScreenshot1(self):
        subprocess.check_call(self.appName + ' &', shell=True)
        sleep(2)
        pyautogui.press('esc')

    def testDeepinScreenshot2(self):
        launcher.searchApp(self.appName)
        sleep(1)
        pyautogui.press('enter')

    def testSaveScreenshot(self):
        size = pyautogui.size()
        s = size[0]/2, size[1]/2
        d = size[0]/2+300, size[1]/2+200
        sleep(2)
        mouseDrag(s, d)
        pyautogui.press('enter')
        pngfiles = [name for name in os.listdir(homePath + '/Desktop') if fnmatch(name, '深度截图*.png')]
        self.assertGreater(len(pngfiles),0)

    def suite():
        suite = unittest.TestSuite()
        suite.addTest(DeepinScreenshot('testDeepinScreenshot1'))
        suite.addTest(DeepinScreenshot('testDeepinScreenshot2'))
        suite.addTest(DeepinScreenshot('testSaveScreenshot'))
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