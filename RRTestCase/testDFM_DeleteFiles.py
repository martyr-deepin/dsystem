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

#2017-05-27 created by cherry
class DFM_DeleteFiles(unittest.TestCase):
    caseid = '220005'

    @classmethod
    def setUpClass(cls):
        cls.pwd = os.getcwd()
        cls.data = 'data'
        cls.fileName =  'testDeleteFiles.txt'
        cls.eventType = 'DeleteFiles'
        cls.testFilePath = 'file://' + '/'.join([cls.pwd, cls.data, cls.fileName])
        cls.urlList = []
        cls.testFile = '/'.join([cls.pwd, cls.data, cls.fileName])

    @classmethod
    def tearDownClass(cls):
        pass

    def urllist(self, testpath):
        urlList = self.urlList
        urlList.append(testpath)
        return urlList

    def judge(self, name, argList):
        for filename in argList:
            if filename == name:
                return 1
            else:
                print(0)

    def cmdline(self, argDict):
        args = json.dumps(argDict)
        return 'dde-file-manager -e \'' + args + '\''

    def testDeleteFiles_urlList_silent(self):
        
        args = {"eventType": self.eventType,
                "urlList": self.urllist(self.testFilePath),
                "silent": True,
                "mode": 2}
        print(args)
        cmdstring = self.cmdline(args)
        print(cmdstring)

        child1 = subprocess.Popen("dde-file-manager -d >/dev/null 2>&1", shell=True)
        sleep(2)
        
        os.mknod(self.testFile)    
        List_output_ls = os.listdir('/'.join([self.pwd, self.data]))
        filename = self.judge(self.fileName, List_output_ls)
        print(filename)
        self.assertTrue( 1 == filename)


        (status, output) = rt(cmdstring)
        sleep(2)
        List_output_ls = os.listdir('/'.join([self.pwd, self.data]))
        filename = self.judge(self.fileName, List_output_ls)
        print(filename)
        self.assertTrue( None == filename)


        print(child1.pid)
        child1.kill()
        os.system('killall dde-file-manager')

    def suite():
        suite = unittest.TestSuite()
        suite.addTest(DFM_DeleteFiles('testDeleteFiles_urlList_silent'))
        return suite

if __name__ == "__main__":
    unittest.installHandler()
    runTest(DFM_DeleteFiles)
