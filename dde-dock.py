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

from ddedock.testFashionDockSize import FashionDockSize
from ddedock.testEfficientDockSize import EfficientDockSize
from ddedock.testFashionDockSizeLarge import FashionDockSizeLarge
from ddedock.testFashionDockSizeMedium import FashionDockSizeMedium
from ddedock.testFashionDockSizeSmall import FashionDockSizeSmall
from ddedock.testEfficientDockSizeLarge import EfficientDockSizeLarge
from ddedock.testEfficientDockSizeMedium import EfficientDockSizeMedium
from ddedock.testEfficientDockSizeSmall import EfficientDockSizeSmall
from ddedock.testDockSizeLargeOtherDirection import DockSizeLargeOtherDirection
from ddedock.testDockSizeMediumOtherDirection import DockSizeMediumOtherDirection
from ddedock.testDockSizeSmallOtherDirection import DockSizeSmallOtherDirection

from ddedock.testGedit import Gedit
from ddedock.testDeepinScreenshot import DeepinScreenshot

def main():
    # suite00 = ddedock.testFashionDefaultIcons.suite()
    # suite01 = ddedock.testEfficientDefaultIcons.suite()
    # suite02 = ddedock.testFashionIconsPopup.suite()
    # suite03 = ddedock.testEfficientIconsPopup.suite()

    classes = []

    # dde-dock
    classes.append(FashionFunction)
    classes.append(EfficientFunction)
    classes.append(FashionExistLeft)
    classes.append(FashionExistRight)
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

    classes.append(FashionDockSize)
    classes.append(EfficientDockSize)
    classes.append(FashionDockSizeLarge)
    classes.append(FashionDockSizeMedium)
    classes.append(FashionDockSizeSmall)
    classes.append(EfficientDockSizeLarge)
    classes.append(EfficientDockSizeMedium)
    classes.append(EfficientDockSizeSmall)
    classes.append(DockSizeLargeOtherDirection)
    classes.append(DockSizeMediumOtherDirection)
    classes.append(DockSizeSmallOtherDirection)

    classes.append(Gedit)
    classes.append(DeepinScreenshot)

    for c in classes:
        suite = c.suite()
        unittest.TextTestRunner(resultclass=c.MyTestResult).run(suite)

if __name__ == "__main__":
    main()
