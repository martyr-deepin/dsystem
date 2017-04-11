#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import gettext
import unittest
from lib.executeTestCase import runTest

from dde_control_center import User_Head
from dde_control_center import Click_UserHead
from dde_control_center import Check_UserHead_Display
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

from dde_control_center import Accounts_AddMultiUserOperation
from dde_control_center import Accounts_AddUserCancel
from dde_control_center import Accounts_AddUserConfirmClipboard
from dde_control_center import Accounts_AddUserConfirm
from dde_control_center import Accounts_DefaultIcon
from dde_control_center import Accounts_Errortip
from dde_control_center import Accounts_ModifyUserIcon
from dde_control_center import Accounts_ModifyUserPasswordAccept
from dde_control_center import Accounts_ModifyUserPasswordCancel

def main():
    classes = []
    classes.append(User_Head)
    classes.append(Click_UserHead)
    classes.append(Check_UserHead_Display)
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

    classes.append(Accounts_AddMultiUserOperation)
    classes.append(Accounts_AddUserCancel)
    classes.append(Accounts_AddUserConfirmClipboard)
    classes.append(Accounts_AddUserConfirm)
    classes.append(Accounts_DefaultIcon)
    classes.append(Accounts_Errortip)
    classes.append(Accounts_ModifyUserIcon)
    classes.append(Accounts_ModifyUserPasswordAccept)
    classes.append(Accounts_ModifyUserPasswordCancel)

    for c in classes:
        runTest(c)

if __name__ == "__main__":
    unittest.installHandler()
    LOCALE_DIR = os.path.abspath("./lib/locale")
    gettext.install('dsystem', LOCALE_DIR)
    main()
