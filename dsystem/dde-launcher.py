#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from lib.executeTestCase import runTest
import importlib
import os 
import re
from lib import utils
from lava_run import getIdFile

'''
def getIdFile():
    return ["2","45362"]
'''

def getClass(file):
    with open(file, 'r') as f:
        for line in f.readlines():
            match = re.match('class (.*)\(unittest.TestCase',line)
            if match:
                return match.group(1)
    raise Exception(file +' has no class ')


    
def main():
    idlist = getIdFile()
    print(idlist)
    classes = []
    casedirs = ["dde_launcher"]
    for casedir in casedirs:
       allfiles = os.listdir(casedir)
       test_files = list(filter(lambda e : e.startswith("test"),allfiles))
       for f in test_files:
            module = importlib.import_module(casedir+"."+f[:-3])
            class_name = getClass(casedir+"/"+f)
            testClass = getattr(module, class_name)
            if hasattr(module,"caseid"):
                testClass.caseid = getattr(module, "caseid")
            classes.append(testClass)

    classes = list(filter(lambda e:e.caseid in idlist, classes))
    for c in classes:
        runTest(c.suite())
if __name__ == '__main__':
    main()
