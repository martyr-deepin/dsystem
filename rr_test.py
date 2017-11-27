#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import json
import gettext
import unittest
from lib import runTest
from optparse import OptionParser

from RRTestCase import Launcher_StartAllAPP
from RRTestCase import Launcher_SendToDesktop
from RRTestCase import Launcher_AddToDock
from RRTestCase import Launcher_AutoStart
from RRTestCase import Launcher_Uninstall

from RRTestCase import Dock_Exist
from RRTestCase import Dock_DefaultSetting
from RRTestCase import Dock_ChangeDisplay
from RRTestCase import Dock_ChangePosition
from RRTestCase import Dock_ChangeIconSize
from RRTestCase import Dock_ChangeHide
from RRTestCase import Dock_DragDockiconToDel

from RRTestCase import DCC_Click_SoundSlider
from RRTestCase import DCC_Click_LightSlider
from RRTestCase import DCC_ShowModules

from RRTestCase import Command_useradd
from RRTestCase import Command_userdel
from RRTestCase import Command_passwd
from RRTestCase import Command_pwd
from RRTestCase import Command_cd
from RRTestCase import Command_mkdir
from RRTestCase import Command_rmdir
from RRTestCase import Command_cp
from RRTestCase import Command_mv
from RRTestCase import Command_rm
from RRTestCase import Command_file
from RRTestCase import Command_find
from RRTestCase import Command_grep
from RRTestCase import Command_chown
from RRTestCase import Command_sort
from RRTestCase import Command_wc
from RRTestCase import Command_ifconfig
from RRTestCase import Command_ping
from RRTestCase import Command_ping_ip
from RRTestCase import Command_ping_local_ip
from RRTestCase import Command_netstat_i
from RRTestCase import Command_netstat_r
from RRTestCase import Command_telnet
from RRTestCase import Command_traceroute
from RRTestCase import Command_tar
from RRTestCase import Command_gzip
from RRTestCase import Command_gunzip
from RRTestCase import Command_kill
from RRTestCase import Command_ps
from RRTestCase import Command_vi
from RRTestCase import Command_man
from RRTestCase import Command_who
from RRTestCase import Command_whoami
from RRTestCase import Command_cal
from RRTestCase import Command_date
from RRTestCase import Command_more
from RRTestCase import Command_redirect
from RRTestCase import Command_pipe
from RRTestCase import Command_apt_get
from RRTestCase import Command_apt_cache

from RRTestCase import DFM_OpenFile
from RRTestCase import DFM_OpenFileByApp
from RRTestCase import DFM_CompressFiles
from RRTestCase import DFM_DecompressFile
from RRTestCase import DFM_DecompressFileHere

from RRTestCase import DFM_RenameFile
from RRTestCase import DFM_DeleteFiles
from RRTestCase import DFM_MoveToTrash
from RRTestCase import DFM_RestoreFromTrash
from RRTestCase import DFM_PasteFile

from RRTestCase import DFM_NewFolder
from RRTestCase import DFM_NewFile
from RRTestCase import DFM_OpenFileLocation
from RRTestCase import DFM_CreateSymlink
from RRTestCase import DFM_FileShare

from RRTestCase import DFM_OpenInTerminal
from RRTestCase import DFM_OpenNewWindow

id_key = 'lava_id'
idfilename = 'id.txt'

def getIdList():
    if not os.path.exists(idfilename):
        return []

    f = open(idfilename)
    content = f.read()
    jsonstring = json.loads(content)
    return jsonstring[id_key]

def get_run_type():
    try:
        opt = OptionParser()
        opt.add_option('--run_all',
                        dest='run_type',
                        default=False,
                        help='the running type for the TestCases (bool: True or False) \
                        python3 rr_test.py --run_all True')
        opt.add_option('--run_dfm',
                        dest='run_dfm',
                        default=False,
                        help='running the TestCases of dde-file-manager (bool: True or False) python3 rr_test.py --run_dfm True')
        (options, args) = opt.parse_args()
        is_valid_paras = True
        error_messages = []
        run_type = options.run_type
        run_dfm = options.run_dfm

        opt.print_help()

        if is_valid_paras:
            user_paras = {"run_type": run_type, "run_dfm": run_dfm}
            return user_paras
    except Exception as ex:
        print("exception :{0".format(str(ex)))
        return None

def main():
    allids = getIdList()

    classes = []

    runtype = get_run_type()
    run_all = runtype['run_type']
    print('run_all =', run_all)
    run_dfm = runtype['run_dfm']
    print('run_dfm =', run_dfm)


    # Launcher
    if run_all or Launcher_StartAllAPP.caseid in allids:
        classes.append(Launcher_StartAllAPP)

    if run_all or Launcher_SendToDesktop.caseid in allids:
        classes.append(Launcher_SendToDesktop)

    if run_all or Launcher_AddToDock.caseid in allids:
        classes.append(Launcher_AddToDock)

    if run_all or Launcher_AutoStart.caseid in allids:
        classes.append(Launcher_AutoStart)

    if run_all or Launcher_Uninstall.caseid in allids:
        classes.append(Launcher_Uninstall)

    # Dock
    if run_all or Dock_Exist.caseid in allids:
        classes.append(Dock_Exist)

    if run_all or Dock_DefaultSetting.caseid in allids:
        classes.append(Dock_DefaultSetting)

    if run_all or Dock_ChangeDisplay.caseid in allids:
        classes.append(Dock_ChangeDisplay)

    if run_all or Dock_ChangePosition.caseid in allids:
        classes.append(Dock_ChangePosition)

    if run_all or Dock_ChangeIconSize.caseid in allids:
        classes.append(Dock_ChangeIconSize)

    if run_all or Dock_ChangeHide.caseid in allids:
        classes.append(Dock_ChangeHide)

    if run_all or Dock_DragDockiconToDel.caseid in allids:
        classes.append(Dock_DragDockiconToDel)

    # Dde control center
    if run_all or DCC_Click_SoundSlider.caseid in allids:
        classes.append(DCC_Click_SoundSlider)

    if run_all or DCC_Click_LightSlider.caseid in allids:
        classes.append(DCC_Click_LightSlider)

    if run_all or DCC_ShowModules.caseid in allids:
        classes.append(DCC_ShowModules)

    # Command
    if run_all or Command_useradd.caseid in allids:
        classes.append(Command_useradd)

    if run_all or Command_userdel.caseid in allids:
        classes.append(Command_userdel)

    if run_all or Command_passwd.caseid in allids:
        classes.append(Command_passwd)

    if run_all or Command_pwd.caseid in allids:
        classes.append(Command_pwd)

    if run_all or Command_cd.caseid in allids:
        classes.append(Command_cd)

    if run_all or Command_mkdir.caseid in allids:
        classes.append(Command_mkdir)

    if run_all or Command_rmdir.caseid in allids:
        classes.append(Command_rmdir)

    if run_all or Command_cp.caseid in allids:
        classes.append(Command_cp)

    if run_all or Command_mv.caseid in allids:
        classes.append(Command_mv)

    if run_all or Command_rm.caseid in allids:
        classes.append(Command_rm)

    if run_all or Command_file.caseid in allids:
        classes.append(Command_file)

    if run_all or Command_find.caseid in allids:
        classes.append(Command_find)

    if run_all or Command_grep.caseid in allids:
        classes.append(Command_grep)

    if run_all or Command_chown.caseid in allids:
        classes.append(Command_chown)

    if run_all or Command_sort.caseid in allids:
        classes.append(Command_sort)

    if run_all or Command_wc.caseid in allids:
        classes.append(Command_wc)

    if run_all or Command_ifconfig.caseid in allids:
        classes.append(Command_ifconfig)

    if run_all or Command_ping.caseid in allids:
        classes.append(Command_ping)

    if run_all or Command_ping_ip.caseid in allids:
        classes.append(Command_ping_ip)

    if run_all or Command_ping_local_ip.caseid in allids:
        classes.append(Command_ping_local_ip)

    if run_all or Command_netstat_i.caseid in allids:
        classes.append(Command_netstat_i)

    if run_all or Command_netstat_r.caseid in allids:
        classes.append(Command_netstat_r)

    if run_all or Command_telnet.caseid in allids:
        classes.append(Command_telnet)

    if run_all or Command_traceroute.caseid in allids:
        classes.append(Command_traceroute)

    if run_all or Command_tar.caseid in allids:
        classes.append(Command_tar)

    if run_all or Command_gzip.caseid in allids:
        classes.append(Command_gzip)

    if run_all or Command_gunzip.caseid in allids:
        classes.append(Command_gunzip)

    if run_all or Command_kill.caseid in allids:
        classes.append(Command_kill)

    if run_all or Command_ps.caseid in allids:
        classes.append(Command_ps)

    if run_all or Command_vi.caseid in allids:
        classes.append(Command_vi)

    if run_all or Command_man.caseid in allids:
        classes.append(Command_man)

    if run_all or Command_who.caseid in allids:
        classes.append(Command_who)

    if run_all or Command_whoami.caseid in allids:
        classes.append(Command_whoami)

    if run_all or Command_cal.caseid in allids:
        classes.append(Command_cal)

    if run_all or Command_date.caseid in allids:
        classes.append(Command_date)

    if run_all or Command_more.caseid in allids:
        classes.append(Command_more)

    if run_all or Command_redirect.caseid in allids:
        classes.append(Command_redirect)

    if run_all or Command_pipe.caseid in allids:
        classes.append(Command_pipe)

    if run_all or Command_apt_get.caseid in allids:
        classes.append(Command_apt_get)

    if run_all or Command_apt_cache.caseid in allids:
        classes.append(Command_apt_cache)

    #dde-file-manager

    if run_all or run_dfm or DFM_OpenFile.caseid in allids:
        classes.append(DFM_OpenFile)

    if run_all or run_dfm or DFM_OpenFileByApp.caseid in allids:
        classes.append(DFM_OpenFileByApp)

    if run_all or run_dfm or DFM_CompressFiles.caseid in allids:
        classes.append(DFM_CompressFiles)

    if run_all or run_dfm or DFM_DecompressFile.caseid in allids:
        classes.append(DFM_DecompressFile)

    if run_all or run_dfm or DFM_DecompressFileHere.caseid in allids:
        classes.append(DFM_DecompressFileHere)

    if run_all or run_dfm or DFM_RenameFile.caseid in allids:
        classes.append(DFM_RenameFile)

    if run_all or run_dfm or DFM_DeleteFiles.caseid in allids:
        classes.append(DFM_DeleteFiles)

    if run_all or run_dfm or DFM_MoveToTrash.caseid in allids:
        classes.append(DFM_MoveToTrash)

    if run_all or run_dfm or DFM_RestoreFromTrash.caseid in allids:
        classes.append(DFM_RestoreFromTrash)

    if run_all or run_dfm or DFM_PasteFile.caseid in allids:
        classes.append(DFM_PasteFile)

    if run_all or run_dfm or DFM_NewFolder.caseid in allids:
        classes.append(DFM_NewFolder)

    if run_all or run_dfm or DFM_NewFile.caseid in allids:
        classes.append(DFM_NewFile)

    if run_all or run_dfm or DFM_OpenFileLocation.caseid in allids:
        classes.append(DFM_OpenFileLocation)

    if run_all or run_dfm or DFM_CreateSymlink.caseid in allids:
        classes.append(DFM_CreateSymlink)

    if run_all or run_dfm or DFM_FileShare.caseid in allids:
        classes.append(DFM_FileShare)

    if run_all or run_dfm or DFM_OpenInTerminal.caseid in allids:
        classes.append(DFM_OpenInTerminal)

    if run_all or run_dfm or DFM_OpenNewWindow.caseid in allids:
        classes.append(DFM_OpenNewWindow)

    if 0 == len(classes):
        print("classes length is 0.\nExit")
        sys.exit()

    for c in classes:
        runTest(c)

if __name__ == "__main__":
    unittest.installHandler()
    LOCALE_DIR = os.path.abspath("./lib/locale")
    gettext.install('dsystem', LOCALE_DIR)
    main()
