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

#2017-05-23 created by cherry
class DFM_DecompressFileHere(unittest.TestCase):
    caseid = '220001'

    @classmethod
    def setUpClass(cls):
        cls.pwd = os.getcwd()
        cls.data = 'data'
        cls.fileName =  'testDecompress.tar.gz'
        cls.eventType = 'DecompressFileHere'
        cls.testFilePath = 'file://' + '/'.join([cls.pwd, cls.data, cls.fileName])
        cls.urlList = []
        cls.applicationName = 'Archive Manager'
        cls.decompressfileName = 'testDecompress'
        cls.remove_decompressFile = '/'.join([cls.pwd, cls.data, cls.decompressfileName])

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

    def testDecompressFileHere_URLLIST(self):
        
        args = {"eventType": self.eventType,
                "urlList": self.urllist(self.testFilePath),
                "mode": 2}
        cmdstring = self.cmdline(args)
        print(cmdstring)

        child1 = subprocess.Popen("dde-file-manager -d >/dev/null 2>&1", shell=True)
        sleep(2)
        
        (status, output) = rt(cmdstring)
        sleep(2)
       
        List_output_ls = os.listdir('/'.join([self.pwd, self.data]))
        '''
        (status_ls, output_ls) = rt('ls ../data/')
        List_output_ls = output_ls.split("\n")
        '''
        print(List_output_ls)
        print(self.decompressfileName)

        decompress_filename = self.judge(self.decompressfileName, List_output_ls)
        print(decompress_filename)
        self.assertTrue( 1 == decompress_filename)
        
        removefile = shutil.rmtree(self.remove_decompressFile)
        self.assertTrue(None == removefile)

        print(child1.pid)
        child1.kill()
        os.system('killall dde-file-manager')

    def suite():
        suite = unittest.TestSuite()
        suite.addTest(DFM_DecompressFileHere('testDecompressFileHere_URLLIST'))
        return suite

if __name__ == "__main__":
    unittest.installHandler()
    runTest(DFM_DecompressFileHere)
