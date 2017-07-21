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

#2017-06-01 created by cherry
class DFM_NewFile(unittest.TestCase):
    caseid = '220015'

    @classmethod
    def setUpClass(cls):
        cls.pwd = os.getcwd()
        cls.data = 'data'
        #cls.fileName =  '新建文本txt'
        cls.fileName =  'New Filetxt'
        cls.eventType = 'NewFile'
        cls.testFilePath = 'file://' + '/'.join([cls.pwd, cls.data])
        cls.testFile = '/'.join([cls.pwd, cls.data, cls.fileName])
        cls.testsuffix = 'txt'

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

    def testNewFile_url_suffix(self):
        args = {"eventType": self.eventType,
                "url": self.testFilePath,
                "suffix": self.testsuffix,
                "mode": 2}
        cmdstring = self.cmdline(args)
        print(cmdstring)

        child1 = subprocess.Popen("dde-file-manager -d >/dev/null 2>&1", shell=True)
        sleep(2)

        #list the name of dir='~/dapps/dde_file_manager/data/'
        List_output_ls = os.listdir('/'.join([self.pwd, self.data]))
        result = self.judge(self.fileName, List_output_ls)
        if result == 1:
            os.remove(self.testFile)

        #run the test
        (status, output) = rt(cmdstring)
        sleep(2)
 
        #list the name of dir='~/dapps/dde_file_manager/data/'
        List_output_ls = os.listdir('/'.join([self.pwd, self.data]))
        print(List_output_ls)

        #judge whether the test successful?
        result = self.judge(self.fileName, List_output_ls)
        print(result)
        self.assertTrue( 1 == result)
        os.remove(self.testFile)

        print(child1.pid)
        child1.kill()
        os.system('killall dde-file-manager')

    def suite():
        suite = unittest.TestSuite()
        suite.addTest(DFM_NewFile('testNewFile_url_suffix'))
        return suite

if __name__ == "__main__":
    unittest.installHandler()
    runTest(DFM_NewFile)
