#!/usr/bin/env python

from dogtail.tree import *
from dogtail.utils import *
import sys

def writePCDataElement(content):
    print('%s' % content)

def generateUnhelpfulHelp(appName):
    try:
        path = '/usr/bin/' + appName
        app = root.application(appName, description=path)
    except SearchError:
        run(appName)

    menus = app.findChildren(predicate.GenericPredicate(name='dockSettingsMenu', roleName="popup menu"))
    for menu in menus:
        items = menu.findChildren(predicate.GenericPredicate(roleName="menu item"))
        if items!=None:
            for item in items:
                verb = item.name
                writePCDataElement("%s"%(verb.title()))

if __name__=='__main__':
    try:
        generateUnhelpfulHelp(sys.argv[1])
    except IndexError:
        print("####################################")
        print("please supply an application name on the cmdline")
        print("####################################")
