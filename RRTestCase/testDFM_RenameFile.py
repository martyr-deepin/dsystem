#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import gettext
import unittest
from time import sleep
import json
from lib import runTest
from subprocess import getstatusoutput as rt
import subprocess
from lib import window

#2017-05-26 created by cherry
class DFM_RenameFile(unittest.TestCase):
    caseid = '220003'

    @classmethod
    def setUpClass(cls):
        cls.pwd = os.getcwd()
        cls.data = 'data'
        cls.fileName =  'testRenameFile.txt'
        cls.fileName_new = 'testRenameFile_new.txt'
        cls.eventType = 'RenameFile'
        cls.testFilePath = 'file://' + '/'.join([cls.pwd, cls.data, cls.fileName])
        cls.testFilePath_new = 'file://' + '/'.join([cls.pwd, cls.data, cls.fileName_new])
        cls.urlList = []       


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
            print('\33[32m%s is not exist!!\33[0m' % name)

    def cmdline(self, argDict):
        args = json.dumps(argDict)
        return 'dde-file-manager -e \'' + args + '\''

    def testRenameFile_from_to(self):
        
        args = {"eventType": self.eventType,
                "from": self.testFilePath,
                "to": self.testFilePath_new,
                "mode": 2}
        cmdstring = self.cmdline(args)
        print(cmdstring)
        
        child1 = subprocess.Popen("dde-file-manager -d >/dev/null 2>&1", shell=True)
        sleep(2)
        
        #"fileName" in the pathpwd?
        List_output_ls = os.listdir('/'.join([self.pwd, self.data]))
        filename = self.judge(self.fileName, List_output_ls)
        self.assertTrue( 1 == filename)


        (status, output) = rt(cmdstring)

        
        List_output_ls = os.listdir('/'.join([self.pwd, self.data]))
        filename = self.judge(self.fileName_new, List_output_ls)
        print(filename)
        self.assertTrue( 1 == filename)
        
        sleep(2)
        fileName_new = '/'.join([self.pwd, self.data, self.fileName_new]) 
        fileName = '/'.join([self.pwd, self.data, self.fileName])
        os.rename(fileName_new, fileName)
        
        print(child1.pid)
        child1.kill()
        os.system('killall dde-file-manager')
        
    def suite():
        suite = unittest.TestSuite()
        suite.addTest(DFM_RenameFile('testRenameFile_from_to'))
        return suite

if __name__ == "__main__":
    unittest.installHandler()
    runTest(DFM_RenameFile)

