#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
import pyautogui
from lib import runner
from lib import utils

result = True
newlayout = 'ara;azerty'

class  KbLayout(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.caseid = '34731'
        cls.casename = 'all-725:键盘布局'

    @classmethod
    def tearDownClass(cls):
        global result,newlayout
        utils.commitresult(cls.caseid, result)
        utils.delKeyboard(newlayout)

    def setUp(self):
    	pass

    def tearDown(self):
    	pass

    def test_addlayout(self):
        global newlayout
        utils.addKeyboard(newlayout)

    def test_changelayout(self):
        global newlayout
        pyautogui.hotkey('winleft',' ')
        self.assertEqual('us;',utils.getCurrentLayout())
        pyautogui.keyUp(' ')
        pyautogui.hotkey('winleft',' ')
        self.assertEqual(newlayout,utils.getCurrentLayout())

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
