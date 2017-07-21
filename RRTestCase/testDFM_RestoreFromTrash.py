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
class DFM_RestoreFromTrash(unittest.TestCase):
    caseid = '220009'

    @classmethod
    def setUpClass(cls):
        cls.pwd = os.getcwd()
        cls.data = 'data'
        cls.fileName =  'testMoveToTrash.txt'
        cls.eventType = 'RestoreFromTrash'
        cls.testFilePath = 'trash:///' + '/'.join([cls.fileName])
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

    def testRestoreFromTrash_urlList(self):
        
        args = {"eventType": self.eventType,
                "urlList": self.urllist(self.testFilePath),
                "mode": 2}
        cmdstring = self.cmdline(args)
        print(cmdstring)

        child1 = subprocess.Popen("dde-file-manager -d >/dev/null 2>&1", shell=True)
        sleep(2)

        
        #run the test
        (status, output) = rt(cmdstring)
        sleep(2)
       
       #list the name of dir='~/.local/share/Trash/files/'
        List_output_ls = os.listdir('/'.join([self.pwd, self.data]))
        print(List_output_ls)

        #judge whether the test successful?
        result = self.judge(self.fileName, List_output_ls)
        print(result)
        self.assertTrue( 1 == result)
        

        print(child1.pid)
        child1.kill()
        os.system('killall dde-file-manager')

    def suite():
        suite = unittest.TestSuite()
        suite.addTest(DFM_RestoreFromTrash('testRestoreFromTrash_urlList'))
        return suite

if __name__ == "__main__":
    unittest.installHandler()
    runTest(DFM_RestoreFromTrash)
