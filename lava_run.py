#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
import json
import os

idfile = "id.txt"
resultfile = "result.txt"

from ddedock import testFashionFunction
from ddedock import testEfficientFunction
from ddedock import testFashionExistLeft
from ddedock import testFashionExistRight
from ddedock import testOtherDirectionDockSize
from ddedock import testDockKeepShown
from ddedock import testDockKeepHidden
from ddedock import testDockSmartHide
from ddedock import testDockKeepShownOtherDirection
from ddedock import testDockKeepHiddenOtherDirection
from ddedock import testDockSmartHideOtherDirection
from ddedock import testDockMenu
from ddedock import testDockFashionMode
from ddedock import testDockEfficientMode

from ddedock import testFashionDockSize
from ddedock import testEfficientDockSize
from ddedock import testFashionDockSizeLarge
from ddedock import testFashionDockSizeMedium
from ddedock import testFashionDockSizeSmall
from ddedock import testEfficientDockSizeLarge
from ddedock import testEfficientDockSizeMedium
from ddedock import testEfficientDockSizeSmall
from ddedock import testDockSizeLargeOtherDirection
from ddedock import testDockSizeMediumOtherDirection
from ddedock import testDockSizeSmallOtherDirection

from ddedock import testGedit
from ddedock import testDeepinScreenshot
from ddedock import testGoogleChrome

from ddedock import testDockIconMenuName
from ddedock import testDockIconMenuMultiClose
from ddedock import testDockIconMenu
from ddedock import testDockIconMenuRemove

from ddedock import testHideDisplayApp
from ddedock import testDockMenuRU

from ddedock import testDockMenuRun
from ddedock import testDockMenuUnDock

from ddedock import testFashionIconsPopup
from ddedock import testEfficientIconsPopup

from ddedock import testDockSoundPluginClick

def getIdFile():
    if os.path.exists("/tmp/%s" % idfile):
        with open("/tmp/%s" % idfile, 'r') as f:
            idstr = f.read()
            print(idstr)
            idlist = idstr.strip('\n').split(',')
            return idlist

    try:
        f = open(idfile, "r")
        content = f.read()
        idcontent = json.loads(content, "UTF-8")
    except:
        print("Open file %s failed." % idfile)
        return None

    idlist = idcontent["test_id"]
    return idlist

def main():
    idlist = getIdFile()
    print(idlist)

    if idlist == None or type(idlist) != list or len(idlist) == 0:
        print("Can't get the idlist in file %s." % idfile)
        exit(1)

    allclasses = []

    # add ddedock classes
    if testFashionFunction.caseid in idlist:
        allclasses.append(testFashionFunction.FashionFunction)

    if testEfficientFunction.caseid in idlist:
        allclasses.append(testEfficientFunction.EfficientFunction)

    if testFashionExistLeft.caseid in idlist:
        allclasses.append(testFashionExistLeft.FashionExistLeft)

    if testFashionExistRight.caseid in idlist:
        allclasses.append(testFashionExistRight.FashionExistRight)

    if testOtherDirectionDockSize.caseid in idlist:
        allclasses.append(testOtherDirectionDockSize.OtherDirectionDockSize)

    if testDockKeepShown.caseid in idlist:
        allclasses.append(testDockKeepShown.DockKeepShown)

    if testDockKeepHidden.caseid in idlist:
        allclasses.append(testDockKeepHidden.DockKeepHidden)

    if testDockSmartHide.caseid in idlist:
        allclasses.append(testDockSmartHide.DockSmartHide)

    if testDockKeepShownOtherDirection.caseid in idlist:
        allclasses.append(testDockKeepShownOtherDirection.DockKeepShownOtherDirection)

    if testDockKeepHiddenOtherDirection.caseid in idlist:
        allclasses.append(testDockKeepHiddenOtherDirection.DockKeepHiddenOtherDirection)

    if testDockSmartHideOtherDirection.caseid in idlist:
        allclasses.append(testDockSmartHideOtherDirection.DockSmartHideOtherDirection)

    if testDockMenu.caseid in idlist:
        allclasses.append(testDockMenu.DockMenu)

    if testDockFashionMode.caseid in idlist:
        allclasses.append(testDockFashionMode.DockFashionMode)

    if testDockEfficientMode.caseid in idlist:
        allclasses.append(testDockEfficientMode.DockEfficientMode)

    if testFashionDockSize.caseid in idlist:
        allclasses.append(testFashionDockSize.FashionDockSize)

    if testEfficientDockSize.caseid in idlist:
        allclasses.append(testEfficientDockSize.EfficientDockSize)

    if testFashionDockSizeLarge.caseid in idlist:
        allclasses.append(testFashionDockSizeLarge.FashionDockSizeLarge)

    if testFashionDockSizeMedium.caseid in idlist:
        allclasses.append(testFashionDockSizeMedium.FashionDockSizeMedium)

    if testFashionDockSizeSmall.caseid in idlist:
        allclasses.append(testFashionDockSizeSmall.FashionDockSizeSmall)

    if testEfficientDockSizeLarge.caseid in idlist:
        allclasses.append(testEfficientDockSizeLarge.EfficientDockSizeLarge)

    if testEfficientDockSizeMedium.caseid in idlist:
        allclasses.append(testEfficientDockSizeMedium.EfficientDockSizeMedium)

    if testEfficientDockSizeSmall.caseid in idlist:
        allclasses.append(testEfficientDockSizeSmall.EfficientDockSizeSmall)

    if testDockSizeLargeOtherDirection.caseid in idlist:
        allclasses.append(testDockSizeLargeOtherDirection.DockSizeLargeOtherDirection)

    if testDockSizeMediumOtherDirection.caseid in idlist:
        allclasses.append(testDockSizeMediumOtherDirection.DockSizeMediumOtherDirection)

    if testDockSizeSmallOtherDirection.caseid in idlist:
        allclasses.append(testDockSizeSmallOtherDirection.DockSizeSmallOtherDirection)

    if testGedit.caseid in idlist:
        allclasses.append(testGedit.Gedit)

    if testDeepinScreenshot.caseid in idlist:
        allclasses.append(testDeepinScreenshot.DeepinScreenshot)

    if testGoogleChrome.caseid in idlist:
        allclasses.append(testGoogleChrome.GoogleChrome)

    if testDockIconMenuName.caseid in idlist:
        allclasses.append(testDockIconMenuName.DockIconMenuName)

    if testDockIconMenuMultiClose.caseid in idlist:
        allclasses.append(testDockIconMenuMultiClose.DockIconMenuMultiClose)

    if testDockIconMenu.caseid in idlist:
        allclasses.append(testDockIconMenu.DockIconMenu)

    if testDockIconMenuRemove.caseid in idlist:
        allclasses.append(testDockIconMenuRemove.DockIconMenuRemove)

    if testHideDisplayApp.caseid in idlist:
        allclasses.append(testHideDisplayApp.HideDisplayApp)

    if testDockMenuRU.caseid in idlist:
        allclasses.append(testDockMenuRU.DockMenuRU)

    if testDockMenuRun.caseid in idlist:
        allclasses.append(testDockMenuRun.DockMenuRun)

    if testDockMenuUnDock.caseid in idlist:
        allclasses.append(testDockMenuUnDock.DockMenuUnDock)

    if testFashionIconsPopup.caseid in idlist:
        allclasses.append(testFashionIconsPopup.FashionIconsPopup)

    if testEfficientIconsPopup.caseid in idlist:
        allclasses.append(testEfficientIconsPopup.EfficientIconsPopup)

    if testDockSoundPluginClick.caseid in idlist:
        allclasses.append(testDockSoundPluginClick.DockSoundPluginClick)

    if len(allclasses) == 0:
        print("All classes list is zero.")
        print("Exit.")
        exit(1)

    for c in allclasses:
        suite = c.suite()
        unittest.TextTestRunner(resultclass=c.MyTestResult).run(suite)

if __name__ == "__main__":
    main()
