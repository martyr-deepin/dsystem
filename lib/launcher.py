#!/usr/bin/env python
#encoding:utf-8

import subprocess
from dogtail.tree import *
from window import *
from dde_dock import *
import pyautogui
pyautogui.FAILSAFE = False


class Launcher:
    def __init__(self):
    	self.launcherObj = root.application(appName='dde-launcher', description='/usr/bin/dde-launcher')
    	#self.launcherApps = self.launcherObj.child('all',roleName='list').children


    def getIconCoorFree(self,icon):
        coor = []
        position = self.launcherObj.child(icon).position
        size = self.launcherObj.child(icon).size
        coor.append(position[0]+size[0]/2)
        coor.append(position[1]+size[1]/2)
        return coor

    def getIconCoorCategory(self,icon):
        coor = []
        position = self.launcherObj.child('chat',roleName='list').children[0].position
        size = self.launcherObj.child('chat',roleName='list').children[0].size
        coor.append(position[0]+size[0]/2)
        coor.append(position[1]+size[1]/2)
        return coor

    def getLauncherAllApps(self):
        apps = []
        for i in range(len(self.launcherObj.child('all',roleName='list').children)):
            apps.append(self.launcherObj.child('all',roleName='list').children[i].name)
        return apps

    def getAppSize(self,app):
		return self.launcherObj.child(app).size

    def dragAppToDockFree(self):
        self.freeMode()
        app = Dock().getLastItemName()
        app_coor = Dock().getAppCoor(app)
        pyautogui.press('winleft')
        launcher = findWindow('dde-launcher')
        if launcher != None:
            icon_coor = self.getIconCoorFree('QQ')
            pyautogui.mouseDown(icon_coor[0], icon_coor[1])
            pyautogui.dragTo(app_coor[0], app_coor[1], duration=2)
            self.exitLauncher()

    def dragAppToDockCategory(self,listName):
        self.categoryMode()
        app = Dock().getLastItemName()
    	app_coor = Dock().getAppCoor(app)
    	pyautogui.press('winleft')
    	launcher = findWindow('dde-launcher')
        if launcher != None:
            QQName = self.launcherObj.child(listName,roleName='list').children[0].name
            print QQName
            icon_coor = self.getIconCoorCategory(QQName)
            pyautogui.mouseDown(icon_coor[0], icon_coor[1])
            pyautogui.dragTo(app_coor[0], app_coor[1], duration=2)
            self.exitLauncher()

    def unDock(self):
        app_coor = Dock().getAppCoor('QQ')
        center_coor = pyautogui.size()
        pyautogui.mouseDown(app_coor[0], app_coor[1])
        pyautogui.dragTo(center_coor[0]/2, center_coor[1]/2, duration=2)

    def exitLauncher(self):
        launcher = findWindow('dde-launcher')
        if launcher != None:
            pyautogui.press('esc')

    def getLauncherMode(self):
    	mode = subprocess.check_output(["gsettings get com.deepin.dde.launcher display-mode"],shell=True).decode().split("\n")
    	mode = [ n for n in mode if len(n.strip()) > 0]
    	mode = ''.join(mode)
    	return mode

    def freeMode(self):
        mode = self.getLauncherMode()
        print mode
        win = findWindow('dde-launcher')
        if mode == '\'category\'' and win == None:
            pyautogui.press('winleft')
            launcher = findWindow('dde-launcher')
            if launcher != None:
                self.launcherObj.child('mode-toggle-button').click()
                self.exitLauncher()

    def categoryMode(self):
        mode = self.getLauncherMode()
        print mode
        win = findWindow('dde-launcher')
        if mode == '\'free\'' and win == None:
            pyautogui.press('winleft')
            launcher = findWindow('dde-launcher')
            if launcher != None:
                self.launcherObj.child('mode-toggle-button').click()
                self.exitLauncher()

    def dragToCenterLeftKey(self):
        pyautogui.press('winleft')
        launcher = findWindow('dde-launcher')
        if launcher != None:
            apps = self.getLauncherAllApps()
            first = apps[0]
            center = apps[17]
            first_size = self.getAppSize(first)
            center_size = self.getAppSize(center)
            first_position = self.launcherObj.child(first).position
            center_position = self.launcherObj.child(center).position
            first_position_x = first_position[0]+first_size[0]/2
            first_position_y = first_position[1]+first_size[1]/2
            center_position_x = center_position[0]+center_size[0]/2
            center_position_y = center_position[1]+center_size[1]/2


            pyautogui.mouseDown(first_position_x, first_position_y)
            pyautogui.dragTo(center_position_x, center_position_y, duration=2)
            self.exitLauncher()

    def dragToFirstLeftKey(self):
        pyautogui.press('winleft')
        launcher = findWindow('dde-launcher')
        if launcher != None:
            apps = self.getLauncherAllApps()
            first = apps[0]
            center = apps[17]
            first_size = self.getAppSize(first)
            center_size = self.getAppSize(center)
            first_position = self.launcherObj.child(first).position
            center_position = self.launcherObj.child(center).position
            first_position_x = first_position[0]+first_size[0]/2
            first_position_y = first_position[1]+first_size[1]/2
            center_position_x = center_position[0]+center_size[0]/2
            center_position_y = center_position[1]+center_size[1]/2


            pyautogui.mouseDown(center_position_x, center_position_y)
            pyautogui.dragTo(first_position_x, first_position_y, duration=2)
            self.exitLauncher()

    def dragToCenterRightKey(self):
        pyautogui.press('winleft')
        launcher = findWindow('dde-launcher')
        if launcher != None:
            apps = self.getLauncherAllApps()
            first = apps[0]
            center = apps[17]
            first_size = self.getAppSize(first)
            center_size = self.getAppSize(center)
            first_position = self.launcherObj.child(first).position
            center_position = self.launcherObj.child(center).position
            first_position_x = first_position[0]+first_size[0]/2
            first_position_y = first_position[1]+first_size[1]/2
            center_position_x = center_position[0]+center_size[0]/2
            center_position_y = center_position[1]+center_size[1]/2

            pyautogui.mouseDown(first_position_x, first_position_y, 3)
            pyautogui.dragTo(center_position_x, center_position_y, duration=2, button='right')
            #self.exitLauncher()





launcher = Launcher()
