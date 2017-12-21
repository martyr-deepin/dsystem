#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os,shutil
import gettext
import unittest
from time import sleep
import json
from lib import runTest
from subprocess import getstatusoutput as rt
import subprocess
from lib import window

#2017-06-02 created by cherry
class DFM_OpenFileLocation(unittest.TestCase):
    caseid = '220017'

    @classmethod
    def setUpClass(cls):
        cls.pwd = os.getcwd()
        cls.data = 'data'
        cls.fileName =  'testOpenFileLocation.txt'
        cls.eventType = 'OpenFileLocation'
        cls.testFilePath = 'file://' + '/'.join([cls.pwd, cls.data, cls.fileName])
        cls.testFile = '/'.join([cls.pwd, cls.data, cls.fileName])
        cls.applicationName = 'Deepin File Manager'

    @classmethod
    def tearDownClass(cls):
        pass

    def cmdline(self, argDict):
        args = json.dumps(argDict)
        return 'dde-file-manager -e \'' + args + '\''

    def testOpenFileLocation_url(self):
        args = {"eventType": self.eventType,
                "url": self.testFilePath,
                "mode": 2}
        cmdstring = self.cmdline(args)
        print(cmdstring)

        child1 = subprocess.Popen("dde-file-manager -d >/dev/null 2>&1", shell=True)
        sleep(2)

        #run the test
        (status, output) = rt(cmdstring)
        sleep(2)

        docwin = window.findWindowByAppName(self.applicationName)
        self.assertTrue(None != docwin)

        window.closeWindow(docwin)

        docwinclose = window.findWindowByAppName(self.applicationName, mode="nowait")
        self.assertTrue(None == docwinclose)

    def suite():
        suite = unittest.TestSuite()
        suite.addTest(DFM_OpenFileLocation('testOpenFileLocation_url'))
        return suite

if __name__ == "__main__":
    unittest.installHandler()
    runTest(DFM_OpenFileLocation)
