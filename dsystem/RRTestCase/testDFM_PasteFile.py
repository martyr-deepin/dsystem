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

#2017-05-24 created by cherry
class DFM_PasteFile(unittest.TestCase):
    caseid = '220011'

    @classmethod
    def setUpClass(cls):
        cls.pwd = os.getcwd()
        cls.data = 'data'
        cls.testdir = 'testdir'
        cls.fileName =  'testDecompress.tar.gz'
        cls.eventType = 'PasteFile'
        cls.testFilePath = 'file://' + '/'.join([cls.pwd, cls.data, cls.fileName])
        cls.urlList = []
        cls.remove_pasteFile = '/'.join([cls.pwd, cls.data, cls.testdir, cls.fileName])
        cls.targetUrl = 'file://' + '/'.join([cls.pwd, cls.data, cls.testdir])

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

    def testPasteFile_urlList_action_targetUrl(self):
        args = {"eventType": self.eventType,
                "urlList": self.urllist(self.testFilePath),
                "action": 1,
                "targetUrl": self.targetUrl,
                "mode": 2}
        cmdstring = self.cmdline(args)
        print(cmdstring)

        child1 = subprocess.Popen("dde-file-manager -d >/dev/null 2>&1", shell=True)
        sleep(2)

        (status, output) = rt(cmdstring)
        sleep(2)

        List_output_ls = os.listdir('/'.join([self.pwd, self.data, self.testdir]))
        '''
        (status_ls, output_ls) = rt('ls ../data/testdir')
        List_output_ls = output_ls.split("\n")
        print(List_output_ls)
        '''
        filename = self.judge(self.fileName, List_output_ls)
        print(filename)
        self.assertTrue( 1 == filename)

        removefile = os.remove(self.remove_pasteFile)
        self.assertTrue(None == removefile)

        print(child1.pid)
        child1.kill()
        os.system('killall dde-file-manager')

    def suite():
        suite = unittest.TestSuite()
        suite.addTest(DFM_PasteFile('testPasteFile_urlList_action_targetUrl'))
        return suite

if __name__ == "__main__":
    unittest.installHandler()
    runTest(DFM_PasteFile)
