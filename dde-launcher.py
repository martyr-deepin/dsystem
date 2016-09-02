#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest

from dde_launcher.testAdjustFirstApp import LauncherAdjustFirstApp
from dde_launcher.testDisableDragInCategory import LauncherDisable
from dde_launcher.testDragAppToDock import LauncherDragAppToDock
from dde_launcher.testDragToCenter import LauncherDragToCenter
from dde_launcher.testStartup import LauncherStartupApp
from dde_launcher.testAddToDock import LauncherAddToDock
from dde_launcher.testRemoveFromDock import LauncherRemoveFromDock
from dde_launcher.testSendToDesktop import LauncherSendToDesktop
from dde_launcher.testRemoveFromDesktop import LauncherRemoveFromDesktop
from dde_launcher.testBoot import LauncherAddToBoot
from dde_launcher.testChineseSearch import LauncherChineseSearch
from dde_launcher.testEnglishSearch import LauncherEnglishSearch
from dde_launcher.testPinyinSearch import LauncherPinyinSearch
from dde_launcher.testMutiSearch import LauncherMutiSearch
from dde_launcher.testPkgNameSearch import LauncherPkgNameSearch
from dde_launcher.testPunctuationSearch import LauncherPunctuationSearch
from dde_launcher.testSpaceSearch import LauncherSpaceSearch
from dde_launcher.testSortApp import LauncherSortApp
from dde_launcher.testUninstall import LauncherUninstall
from dde_launcher.testShotcuts import LauncherShotcuts
from dde_launcher.testEnterKey import LauncherEnterKey
from dde_launcher.testEscKey import LauncherEscKey
from dde_launcher.testHideByClickDock import LauncherHideByClickDock


def main():
    classes = []
    classes.append(LauncherAdjustFirstApp)
    classes.append(LauncherDisable)
    classes.append(LauncherDragAppToDock)
    classes.append(LauncherDragToCenter)
    classes.append(LauncherStartupApp)
    classes.append(LauncherAddToDock)
    classes.append(LauncherRemoveFromDock)
    classes.append(LauncherSendToDesktop)
    classes.append(LauncherRemoveFromDesktop)
    classes.append(LauncherAddToBoot)
    #classes.append(LauncherChineseSearch)
    #classes.append(LauncherEnglishSearch)
    #classes.append(LauncherPinyinSearch)
    classes.append(LauncherMutiSearch)
    classes.append(LauncherPkgNameSearch)
    classes.append(LauncherPunctuationSearch)
    classes.append(LauncherSpaceSearch)
    classes.append(LauncherSortApp)
    classes.append(LauncherUninstall)
    classes.append(LauncherShotcuts)
    classes.append(LauncherEnterKey)
    classes.append(LauncherEscKey)
    classes.append(LauncherHideByClickDock)

    for c in classes:
        unittest.TextTestRunner(resultclass=c.MyTestResult).run(c.suite())
if __name__ == '__main__':
    main()
