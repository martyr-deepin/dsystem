#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from subprocess import getstatusoutput
import re
from lib import runner
from lib import utils

result = True
caseid = '39058'
casename = 'all-1458:进程管理命令--验证对ps命令的支持'

class  Ps(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        global result
        utils.commitresult(caseid, result)

    def setUp(self):
    	pass

    def tearDown(self):
    	pass

    def testPsOne(self):
        (status,output) = getstatusoutput('ps')
        self.assertTrue(0 == status)
        psresult = output.split('\n')
        self.assertTrue(psresult[0].strip() =='PID TTY          TIME CMD')
        listps  = []
        for i in psresult[1:]:
            m = re.match(r'^\d+.+\d{2}:\d{2}:\d{2}.+$',i.strip())
            self.assertTrue(m != None)   #m取值为None（失败）或_sre.SRE_Match类型（成功）
            listps.append((i.split())[-1])
        (status,output) = getstatusoutput('echo $SHELL')
        shelltype = (output.split('/'))[-1]
        self.assertIn(shelltype,listps)
        self.assertIn('ps',listps)
        self.assertTrue(len(listps) <= 4)

    def testPsTwo(self):
        (status,output) = getstatusoutput('ps -A')
        self.assertTrue(0 == status)
        psaresult = output.split('\n')
        self.assertTrue(psaresult[0].strip() == 'PID TTY          TIME CMD')
        listpsa = []
        for i in psaresult[1:]:
            m = re.match(r'^\d+.+\d{2}:\d{2}:\d{2}.+$',i.strip())
            self.assertTrue(m != None)
            listpsa.append((i.split())[-1])
        self.assertIn('systemd',listpsa)
        self.assertIn('kthreadd',listpsa)
        self.assertTrue(len(listpsa) > 50)

    def testPsThree(self):
        (status,output) = getstatusoutput('ps -au')
        self.assertTrue(0 == status)
        psauresult = output.split('\n')
        self.assertTrue(psauresult[0].strip() == 'USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND')
        listpsau = []
        for i in psauresult[1:]:
            listpsau.append((i.split())[-1])
        self.assertIn('linux',listpsau)
        self.assertTrue(len(listpsau) >= 4)

    def testPsFour(self):
        (status,output) = getstatusoutput('ps -x')
        self.assertTrue(0 == status)
        psxresult = output.split('\n')
        self.assertTrue(psxresult[0].strip() == 'PID TTY      STAT   TIME COMMAND')
        listpsx = []
        for i in psxresult[1:]:
            listpsx.append((i.split())[-1])
        self.assertIn('--user',listpsx)
        self.assertTrue(len(listpsx) >= 4)

    def testPsFive(self):
        (status,output) = getstatusoutput('ps -ef')
        self.assertTrue(0 == status)
        psefresult = output.split('\n')
        self.assertTrue(psefresult[0].strip() == 'UID        PID  PPID  C STIME TTY          TIME CMD')
        listpsef = []
        for i in psefresult[1:]:
            listpsef.append((i.split())[-1])
        self.assertIn(r'[rcu_sched]',listpsef)
        self.assertIn(r'[watchdog/0]',listpsef)
        self.assertTrue(len(listpsef) > 50)

    def testPsSix(self):
        (status,output) = getstatusoutput(r'ps -ef|grep bash|grep -v grep')
        bashpid = output.split()[1]
        (status,output) = getstatusoutput('ps -p %s' % bashpid)
        self.assertTrue(0 == status)
        pspresult = output.split('\n')
        self.assertTrue(pspresult[0].strip() == 'PID TTY          TIME CMD')
        self.assertTrue((pspresult[1].split())[-1] == 'bash')

    def suite():
        suite = unittest.TestSuite()
        suite.addTest(Ps('testPsOne'))
        suite.addTest(Ps('testPsTwo'))
        suite.addTest(Ps('testPsThree'))
        suite.addTest(Ps('testPsFour'))
        suite.addTest(Ps('testPsFive'))
        suite.addTest(Ps('testPsSix'))
        return suite

    class MyTestResult(runner.MyTextTestResult):
        def addError(self, test, err):
            super(Ps.MyTestResult, self).addError(test, err)
            global result
            result = result and False

        def addFailure(self, test, err):
            super(Ps.MyTestResult, self).addError(test, err)
            global result
            result = result and False

if __name__ == "__main__":
    unittest.TextTestRunner(resultclass=Ps.MyTestResult).run(Ps.suite())
