#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest

from collectedBugs.testShowDesktop import ShowDesktopBtn
from collectedBugs.testHP import HPIntergration
from collectedBugs.testjournald import RestrictLog
from collectedBugs.testyoudao import Youdao
from collectedBugs.testcodename import CodeName


def main():
    classes = []
    classes.append(ShowDesktopBtn)
    classes.append(HPIntergration)
    classes.append(RestrictLog)
    classes.append(Youdao)
    classes.append(CodeName)


    for c in classes:
        unittest.TextTestRunner(resultclass=c.MyTestResult).run(c.suite())
if __name__ == '__main__':
    main()
