#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from lib import executeTestCase
import pyautogui
from lib import runner
from lib import utils

result = True
casename = 'all-725:键盘布局'
newlayout = 'ara;azerty'

class  KbLayout(unittest.TestCase):
    caseid = '34731'
    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass
    def setUp(self):
    	pass

    def tearDown(self):
        utils.delKeyboard(newlayout)

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

if __name__ == "__main__":
    executeTestCase.runTest(KbLayout)
