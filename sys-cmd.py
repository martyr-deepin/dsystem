#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
import os

from systemcommand.test_pwd import Pwd
from systemcommand.test_cd import Cd
from systemcommand.test_mkdir import Mkdir
from systemcommand.test_rmdir import Rmdir
from systemcommand.test_cp import Cp

def main():
    classes = []

    # systemcommand
    classes.append(Pwd)
    classes.append(Cd)
    classes.append(Mkdir)
    classes.append(Rmdir)
    classes.append(Cp)

    for c in classes:
        suite = c.suite()
        unittest.TextTestRunner(resultclass=c.MyTestResult).run(suite)

if __name__ == "__main__":
    main()
