#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import unittest
from time import sleep
import json
from lib import runTest
from subprocess import getstatusoutput as rt
import subprocess
from lib import window

#2017-06-09 created by cherry
class DFM_OpenNewWindow(unittest.TestCase):
    caseid = '220025'

    @classmethod
    def setUpClass(cls):
        cls.pwd = os.getcwd()
        cls.data = 'data'
        cls.fileName =  'testdir'
        cls.eventType = 'OpenNewWindow'
        cls.testFilePath = 'file://' + '/'.join([cls.pwd, cls.data, cls.fileName])
        cls.windowName = 'Deepin File Manager'
        cls.urlList = []

    @classmethod
    def tearDownClass(cls):
        pass

    def urllist(self, testpath):
        urlList = self.urlList
        urlList.append(testpath)
        return urlList

    def cmdline(self, argDict):
        args = json.dumps(argDict)
        return 'dde-file-manager -e \'' + args + '\''

    def testOpenINewWindow_urlList_force(self):

        args = {"eventType": self.eventType,
                "urlList": self.urllist(self.testFilePath),
                "force": True,
                "mode": 2}
        cmdstring = self.cmdline(args)
        print(cmdstring)

        #if opened dde-file-manager, close it
        docwin = window.findWindow(self.windowName)
        if docwin != None:
            window.closeWindow(docwin)

        child1 = subprocess.Popen("dde-file-manager -d >/dev/null 2>&1", shell=True)
        sleep(1)

        #run the test
        (status, output) = rt(cmdstring)
        sleep(1)

        docwin = window.findWindow(self.windowName)
        self.assertTrue(None != docwin)

        window.closeWindow(docwin)

        docwinclose = window.findWindow(self.windowName, mode="nowait")
        self.assertTrue(None == docwinclose)

        print(child1.pid)
        child1.kill()
        # os.system('killall dde-file-manager')

    def suite():
        suite = unittest.TestSuite()
        suite.addTest(DFM_OpenNewWindow('testOpenINewWindow_urlList_force'))
        return suite

if __name__ == "__main__":
    unittest.installHandler()
    runTest(DFM_OpenNewWindow)
