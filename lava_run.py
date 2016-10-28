#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
import json
import os

idfile = "id.txt"
resultfile = "result.txt"

from ddedock import testFashionExistLeft

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
    if testFashionExistLeft.caseid in idlist:
        allclasses.append(testFashionExistLeft.FashionExistLeft)

    if len(allclasses) == 0:
        print("All classes list is zero.")
        print("Exit.")
        exit(1)

    for c in allclasses:
        suite = c.suite()
        unittest.TextTestRunner(resultclass=c.MyTestResult).run(suite)

if __name__ == "__main__":
    main()
