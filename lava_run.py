#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
import json
import os
from unittest import TestCase
from lib.executeTestCase import runTest
from importlib import import_module

casedirs=["ddedock","dde_launcher","apps","systemcommand","osd","collectedBugs"]
idfile = "id.txt"

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

def getClass(f):
    all_attrs = [getattr(f,c) for c in dir(f)]
    class_attr = [all_attr for all_attr in all_attrs if hasattr(all_attr,"__bases__") and TestCase in all_attr.__bases__]
    noIdClass = [cla for cla in class_attr if not hasattr(cla,"caseid")]
    for ncla in noIdClass:
        ncla.caseid = f.caseid
    return class_attr

def getAllClass():
    allmodules = [d+"."+f[:-3] for d in casedirs for f in os.listdir(d) if  f.startswith("test")]
    classes = [getClass(import_module(f)) for f in allmodules]
    return [c  for x in classes for c in x  if  c.caseid in getIdFile()]

if __name__ == "__main__":
    for c in getAllClass():
        runTest(c)
