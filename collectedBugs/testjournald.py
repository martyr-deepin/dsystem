#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from lib import runner,utils
from subprocess import getoutput

result = True
caseid = '80272'
casename = "all-2974:systemd-journalctl日志大小限制"

class RestrictLog(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.startTime = time.time()
        cls.log = 'SystemMaxUse=500M'
        cls.cmd = "cat /etc/systemd/journald.conf |grep SystemMaxUse"


    @classmethod
    def tearDownClass(cls):
        seconds = %.3f % (time.time() - cls.startTime)
        minutes = utils.convertToMinutes(float(seconds))
        global result
        utils.commitresult(caseid, result, minutes)


    def testRestrictLog(self):
        output = getoutput(self.cmd)
        self.assertEqual(output, self.log)


    def suite():
        suite = unittest.TestSuite()
        suite.addTest(RestrictLog('testRestrictLog'))
        return suite

    class MyTestResult(runner.MyTextTestResult):
        def addError(self, test, err):
            super(RestrictLog.MyTestResult, self).addError(test, err)
            global result
            result = result and False

        def addFailure(self, test, err):
            super(RestrictLog.MyTestResult, self).addFailure(test, err)
            global result
            result = result and False

if __name__ == "__main__":
    unittest.TextTestRunner(resultclass=RestrictLog.MyTestResult).run(RestrictLog.suite())
