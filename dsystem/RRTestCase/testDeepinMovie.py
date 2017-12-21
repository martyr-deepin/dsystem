#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import time
import gettext
import unittest
import pexpect
from lib import runTest

casename = "all-6090:deepin-movie打开各类型视频文件"

class DeepinMovie(unittest.TestCase):
    caseid = '267338'

    @classmethod
    def setUpClass(cls):
        cls.filedir = 'data/movieFiles'

    @classmethod
    def tearDownClass(cls):
        pass

    def testRunAllType(self):
        allTypeMovie = os.listdir(self.filedir)
        errorList = []

        for ifile in allTypeMovie:
            child = pexpect.spawn("deepin-movie \
                    '%s/%s'" % (self.filedir, ifile))

            i = child.expect(["cplayer: Playing:", pexpect.EOF, pexpect.TIMEOUT], 5)

            if 0 == i:
                print("Playing movie %s OK." % ifile)
                time.sleep(6)
            elif 1 == i:
                print("Error : %s." % ifile)
                errorList.append(ifile)
            elif 2 == i:
                print("Time out : %s" % ifile)
                errorList.append(ifile)

        self.assertTrue(0 == len(errorList), "errorList movie file: %s" % str(errorList))

    def suite():
        suite = unittest.TestSuite()
        suite.addTest(DeepinMovie('testRunAllType'))
        return suite

if __name__ == "__main__":
    unittest.installHandler()
    LOCALE_DIR = os.path.abspath("./lib/locale")
    gettext.install('dsystem', LOCALE_DIR)
    runTest(DeepinMovie)
