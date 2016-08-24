#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
import os

# import ddedock.testFashionDefaultIcons
# import ddedock.testEfficientDefaultIcons
# import ddedock.testFashionIconsPopup
# import ddedock.testEfficientIconsPopup
from ddedock.testFashionFunction import FashionFunction
from ddedock.testEfficientFunction import EfficientFunction
from ddedock.testFashionExistLeft import FashionExistLeft
from ddedock.testFashionExistRight import FashionExistRight
from ddedock.testFashionDockSize import FashionDockSize
from ddedock.testEfficientDockSize import EfficientDockSize
from ddedock.testOtherDirectionDockSize import OtherDirectionDockSize
from ddedock.testDockKeepShown import DockKeepShown
from ddedock.testDockKeepHidden import DockKeepHidden
from ddedock.testDockSmartHide import DockSmartHide
from ddedock.testDockKeepShownOtherDirection import DockKeepShownOtherDirection
from ddedock.testDockKeepHiddenOtherDirection import DockKeepHiddenOtherDirection
from ddedock.testDockSmartHideOtherDirection import DockSmartHideOtherDirection
from ddedock.testDockMenu import DockMenu
from ddedock.testDockFashionMode import DockFashionMode
from ddedock.testDockEfficientMode import DockEfficientMode

def main():
    # suite00 = ddedock.testFashionDefaultIcons.suite()
    # suite01 = ddedock.testEfficientDefaultIcons.suite()
    # suite02 = ddedock.testFashionIconsPopup.suite()
    # suite03 = ddedock.testEfficientIconsPopup.suite()

    classes = []
    classes.append(FashionFunction)
    classes.append(EfficientFunction)
    classes.append(FashionExistLeft)
    classes.append(FashionExistRight)
    classes.append(FashionDockSize)
    classes.append(EfficientDockSize)
    classes.append(OtherDirectionDockSize)
    classes.append(DockKeepShown)
    classes.append(DockKeepHidden)
    classes.append(DockSmartHide)
    classes.append(DockKeepShownOtherDirection)
    classes.append(DockKeepHiddenOtherDirection)
    classes.append(DockSmartHideOtherDirection)
    classes.append(DockMenu)
    classes.append(DockFashionMode)
    classes.append(DockEfficientMode)

    for c in classes:
        suite = c.suite()
        unittest.TextTestRunner(resultclass=c.MyTestResult).run(suite)

if __name__ == "__main__":
    main()
