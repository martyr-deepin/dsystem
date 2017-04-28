#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import json
import gettext
import unittest
from lib import runTest

from dde_control_center import User_Head

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

    if User_Head.caseid in allids:
        classes.append(User_Head)

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
