#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
import time
import pyautogui
from lib import runner
from lib import utils

result = True
caseid = '34731'
casename = 'all-725:键盘布局'
newlayout = 'ara;azerty'

class  KbLayout(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.startTime = time.time()
        pass

    @classmethod
    def tearDownClass(cls):
        seconds = "%.3f" % (time.time() - cls.startTime)
        minutes = utils.convertToMinutes(float(seconds))
        global result,newlayout
        utils.commitresult(caseid, result, minutes)
        utils.delKeyboard(newlayout)

    def setUp(self):
    	pass

    def tearDown(self):
    	pass

    def test_addlayout(self):
        global newlayout
        self.assertEqual('us;',utils.getCurrentLayout())
        utils.addKeyboard(newlayout)

    def test_changelayout(self):
        global newlayout
        pyautogui.hotkey('winleft',' ')
        pyautogui.keyUp(' ')
        pyautogui.hotkey('winleft',' ')
        pyautogui.keyUp('winleft')
        self.assertEqual(newlayout,utils.getCurrentLayout())
        time.sleep(2)
        pyautogui.hotkey('winleft',' ')
        pyautogui.keyUp(' ')
        pyautogui.hotkey('winleft',' ')
        pyautogui.keyUp('winleft')
        time.sleep(2)

    def suite():
        suite = unittest.TestSuite()
        suite.addTest(KbLayout('test_addlayout'))
        suite.addTest(KbLayout('test_changelayout'))
        return suite

    class MyTestResult(runner.MyTextTestResult):
        def addError(self, test, err):
            super(KbLayout.MyTestResult, self).addError(test, err)
            global result
            result = result and False

        def addFailure(self, test, err):
            super(KbLayout.MyTestResult, self).addError(test, err)
            global result
            result = result and False

if __name__ == "__main__":
    unittest.TextTestRunner(resultclass=KbLayout.MyTestResult).run(KbLayout.suite())
