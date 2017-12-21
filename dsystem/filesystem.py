#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest

from compatibility.testExt2 import FilesystemExt2
from compatibility.testExt3 import FilesystemExt3
#from compatibility.testNtfs import FilesystemNtfs
from compatibility.testFat32 import FilesystemFat32
#from compatibility.testBtrfs import FilesystemBtrfs
from compatibility.testReiserfs import FilesystemReiserfs
from compatibility.testXfs import FilesystemXfs


def main():
    classes = []
    classes.append(FilesystemExt2)
    classes.append(FilesystemExt3)
    #classes.append(FilesystemNtfs)
    classes.append(FilesystemFat32)
    #classes.append(FilesystemBtrfs)
    classes.append(FilesystemReiserfs)
    classes.append(FilesystemXfs)


    for c in classes:
        unittest.TextTestRunner(resultclass=c.MyTestResult).run(c.suite())
if __name__ == '__main__':
    main()
