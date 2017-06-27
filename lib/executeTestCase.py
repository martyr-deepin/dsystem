#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
from unittest import TextTestRunner,TextTestResult
from lib import utils

class HandleTestResult(TextTestResult):
    def startTestRun(self):
        self.startTime=time.time()

    def startTest(self, test):
        super(HandleTestResult, self).startTest(test)
        self.test = test

    def stopTestRun(self):
        re = len(self.failures) == 0 and len(self.errors) == 0
        caseid = type(self.test).caseid
        seconds = "%.3f" % (time.time() - self.startTime)

        if float(seconds) < 0:
            seconds = '1'

        minutes = utils.convertToMinutes(float(seconds))
        utils.commitresult(caseid, re, minutes)

def runTest(testcase):
    TextTestRunner(resultclass=HandleTestResult).run(testcase.suite())
