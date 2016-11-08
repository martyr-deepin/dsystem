#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from lib import runner,utils
from lib.filesystem import *
from glob import glob

result = True

class FilesystemNtfs(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.startTime = time.time()
        cls.caseid = '42903'
        cls.casename = 'all-1995:读写ntfs格式的文件'
        mkextx('ntfs')

    @classmethod
    def tearDownClass(cls):
        seconds = %.3f % (time.time() - cls.startTime)
        minutes = utils.convertToMinutes(float(seconds))
        global result
        utils.commitresult(caseid, result, minutes)
        chroot('sudo rm -rf /mnt/*', 'sudo umount /mnt')

    def testTxt(self):
        mntFiles = glob('/mnt/*')
        txt = '/mnt/a.txt'
        self.assertIn(txt, mntFiles)

    def testDirs(self):
        mntFiles = glob('/mnt/*')
        dir1 = '/mnt/中文'
        dir2 = '/mnt/test'
        dir3 = '/mnt/中文test'
        self.assertIn(dir1, mntFiles)
        self.assertIn(dir2, mntFiles)
        self.assertIn(dir3, mntFiles)

    def testTxts(self):
        mntFiles1 = glob('/mnt/中文/*')
        mntFiles2 = glob('/mnt/test/*')
        mntFiles3 = glob('/mnt/中文test/*')
        txt1 = '/mnt/中文/中文.txt'
        txt2 = '/mnt/中文/test.txt'
        txt3 = '/mnt/中文/中文test.txt'
        txt4 = '/mnt/test/中文.txt'
        txt5 = '/mnt/test/test.txt'
        txt6 = '/mnt/test/中文test.txt'
        txt7 = '/mnt/中文test/中文.txt'
        txt8 = '/mnt/中文test/test.txt'
        txt9 = '/mnt/中文test/中文test.txt'
        self.assertIn(txt1, mntFiles1)
        self.assertIn(txt2, mntFiles1)
        self.assertIn(txt3, mntFiles1)
        self.assertIn(txt4, mntFiles2)
        self.assertIn(txt5, mntFiles2)
        self.assertIn(txt6, mntFiles2)
        self.assertIn(txt7, mntFiles3)
        self.assertIn(txt8, mntFiles3)
        self.assertIn(txt8, mntFiles3)

    def suite():
        suite = unittest.TestSuite()
        suite.addTest(FilesystemNtfs('testTxt'))
        suite.addTest(FilesystemNtfs('testDirs'))
        suite.addTest(FilesystemNtfs('testTxts'))
        return suite

    class MyTestResult(runner.MyTextTestResult):
        def addError(self, test, err):
            super(FilesystemNtfs.MyTestResult, self).addError(test, err)
            global result
            result = result and False

        def addFailure(self, test, err):
            super(FilesystemNtfs.MyTestResult, self).addFailure(test, err)
            global result
            result = result and False

if __name__ == "__main__":
    unittest.TextTestRunner(resultclass=FilesystemNtfs.MyTestResult).run(FilesystemNtfs.suite())
