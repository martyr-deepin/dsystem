#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest

from apps.testDeepinMovie import DeepinMovie
from apps.testDeepinMusic import DeepinMusic
from apps.testDeepinScreenShot import DeepinScreenshot
from apps.testDeepinStore import DeepinStore
from apps.testDeepinTerminal import DeepinTerminal
from apps.testYoudaoDict import YoudaoDict
from apps.testDeepinMovieHelp import DeepinMovieHelp

def main():
    classes = []
    classes.append(DeepinMovie)
    classes.append(DeepinMusic)
    classes.append(DeepinScreenshot)
    classes.append(DeepinStore)
    classes.append(DeepinTerminal)
    classes.append(YoudaoDict)
    classes.append(DeepinMovieHelp)

    for c in classes:
        unittest.TextTestRunner(resultclass=c.MyTestResult).run(c.suite())
if __name__ == '__main__':
    main()
