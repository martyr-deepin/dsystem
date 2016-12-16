#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from lib import executeTestCase
from lib import runner,utils
from subprocess import getoutput

result = True
casename = "all-2974:systemd-journalctl日志大小限制"

class RestrictLog(unittest.TestCase):
    caseid = '80272'
    @classmethod
    def setUpClass(cls):
        cls.log = 'SystemMaxUse=500M'
        cls.cmd = "cat /etc/systemd/journald.conf |grep SystemMaxUse"


    @classmethod
    def tearDownClass(cls):
        pass
    def testRestrictLog(self):
        output = getoutput(self.cmd)
        self.assertEqual(output, self.log)


    def suite():
        suite = unittest.TestSuite()
        suite.addTest(RestrictLog('testRestrictLog'))
        return suite

if __name__ == "__main__":
    executeTestCase.runTest(RestrictLog)
