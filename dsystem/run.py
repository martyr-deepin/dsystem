#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
import json
from tools.get_testcase_id import getCaseId
from tools.upload_result import reportTCResult

import ddedock.testFashionFunction

idfile = "id.txt"
resultfile = "result.txt"

def getIdFile():
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
    result = getCaseId(idfile)
    if result == False:
        print("Run: Can't get the case id")

    idlist = getIdFile()

    if idlist == None or type(idlist) != list or len(idlist) == 0:
        print("Can't get the idlist in file %s." % idfile)
        exit(1)

    allsuite = []

    # add ddedock suite
    if ddedock.testFashionFunction.caseid in idlist:
        allsuite.append(ddedock.testFashionFunction.suite())

    if len(allsuite) == 0:
        print("Suite list is zero.")
        print("Exit.")
        exit(1)

    alltest = unittest.TestSuite(tuple(allsuite))
    runner = unittest.TextTestRunner()
    runner.run(alltest)

    reportTCResult(resultfile)

if __name__ == "__main__":
    main()


