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

#2017-06-06 created by cherry
class DFM_FileShare(unittest.TestCase):
    caseid = '220021'

    @classmethod
    def setUpClass(cls):
        cls.pwd = os.getcwd()
        cls.data = 'data'
        cls.fileName =  'testdir'
        cls.eventType = 'FileShare'
        cls.testFilePath = 'file://' + '/'.join([cls.pwd, cls.data, cls.fileName])
        cls.sharename = 'cherry_share'
        cls.share_list = []

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

    def testFileShare_url_name_isWritable_allowGuest(self):
        
        args = {"eventType": self.eventType,
                "url": self.testFilePath,
                "name": self.sharename,
                "isWritable": True,
                "allowGuest": True,
                "mode": 2}
        cmdstring = self.cmdline(args)
        print(cmdstring)

        child1 = subprocess.Popen("dde-file-manager -d >/dev/null 2>&1", shell=True)
        sleep(2)

        #if there's a share file named "cherry_share",delete it
        dele = 'net usershare delete ' + self.sharename
        (status, output) = rt(dele)

        #run the test
        (status, output) = rt(cmdstring)
        sleep(2)
       
       #list the name of share
        for line in os.popen("net usershare list"):
            line = line.strip('\n')
            self.share_list.append(line)
        print(self.share_list)

        #judge whether the test successful?
        result = self.judge(self.sharename, self.share_list)
        print(result)
        self.assertTrue( 1 == result)

        #delete the share file 
        (status, output) = rt(dele)

        print(child1.pid)
        child1.kill()
        os.system('killall dde-file-manager')

    def suite():
        suite = unittest.TestSuite()
        suite.addTest(DFM_FileShare('testFileShare_url_name_isWritable_allowGuest'))
        return suite

if __name__ == "__main__":
    unittest.installHandler()
    runTest(DFM_FileShare)
