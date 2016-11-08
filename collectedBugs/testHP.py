#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from lib import runner,utils
from subprocess import getoutput

result = True
caseid = '80240'
casename = "all-2967:hplipj集成测试"

class HPIntergration(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.startTime = time.time()
        cls.installed = 'ii'
        cls.pkg1 = "dpkg -l |grep hpijs-ppds |awk END'{print $1}'"
        cls.pkg2 = "dpkg -l |grep hplip |awk END'{print $1}'"
        cls.pkg3 = "dpkg -l |grep hplip-data |awk END'{print $1}'"
        cls.pkg4 = "dpkg -l |grep libhpmud0 |awk END'{print $1}'"
        cls.pkg5 = "dpkg -l |grep libsane-hpaio |awk END'{print $1}'"
        cls.pkg6 = "dpkg -l |grep openprinting-ppds |awk END'{print $1}'"
        cls.pkg7 = "dpkg -l |grep printer-driver-hpcups |awk END'{print $1}'"
        cls.pkg8 = "dpkg -l |grep printer-driver-hpijs |awk END'{print $1}'"


    @classmethod
    def tearDownClass(cls):
        seconds = %.3f % (time.time() - cls.startTime)
        minutes = utils.convertToMinutes(float(seconds))
        global result
        utils.commitresult(caseid, result, minutes)


    def testhpijs(self):
        pkg1 = getoutput(self.pkg1)
        self.assertEqual(pkg1, self.installed)
    def testhplip(self):
        pkg2 = getoutput(self.pkg2)
        self.assertEqual(pkg2, self.installed)
    def testhplip_data(self):
        pkg3 = getoutput(self.pkg3)
        self.assertEqual(pkg3, self.installed)
    def testlibhpmud0(self):
        pkg4 = getoutput(self.pkg4)
        self.assertEqual(pkg4, self.installed)
    def testlibsane(self):
        pkg5 = getoutput(self.pkg5)
        self.assertEqual(pkg5, self.installed)
    def testopenprinting(self):
        pkg6 = getoutput(self.pkg6)
        self.assertEqual(pkg6, self.installed)
    def testhpcups(self):
        pkg7 = getoutput(self.pkg7)
        self.assertEqual(pkg7, self.installed)
    def testdriver_hpijs(self):
        pkg8 = getoutput(self.pkg8)
        self.assertEqual(pkg8, self.installed)


    def suite():
        suite = unittest.TestSuite()
        suite.addTest(HPIntergration('testhpijs'))
        suite.addTest(HPIntergration('testhplip'))
        suite.addTest(HPIntergration('testhplip_data'))
        suite.addTest(HPIntergration('testlibhpmud0'))
        suite.addTest(HPIntergration('testlibsane'))
        suite.addTest(HPIntergration('testopenprinting'))
        suite.addTest(HPIntergration('testhpcups'))
        suite.addTest(HPIntergration('testdriver_hpijs'))
        return suite

    class MyTestResult(runner.MyTextTestResult):
        def addError(self, test, err):
            super(HPIntergration.MyTestResult, self).addError(test, err)
            global result
            result = result and False

        def addFailure(self, test, err):
            super(HPIntergration.MyTestResult, self).addFailure(test, err)
            global result
            result = result and False

if __name__ == "__main__":
    unittest.TextTestRunner(resultclass=HPIntergration.MyTestResult).run(HPIntergration.suite())
