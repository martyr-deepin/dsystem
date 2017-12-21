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
class DFM_CreateSymlink(unittest.TestCase):
    caseid = '220019'

    @classmethod
    def setUpClass(cls):
        cls.pwd = os.getcwd()
        cls.data = 'data'
        cls.fileName =  'testCreateSymlink.txt'
        cls.eventType = 'CreateSymlink'
        cls.testFilePath = 'file://' + '/'.join([cls.pwd, cls.data, cls.fileName])
        cls.testFile = '/'.join([cls.pwd, cls.data, cls.fileName])
        cls.test_toUrl = '~/' + '/'.join(['Desktop', cls.fileName])
        cls.desktopurl = '/home/deepin/Desktop/'

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

    def testCreateSymlink_fileUrl_toUrl(self):
        
        args = {"eventType": self.eventType,
                "fileUrl": self.testFilePath,
                "toUrl": self.test_toUrl,
                "mode": 2}
        cmdstring = self.cmdline(args)
        print(cmdstring)

        child1 = subprocess.Popen("dde-file-manager -d >/dev/null 2>&1", shell=True)
        sleep(2)

        #list the name of dir='~/Desktop/'
        List_output_ls = os.listdir(self.desktopurl)
        result = self.judge(self.fileName, List_output_ls)
        if result == 1:
            os.remove(self.desktopurl + self.fileName)

        #run the test
        (status, output) = rt(cmdstring)
        sleep(2)
       
       #list the name of dir='~/Desktop/'
        List_output_ls = os.listdir(self.desktopurl)
        print(List_output_ls)

        #judge whether the test successful?
        result = self.judge(self.fileName, List_output_ls)
        print(result)
        self.assertTrue( 1 == result)
        os.remove(self.desktopurl + self.fileName)
        

        print(child1.pid)
        child1.kill()
        os.system('killall dde-file-manager')

    def suite():
        suite = unittest.TestSuite()
        suite.addTest(DFM_CreateSymlink('testCreateSymlink_fileUrl_toUrl'))
        return suite

if __name__ == "__main__":
    unittest.installHandler()
    runTest(DFM_CreateSymlink)
