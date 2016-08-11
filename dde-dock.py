#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
import os

import ddedock.testFashionDefaultIcons
import ddedock.testEfficientDefaultIcons
import ddedock.testFashionIconsPopup
import ddedock.testEfficientIconsPopup
import ddedock.testFashionFunction
import ddedock.testEfficientFunction
import ddedock.testFashionExistLeft
import ddedock.testFashionExistRight
import ddedock.testFashionDockSize
import ddedock.testEfficientDockSize
import ddedock.testOtherDirectionDockSize
import ddedock.testDockKeepShown
import ddedock.testDockKeepHidden
import ddedock.testDockSmartHide
import ddedock.testDockKeepShownOtherDirection
import ddedock.testDockKeepHiddenOtherDirection
import ddedock.testDockSmartHideOtherDirection
import ddedock.testDockMenu

def main():
    suite00 = ddedock.testFashionDefaultIcons.suite()
    suite01 = ddedock.testEfficientDefaultIcons.suite()
    suite02 = ddedock.testFashionIconsPopup.suite()
    suite03 = ddedock.testEfficientIconsPopup.suite()
    suite1 = ddedock.testFashionFunction.suite()
    suite2 = ddedock.testEfficientFunction.suite()
    suite3 = ddedock.testFashionExistLeft.suite()
    suite4 = ddedock.testFashionExistRight.suite()
    suite5 = ddedock.testFashionDockSize.suite()
    suite6 = ddedock.testEfficientDockSize.suite()
    suite7 = ddedock.testOtherDirectionDockSize.suite()
    suite8 = ddedock.testDockKeepShown.suite()
    suite9 = ddedock.testDockKeepHidden.suite()
    suite10 = ddedock.testDockSmartHide.suite()
    suite11 = ddedock.testDockKeepShownOtherDirection.suite()
    suite12 = ddedock.testDockKeepHiddenOtherDirection.suite()
    suite13 = ddedock.testDockSmartHideOtherDirection.suite()
    suite14 = ddedock.testDockMenu.suite()

    alltests = unittest.TestSuite((suite00, suite01, suite02, suite03,
                                   suite1, suite2, suite3, suite4,
                                   suite5, suite6, suite7, suite8,
                                   suite9, suite10, suite11, suite12,
                                   suite13, suite14))

    runner = unittest.TextTestRunner()
    runner.run(alltests)

if __name__ == "__main__":
    main()
