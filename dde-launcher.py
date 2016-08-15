#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest

import dde_launcher.testAdjustFirstApp
import dde_launcher.testDisableDragInCategory
import dde_launcher.testDragAppToDock
import dde_launcher.testDragToCenter
import dde_launcher.testStartup

def main():
    suite1 = dde_launcher.testAdjustFirstApp.suite()
    suite2 = dde_launcher.testDisableDragInCategory.suite()
    suite3 = dde_launcher.testDragAppToDock.suite()
    suite4 = dde_launcher.testDragToCenter.suite()
    suite5 = dde_launcher.testStartup.suite()

    alltests = unittest.TestSuite((suite1, suite2, suite3, suite4, suite5))

    runner = unittest.TextTestRunner()
    runner.run(alltests)
    
if __name__ == '__main__':
    main()
