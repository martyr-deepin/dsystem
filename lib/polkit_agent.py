#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from lib import window
from lib import utils
from dogtail.tree import root

def do_polkit_agent(pw = 'deepin'):
    app_name = 'Deepin Polkit Agent'
    polkit_agent = window.WindowState(app_name)
    win_polkit_agent = polkit_agent.getWindow()

    if None == win_polkit_agent:
        print("Window: %s does not exist." % app_name)
    else:
        dogtail_agent = root.application('dde-polkit-agent',
                '/usr/lib/polkit-1-dde/dde-polkit-agent')
        PasswordInput = dogtail_agent.child('PasswordInput')
        PasswordInput.click()
        utils.keyTypeString(pw)
        Comfirm = dogtail_agent.child('Confirm')
        Comfirm.click()

