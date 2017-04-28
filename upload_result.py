#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import json
import requests
import xmlrpc.client

TESTPLANID = os.getenv("TESTPLAN_ID") or None
BUILDID    = os.getenv("BUILD_ID") or None
SERVER_URL = os.getenv("SERVER_URL") or None
TESTLINKAPIKEY = os.getenv("TESTLINKAPIKEY") or None

resultname = "result.txt"

def get_review_info(id = None):
    if None == id or None == host or None == rr_token:
        return (None, None)

    url_review = "/".join((host, review_path, review_id))
    data_response = requests.get(url_review, headers=headers)
    jsondata = json.loads(data_response.text)

    plan_id = None
    build_id = None
    try:
        plan_id = jsondata["result"]["tl_test_plan_id"]
        build_id = jsondata["result"]["tl_build_id"]
        return (plan_id, build_id)
    except Exception:
        print("Got keyError Exception jsondata")
        return (None, None)

class TestlinkAPIClient:
    def __init__(self, devKey):
        self.server = xmlrpc.client.ServerProxy(SERVER_URL)
        self.devKey = devKey

    def getInfo(self):
        return self.server.tl.about()

    def getProjects(self):
        return self.server.tl.getProjects(dict(devKey=self.devKey))

    def testLinkVersion(self):
        dictargs = {}
        dictargs["devKey"] = self.devKey
        return self.server.tl.testLinkVersion(dictargs)

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

def reportToTestlink(case_id, case_status, duration, platform_id):
    args = {}
    args["testplanid"] = TESTPLANID
    args["testcaseid"] = case_id
    # args["platformid"] = platform_id
    # args["buildname"] = "new version"
    # args["buildname"] = BUILDNAME
    # args["notes"] = 'something'
    args["execduration"] = duration
    args["buildid"] = BUILDID
    args["status"] = case_status
    result = client.reportToTestlink(args)
    print(result)

rr_token = os.getenv("RR_TOKEN") or None
headers = {"Access-Token": rr_token}

host        = os.getenv("HOST_API") or None
review_id   = os.getenv("REVIEW_ID") or None
review_path = "review"

if TESTPLANID == None or BUILDID == None:
    (plan_id, build_id) = get_review_info(review_id)
    TESTPLANID = plan_id
    BUILDID = build_id

    print("TESTPLAN_ID : %s" % TESTPLANID)
    print("BUILDID : %s" % BUILDID)
    print('-' * 80)

platform_docker_id = 1
platform_desktop_id = 2

ffile = open(resultname, 'r')
try:
    #result_content = ffile.read()
    while 1:
        line = ffile.readline()

        if not line:
            break
        tc_id, tc_result, time_duration = line.strip('\n').split()
        print(tc_id + " : " + tc_result)

        upload_result = ''

        if 'True' == tc_result:
            tc_result = 'Pass'
        else:
            tc_result = 'Fail'

        reportToTestlink(int(tc_id), tc_result[0].lower(), time_duration, platform_desktop_id)
finally:
    ffile.close()

print(client.testLinkVersion())
