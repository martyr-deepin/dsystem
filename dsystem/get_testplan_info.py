#!/usr/bin/env python3
# coding=utf-8

import os
import sys
import json
import requests
import xmlrpc.client

TESTPLANID = os.getenv("TESTPLAN_ID") or None
BUILDID    = os.getenv("BUILD_ID") or None
SERVER_URL = os.getenv("SERVER_URL") or None
TESTLINKAPIKEY = os.getenv("TESTLINKAPIKEY") or None
rr_token = os.getenv("RR_TOKEN") or None
headers = {"Access-Token": rr_token}

host        = os.getenv("HOST_API") or None
review_id   = os.getenv("REVIEW_ID") or None
review_path = "review"

def printline():
    print('-' * 80)

idfilename = "id.txt"

def get_review_info(id = None):
    if None == id or None == host or None == rr_token:
        return (None, None)

    url_review = "/".join((host, review_path, review_id))
    data_response = requests.get(url_review, headers=headers)
    jsondata = json.loads(data_response.text)

    plan_id = None
    build_id = None
    try:
        plan_id  = jsondata["result"]["tl_test_plan_id"]
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
printline()

if None == TESTPLANID or None == BUILDID:
    (plan_id, build_id) = get_review_info(review_id)
    TESTPLANID = plan_id
    BUILDID = build_id

    print("TESTPLAN_ID : %s\n" % TESTPLANID)
    print("BUILD_ID : %s\n" % BUILDID)
    printline()

platform_docker = '1'
platform_desktop = '2'

def getAllTestCaseID(execution_type=2):  # execution_type 1:手动　2:自动
    args = {}
    allid = {}
    docker_id = []
    lava_id = []
    args["testplanid"] = TESTPLANID

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
                #docker_id.append(str(plantestcases[k][0]['tcase_id']))
                #print(plantestcases[k][0]['tcase_id'] + " : " + str(plantestcases[k][0]['tcase_name']))
                pass

            if plantestcases[k][0]['execution_type'] == str(execution_type):
                lava_id.append(plantestcases[k][0]['tcase_id'])
                print(plantestcases[k][0]['tcase_id'] + " : " + str(plantestcases[k][0]['tcase_name']))

        if type(plantestcases[k]) == dict:
            if platform_docker in plantestcases[k].keys() and str(execution_type) == plantestcases[k][platform_docker]['execution_type']:
                docker_id.append(str(plantestcases[k][platform_docker]['tcase_id']))
                print(plantestcases[k][platform_docker]['tcase_id'] + " : " + str(plantestcases[k][platform_docker]['tcase_name']))

            if platform_desktop in plantestcases[k].keys() and str(execution_type) == plantestcases[k][platform_desktop]['execution_type']:
                lava_id.append(plantestcases[k][platform_desktop]['tcase_id'])
                print(plantestcases[k][platform_desktop]['tcase_id'] + " : " + str(plantestcases[k][platform_desktop]['tcase_name']))

    printline()
    # print("docker_id "),
    # print(docker_id)
    print("lava_id: ")
    print(lava_id)
    # allid['docker_id'] = docker_id
    # allid['lava_id'] = ",".join(str(i) for i in lava_id)
    allid['lava_id'] = lava_id

    return allid

def main():
    caseid_dict = getAllTestCaseID()

    if 0 == len(caseid_dict["lava_id"]):
        print("lave_id list is 0.")
        sys.exit(1)

    ffile = open(idfilename, 'w')
    # print(caseid_dict)
    ffile.write(json.dumps(caseid_dict))
    ffile.close()

if __name__ == "__main__":
    main()
