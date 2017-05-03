#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import json
import gettext
import unittest
from lib import runTest

from RRTestCase import Launcher_StartAllAPP

from RRTestCase import Dock_DragDockiconToDel

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

    if Dock_DragDockiconToDel.caseid in allids:
        classes.append(Dock_DragDockiconToDel)

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
