#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import gettext
import unittest
import json
from time import sleep
from lib import runTest
from subprocess import getstatusoutput as rt
from lib import window
import subprocess

class DFM_OpenFile(unittest.TestCase):
    caseid = '219993'

    @classmethod
    def setUpClass(cls):
        def load():
            with open('test_menu.json', 'r') as json_file:
                data = json.load(json_file)
                return data

        ddata = load()
        cls.params = ddata['OpenFile']


        cls.lang = os.getenv("LANG")
        cls.pwd = os.getcwd()
        cls.data = 'data'
        #cls.fileName = ddata['OpenFile'][1]['fileName']
        cls.eventType = 'OpenFile'
        #cls.testFilePath = 'file://' + '/'.join([cls.pwd, cls.data, cls.fileName])
        #cls.windowName = ddata['OpenFile'][1]['windowName']

    @classmethod
    def tearDownClass(cls):
        pass

    def cmdline(self, argDict):
        args = json.dumps(argDict)
        return 'dde-file-manager -e \'' + args + '\''

    def testOpenFile_URL(self, fileName, windowName):
        self.fileName = fileName
        self.testFilePath = 'file://' + '/'.join([self.pwd, self.data, self.fileName])
        self.windowName = windowName

        args = {"eventType": self.eventType,
                "url": self.testFilePath,
                "mode": 2}
        cmdstring = self.cmdline(args)
        print(cmdstring)

        child1 = subprocess.Popen("dde-file-manager -d >/dev/null 2>&1", shell=True)
        sleep(2)

        (status, output) = rt(cmdstring)

        docwin = window.findWindow(self.windowName)
        self.assertTrue(None != docwin)

        window.closeWindow(docwin)

        docwinclose = window.findWindow(self.windowName, mode="nowait")
        self.assertTrue(None == docwinclose)

        print(child1.pid)
        child1.kill()
        os.system('killall dde-file-manager')

    def testOpenFile(self):
        for item in self.params:
            print(item)

            if self.lang == "en_US.UTF-8":
                self.testOpenFile_URL(item['fileName'], item['windowName_en'])
            else:
                self.testOpenFile_URL(item['fileName'], item['windowName_zh'])

            print('\033[32m********************************************************************************\033[0m')

    def suite():
        suite = unittest.TestSuite()
        #suite.addTest(DFM_OpenFile('testOpenFile_URL'))
        suite.addTest(DFM_OpenFile('testOpenFile'))
        return suite

if __name__ == "__main__":
    unittest.installHandler()
    runTest(DFM_OpenFile)

