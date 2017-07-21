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
class DFM_OpenInTerminal(unittest.TestCase):
    caseid = '220023'

    @classmethod
    def setUpClass(cls):
        cls.pwd = os.getcwd()
        cls.data = 'data'
        cls.fileName =  'testdir'
        cls.eventType = 'OpenInTerminal'
        cls.testFilePath = 'file://' + '/'.join([cls.pwd, cls.data, cls.fileName])
        cls.windowName = cls.fileName + ' - Deepin Terminal'

    @classmethod
    def tearDownClass(cls):
        pass

    def cmdline(self, argDict):
        args = json.dumps(argDict)
        return 'dde-file-manager -e \'' + args + '\''

    def testOpenInTerminal_url(self):
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

        docwin = window.findWindow(self.windowName)
        self.assertTrue(None != docwin)

        window.closeWindow(docwin)

        docwinclose = window.findWindow(self.windowName, mode="nowait")
        self.assertTrue(None == docwinclose)

        print(child1.pid)
        child1.kill()
        os.system('killall dde-file-manager')

    def suite():
        suite = unittest.TestSuite()
        suite.addTest(DFM_OpenInTerminal('testOpenInTerminal_url'))
        return suite

if __name__ == "__main__":
    unittest.installHandler()
    runTest(DFM_OpenInTerminal)
