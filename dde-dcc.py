#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import gettext
import unittest
from lib.executeTestCase import runTest

from dde_control_center import Accounts_UI
from dde_control_center import Display_UI
from dde_control_center import DefaultApplications_UI
from dde_control_center import Personalization_UI
from dde_control_center import Network_UI
from dde_control_center import Sound_UI
from dde_control_center import TimeDate_UI
from dde_control_center import PowerManagement_UI
from dde_control_center import MouseTouchpad_UI
from dde_control_center import KeyboardLanguage_UI
from dde_control_center import Update_UI
from dde_control_center import SystemInformation_UI

def main():
    classes = []

    classes.append(Accounts_UI)
    classes.append(Display_UI)
    classes.append(DefaultApplications_UI)
    classes.append(Personalization_UI)
    classes.append(Network_UI)
    classes.append(Sound_UI)
    classes.append(TimeDate_UI)
    classes.append(PowerManagement_UI)
    classes.append(MouseTouchpad_UI)
    classes.append(KeyboardLanguage_UI)
    classes.append(Update_UI)
    classes.append(SystemInformation_UI)

    for c in classes:
        runTest(c)

if __name__ == "__main__":
    unittest.installHandler()
    LOCALE_DIR = os.path.abspath("./lib/locale")
    gettext.install('dsystem', LOCALE_DIR)
    main()
