#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest

import dde_launcher.testAdjustFirstApp
import dde_launcher.testDisableDragInCategory
import dde_launcher.testDragAppToDock
import dde_launcher.testDragToCenter
import dde_launcher.testStartup
import dde_launcher.testAddToDock
import dde_launcher.testRemoveFromDock
import dde_launcher.testSendToDesktop
import dde_launcher.testRemoveFromDock
import dde_launcher.testBoot
import dde_launcher.testChineseSearch
import dde_launcher.testEnglishSearch
import dde_launcher.testPinyinSearch
import dde_launcher.testMutiSearch
import dde_launcher.testPkgNameSearch
import dde_launcher.testPunctuationSearch
import dde_launcher.testSpaceSearch
import dde_launcher.testSortApp

def main():
    suite1 = dde_launcher.testAdjustFirstApp.suite()
    suite2 = dde_launcher.testDisableDragInCategory.suite()
    suite3 = dde_launcher.testDragAppToDock.suite()
    suite4 = dde_launcher.testDragToCenter.suite()
    suite5 = dde_launcher.testStartup.suite()
    suite6 = dde_launcher.testAddToDock.suite()
    suite7 = dde_launcher.testRemoveFromDock.suite()
    suite8 = dde_launcher.testSendToDesktop.suite()
    suite9 = dde_launcher.testRemoveFromDock.suite()
    suite10 = dde_launcher.testBoot.suite()
    suite11 = dde_launcher.testChineseSearch.suite()
    suite12 = dde_launcher.testEnglishSearch.suite()
    suite13 = dde_launcher.testPinyinSearch.suite()
    suite14 = dde_launcher.testMutiSearch.suite()
    suite15 = dde_launcher.testPkgNameSearch.suite()
    suite16 = dde_launcher.testPunctuationSearch.suite()
    suite17 = dde_launcher.testSpaceSearch.suite()
    suite18 = dde_launcher.testSortApp.suite()

    alltests = unittest.TestSuite((suite1, suite2, suite3, suite4, suite5, suite6, suite7, suite8, suite9, suite10,
                                    suite11, suite12, suite13, suite14, suite15, suite16, suite17, suite18))

    runner = unittest.TextTestRunner()
    runner.run(alltests)
    
if __name__ == '__main__':
    main()
