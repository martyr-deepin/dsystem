#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
import json
import os

idfile = "id.txt"
resultfile = "result.txt"

# dde-dock
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

from dde_launcher import testAdjustFirstApp
from dde_launcher import testDisableDragInCategory

# dde launcher
from dde_launcher import testAdjustFirstApp
from dde_launcher import testDisableDragInCategory
from dde_launcher import testDragAppToDock
from dde_launcher import testDragToCenter
from dde_launcher import testStartup
from dde_launcher import testAddToDock
from dde_launcher import testRemoveFromDock
from dde_launcher import testSendToDesktop
from dde_launcher import testRemoveFromDesktop
from dde_launcher import testBoot
from dde_launcher import testChineseSearch
from dde_launcher import testEnglishSearch
from dde_launcher import testPinyinSearch
from dde_launcher import testMutiSearch
from dde_launcher import testPkgNameSearch
from dde_launcher import testPunctuationSearch
from dde_launcher import testSpaceSearch
from dde_launcher import testSortApp
from dde_launcher import testUninstall
#from dde_launcher import testShotcuts
from dde_launcher import testEnterKey
from dde_launcher import testEscKey
from dde_launcher import testHideByClickDock
from dde_launcher import testClickBlank
from dde_launcher import testBluePoint
from dde_launcher import testAppDelete1
from dde_launcher import testAppDelete2
from dde_launcher import testSortWithSearch
from dde_launcher import test_ctrl_c
from dde_launcher import test_ctrl_x
from dde_launcher import testStartupLauncher
from dde_launcher import testUninstallFailed
from dde_launcher import testUpdate_uninstall
from dde_launcher import testRebootLauncher

# system command
from systemcommand import test_useradd
from systemcommand import test_userdel
from systemcommand import test_passwd

from systemcommand import test_pwd
from systemcommand import test_cd
from systemcommand import test_mkdir
from systemcommand import test_rmdir
from systemcommand import test_cp
from systemcommand import test_mv
from systemcommand import test_rm
from systemcommand import test_file
from systemcommand import test_find
from systemcommand import test_grep
from systemcommand import test_chown
from systemcommand import test_sort
from systemcommand import test_wc

from systemcommand import test_ifconfig
from systemcommand import test_ping
from systemcommand import test_ping_ip
from systemcommand import test_ping_local_ip
from systemcommand import test_netstat_i
from systemcommand import test_netstat_r
from systemcommand import test_telnet
from systemcommand import test_traceroute

from systemcommand import test_tar
from systemcommand import test_gzip
from systemcommand import test_gunzip

from systemcommand import test_kill
from systemcommand import test_ps

from systemcommand import test_vi

from systemcommand import test_man
from systemcommand import test_who
from systemcommand import test_whoami
from systemcommand import test_cal
from systemcommand import test_date
from systemcommand import test_more
from systemcommand import test_redirect
from systemcommand import test_pipe

from systemcommand import test_apt_get
from systemcommand import test_apt_cache

# osd
from osd import test_keyboardlayout

# app
from apps import testDeepinMovie
from apps import testDeepinMusic
from apps import testDeepinScreenShot
from apps import testDeepinStore
from apps import testDeepinTerminal
from apps import testYoudaoDict
from apps import testDeepinMovieHelp

# bugs
from collectedBugs import testShowDesktop
from collectedBugs import testHP
from collectedBugs import testjournald
from collectedBugs import testyoudao
from collectedBugs import testcodename

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

    # 插件
    if testDockSoundPluginClick.caseid in idlist:
        allclasses.append(testDockSoundPluginClick.DockSoundPluginClick)

    # add dde launcher classes
    if testAdjustFirstApp.caseid in idlist:
        allclasses.append(testAdjustFirstApp.LauncherAdjustFirstApp)

    if testDisableDragInCategory.caseid in idlist:
        allclasses.append(testDisableDragInCategory.LauncherDisable)

    if testDragAppToDock.caseid in idlist:
        allclasses.append(testDragAppToDock.LauncherDragAppToDock)

    if testDragToCenter.caseid in idlist:
        allclasses.append(testDragToCenter.LauncherDragToCenter)

    if testStartup.caseid in idlist:
        allclasses.append(testStartup.LauncherStartupApp)

    if testAddToDock.caseid in idlist:
        allclasses.append(testAddToDock.LauncherAddToDock)

    if testRemoveFromDock.caseid in idlist:
        allclasses.append(testRemoveFromDock.LauncherRemoveFromDock)

    if testSendToDesktop.caseid in idlist:
        allclasses.append(testSendToDesktop.LauncherSendToDesktop)

    if testRemoveFromDesktop.caseid in idlist:
        allclasses.append(testRemoveFromDesktop.LauncherRemoveFromDesktop)

    if testBoot.caseid in idlist:
        allclasses.append(testBoot.LauncherAddToBoot)

    if testChineseSearch.caseid in idlist:
        allclasses.append(testChineseSearch.LauncherChineseSearch)

    if testEnglishSearch.caseid in idlist:
        allclasses.append(testEnglishSearch.LauncherEnglishSearch)

    if testPinyinSearch.caseid in idlist:
        allclasses.append(testPinyinSearch.LauncherPinyinSearch)

    if testMutiSearch.caseid in idlist:
        allclasses.append(testMutiSearch.LauncherMutiSearch)

    if testPkgNameSearch.caseid in idlist:
        allclasses.append(testPkgNameSearch.LauncherPkgNameSearch)

    if testPunctuationSearch.caseid in idlist:
        allclasses.append(testPunctuationSearch.LauncherPunctuationSearch)

    if testSpaceSearch.caseid in idlist:
        allclasses.append(testSpaceSearch.LauncherSpaceSearch)

    if testSortApp.caseid in idlist:
        allclasses.append(testSortApp.LauncherSortApp)

    if testUninstall.caseid in idlist:
        allclasses.append(testUninstall.LauncherUninstall)

    #if testShotcuts.caseid in idlist:
    #    allclasses.append(testShotcuts.LauncherShotcuts)

    if testEnterKey.caseid in idlist:
        allclasses.append(testEnterKey.LauncherEnterKey)

    if testEscKey.caseid in idlist:
        allclasses.append(testEscKey.LauncherEscKey)

    if testHideByClickDock.caseid in idlist:
        allclasses.append(testHideByClickDock.LauncherHideByClickDock)

    if testClickBlank.caseid in idlist:
        allclasses.append(testClickBlank.ClickBlank)

    if testBluePoint.caseid in idlist:
        allclasses.append(testBluePoint.BluePoint)

    if testAppDelete1.caseid in idlist:
        allclasses.append(testAppDelete1.AppDelete1)

    if testAppDelete2.caseid in idlist:
        allclasses.append(testAppDelete2.AppDelete2)

    if testSortWithSearch.caseid in idlist:
        allclasses.append(testSortWithSearch.LauncherSortWithSearch)

    if test_ctrl_c.caseid in idlist:
        allclasses.append(test_ctrl_c.LauncherShotcuts_ctrl_c)

    if test_ctrl_x.caseid in idlist:
        allclasses.append(test_ctrl_x.LauncherShotcuts_ctrl_x)

    if testStartupLauncher.caseid in idlist:
        allclasses.append(testStartupLauncher.LauncherStartup)

    if testUninstallFailed.caseid in idlist:
        allclasses.append(testUninstallFailed.LauncherUninstall)

    if testUpdate_uninstall.caseid in idlist:
        allclasses.append(testUpdate_uninstall.LauncherUpdateUninstall)

    if testRebootLauncher.caseid in idlist:
        allclasses.append(testRebootLauncher.LauncherReboot)

    # add system command classes
    if test_useradd.caseid in idlist:
        allclasses.append(test_useradd.Useradd)

    if test_userdel.caseid in idlist:
        allclasses.append(test_userdel.Userdel)

    if test_passwd.caseid in idlist:
        allclasses.append(test_passwd.Passwd)

    if test_pwd.caseid in idlist:
        allclasses.append(test_pwd.Pwd)

    if test_cd.caseid in idlist:
        allclasses.append(test_cd.Cd)

    if test_mkdir.caseid in idlist:
        allclasses.append(test_mkdir.Mkdir)

    if test_rmdir.caseid in idlist:
        allclasses.append(test_rmdir.Rmdir)

    if test_cp.caseid in idlist:
        allclasses.append(test_cp.Cp)

    if test_mv.caseid in idlist:
        allclasses.append(test_mv.Mv)

    if test_rm.caseid in idlist:
        allclasses.append(test_rm.Rm)

    if test_file.caseid in idlist:
        allclasses.append(test_file.File)

    if test_find.caseid in idlist:
        allclasses.append(test_find.Find)

    if test_grep.caseid in idlist:
        allclasses.append(test_grep.Grep)

    if test_chown.caseid in idlist:
        allclasses.append(test_chown.Chown)

    if test_sort.caseid in idlist:
        allclasses.append(test_sort.Sort)

    if test_wc.caseid in idlist:
        allclasses.append(test_wc.Wc)

    if test_ifconfig.caseid in idlist:
        allclasses.append(test_ifconfig.Ifconfig)

    if test_ping.caseid in idlist:
        allclasses.append(test_ping.Ping)

    if test_ping_ip.caseid in idlist:
        allclasses.append(test_ping_ip.Ping_ip)

    if test_ping_local_ip.caseid in idlist:
        allclasses.append(test_ping_local_ip.Ping_local_ip)

    if test_netstat_i.caseid in idlist:
        allclasses.append(test_netstat_i.Netstat_i)

    if test_netstat_r.caseid in idlist:
        allclasses.append(test_netstat_r.Netstat_r)

    if test_telnet.caseid in idlist:
        allclasses.append(test_telnet.Telnet)

    if test_traceroute.caseid in idlist:
        allclasses.append(test_traceroute.Traceroute)

    if test_tar.caseid in idlist:
        allclasses.append(test_tar.Tar)

    if test_gzip.caseid in idlist:
        allclasses.append(test_gzip.Gzip)

    if test_gunzip.caseid in idlist:
        allclasses.append(test_gunzip.Gunzip)

    if test_kill.caseid in idlist:
        allclasses.append(test_kill.Kill)

    if test_ps.caseid in idlist:
        allclasses.append(test_ps.Ps)

    if test_vi.caseid in idlist:
        allclasses.append(test_vi.Vi)

    if test_man.caseid in idlist:
        allclasses.append(test_man.Man)

    if test_who.caseid in idlist:
        allclasses.append(test_who.Who)

    if test_whoami.caseid in idlist:
        allclasses.append(test_whoami.Whoami)

    if test_cal.caseid in idlist:
        allclasses.append(test_cal.Cal)

    if test_date.caseid in idlist:
        allclasses.append(test_date.Date)

    if test_more.caseid in idlist:
        allclasses.append(test_more.More)

    if test_redirect.caseid in idlist:
        allclasses.append(test_redirect.Redirect)

    if test_pipe.caseid in idlist:
        allclasses.append(test_pipe.Pipe)

    if test_apt_get.caseid in idlist:
        allclasses.append(test_apt_get.Apt_get)

    if test_apt_cache.caseid in idlist:
        allclasses.append(test_apt_cache.Apt_cache)

    # add osd classes
    if test_keyboardlayout.caseid in idlist:
        allclasses.append(test_keyboardlayout.KbLayout)

    # add app classes
    if testDeepinMovie.caseid in idlist:
        allclasses.append(testDeepinMovie.DeepinMovie)

    if testDeepinMusic.caseid in idlist:
        allclasses.append(testDeepinMusic.DeepinMusic)

    if testDeepinScreenShot.caseid in idlist:
        allclasses.append(testDeepinScreenShot.DeepinScreenShot)

    if testDeepinStore.caseid in idlist:
        allclasses.append(testDeepinStore.DeepinStore)

    if testDeepinTerminal.caseid in idlist:
        allclasses.append(testDeepinTerminal.DeepinTerminal)

    if testYoudaoDict.caseid in idlist:
        allclasses.append(testYoudaoDict.YoudaoDict)

    if testDeepinMovieHelp.caseid in idlist:
        allclasses.append(testDeepinMovieHelp.DeepinMovieHelp)

    # add bugs classes
    if testShowDesktop.caseid in idlist:
        allclasses.append(testShowDesktop.ShowDesktopBtn)

    if testHP.caseid in idlist:
        allclasses.append(testHP.HPIntergration)

    if testjournald.caseid in idlist:
        allclasses.append(testjournald.RestrictLog)

    if testyoudao.caseid in idlist:
        allclasses.append(testyoudao.Youdao)

    if testcodename.caseid in idlist:
        allclasses.append(testcodename.CodeName)

    if len(allclasses) == 0:
        print("All classes list is zero.")
        print("Exit.")
        exit(1)

    for c in allclasses:
        suite = c.suite()
        unittest.TextTestRunner(resultclass=c.MyTestResult).run(suite)

if __name__ == "__main__":
    main()
