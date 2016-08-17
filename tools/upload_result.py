#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import xmlrpc.client

TESTPLANID = os.getenv("TESTPLAN_ID")
BUILDID  = os.getenv("BUILD_ID")
SERVER_URL = os.getenv("SERVER_URL")
TESTLINKAPIKEY = os.getenv("TESTLINKAPIKEY")

if TESTPLANID == None or BUILDID == None or SERVER_URL == None or TESTLINKAPIKEY == None:
    print("Please make sure you have export the TESTPLAN_ID, BUILD_ID, TESTLINKAPIKEY and SERVER_URL")
    sys.exit(2)

resultname = "../result.txt"

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

    def reportToTestlink(self, dictargs):
        dictargs["devKey"] = self.devKey
        return self.server.tl.reportTCResult(dictargs)

# substitute your Dev Key Here
client = TestlinkAPIClient(TESTLINKAPIKEY)

def getAllTestCaseID():
    args = {}
    allid = []
    args["testplanid"] = TESTPLANID
    plantestcases = client.getTestCaseForTestPlan(args)
    for k in sorted(plantestcases.keys()):
        allid.append(plantestcases[k][0]['tcase_id'])
        print(plantestcases[k][0]['tcase_id'] + " : " + str(plantestcases[k][0]['tcase_name']))

    print('-' * 80)

    return allid

def reportToTestlink(case_id, case_status):
    args = {}
    args["testplanid"] = TESTPLANID
    args["testcaseid"] = case_id
    args["buildid"] = BUILDID
    args["status"] = case_status
    result = client.reportToTestlink(args)
    print(result)

def reportTCResult(path=resultname):
    try:
        ffile = open(path, 'r')

        while 1:
            line = ffile.readline()
            if not line:
                break
            tc_id, tc_result = line.split()

            tl_result = None
            if tc_result == 'True':
                tl_result = 'p'
            elif tc_result == 'False':
                tl_result = 'f'

            print(tc_id + " : " + tc_result)
            reportToTestlink(int(tc_id), tl_result)
        ffile.close()
    except IOError:
        print("Open %s failed." % path)

if __name__ == "__main__":
    reportTCResult()
