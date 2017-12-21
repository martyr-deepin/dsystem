#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import json
import xmlrpc.client

TESTPLANID = os.getenv("TESTPLAN_ID")
BUILDID = os.getenv("BUILD_ID")
USERID  = os.getenv("USER_ID")
SERVER_URL = os.getenv("SERVER_URL")
TESTLINKAPIKEY = os.getenv("TESTLINKAPIKEY")

def printline():
    print('-' * 80)

if TESTPLANID == None or BUILDID == None or SERVER_URL == None or TESTLINKAPIKEY == None:
    print("Please make sure you have export the parameters.")
    exit(1)

idfilename = "id.txt"

class TestlinkAPIClient:
    def __init__(self, devKey):
        self.server = xmlrpc.client.ServerProxy(SERVER_URL)
        self.devKey = devKey

    def getInfo(self):
        return self.server.tl.about()

    def getProjects(self):
        return self.server.tl.getProjects(dict(devKey=self.devKey))

    def getPlaninfo(self, dictargs):
        dictargs["devKey"] = self.devKey
        return self.server.tl.getTestPlanByName(dictargs)

    def getTestCaseForTestPlan(self, dictargs):
        dictargs["devKey"] = self.devKey
        return self.server.tl.getTestCasesForTestPlan(dictargs)

    def getTestCaseIDByName(self, dictargs):
        dictargs["devKey"] = self.devKey
        return self.server.tl.getTestCaseIDByName(dictargs)

    def createTestPlan(self, dictargs):
        dictargs["devKey"] = self.devKey
        return self.server.tl.createTestPlan(dictargs)

    def addTestCaseToTestPlan(self, dictargs):
        dictargs["devKey"] = self.devKey
        return self.server.tl.addTestCaseToTestPlan(dictargs)

# substitute your Dev Key Here
client = TestlinkAPIClient(TESTLINKAPIKEY)

def getAllTestCaseID(userid, execution_type=2):  # execution_type 1:手动　2:自动
    args = {}
    allid = {}
    test_id = []
    args["testplanid"] = TESTPLANID
    args["buildid"] = BUILDID
    args["assignedto"] = userid
    plantestcases = client.getTestCaseForTestPlan(args)

    if 2 == execution_type:
        print('Auto test id:')
        printline()
    else:
        print('Manual test id:')
        printline()

    for k in sorted(plantestcases.keys()):
        if type(plantestcases[k]) == list:
            if plantestcases[k][0]['execution_type'] == str(execution_type):
                test_id.append(str(plantestcases[k][0]['tcase_id']))
                print(plantestcases[k][0]['tcase_id'] + " : " + str(plantestcases[k][0]['tcase_name']))

    printline()
    print("Total cases: %d" % len(test_id))
    printline()
    allid['test_id'] = test_id

    return allid

def getCaseId(path=idfilename):
    caseid_dict = getAllTestCaseID(USERID)

    try:
        ffile = open(path, 'w')
        print(json.dumps(caseid_dict, indent=4))
        ffile.write(json.dumps(caseid_dict, indent=4))
        ffile.close()
        return True
    except IOError:
        print("Open file %s failed." % path)
        return False

if __name__ == "__main__":
    getCaseId()
