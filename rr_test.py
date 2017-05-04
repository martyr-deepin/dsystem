#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import json
import gettext
import unittest
from lib import runTest

from RRTestCase import Launcher_StartAllAPP
from RRTestCase import Launcher_SendToDesktop
from RRTestCase import Launcher_AddToDock
from RRTestCase import Launcher_AutoStart

from RRTestCase import Dock_DragDockiconToDel

from RRTestCase import DCC_Click_SoundSlider
from RRTestCase import DCC_Click_LightSlider

id_key = 'lava_id'
idfilename = 'id.txt'

def getIdList():
    f = open(idfilename)
    content = f.read()
    jsonstring = json.loads(content)
    return jsonstring[id_key]

def main():
    allids = getIdList()

    classes = []

    if Launcher_StartAllAPP.caseid in allids:
        classes.append(Launcher_StartAllAPP)

    if Launcher_SendToDesktop.caseid in allids:
        classes.append(Launcher_SendToDesktop)

    if Launcher_AddToDock.caseid in allids:
        classes.append(Launcher_AddToDock)

    if Launcher_AutoStart.caseid in allids:
        classes.append(Launcher_AutoStart)

    if Dock_DragDockiconToDel.caseid in allids:
        classes.append(Dock_DragDockiconToDel)

    if Click_SoundSlider.caseid in allids:
        classes.append(DCC_Click_SoundSlider)

    if Click_LightSlider.caseid in allids:
        classes.append(DCC_Click_LightSlider)

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
