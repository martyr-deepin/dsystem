#!/usr/bin/env python
#encoding:utf-8

import subprocess
from dogtail.tree import *
from window import *
from dde_dock import *
import pyautogui
pyautogui.FAILSAFE = False
pyautogui.PAUSE = 1

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

    def getIconCoorCategory(self,lst):
        coor = []
        position = self.launcherObj.child(lst,roleName='list').children[0].position
        size = self.launcherObj.child(lst,roleName='list').children[0].size
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
            icon_coor = self.getIconCoorCategory('chat')
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

    def dragSrcToDest(self, s, d, btn='left'):
        pyautogui.press('winleft')
        launcher = findWindow('dde-launcher')
        if launcher != None:
            apps = self.getLauncherAllApps()
            src = apps[s]
            dest = apps[d]
            src_size = self.getAppSize(src)
            dest_size = self.getAppSize(dest)
            src_position = self.launcherObj.child(src).position
            dest_position = self.launcherObj.child(dest).position
            src_x = src_position[0]+src_size[0]/2
            src_y = src_position[1]+src_size[1]/2
            dest_x = dest_position[0]+dest_size[0]/2
            dest_y = dest_position[1]+dest_size[1]/2
            print src_x,src_y
            if src_y<0:
                pyautogui.scroll(30)
            pyautogui.mouseDown(src_x, src_y, button=btn)
            if d>27:
                pyautogui.scroll(-30)
                pyautogui.dragTo(dest_x, dest_y, duration=6, button=btn)
            pyautogui.dragTo(dest_x, dest_y, duration=2, button=btn)

    def dragToCenterLeftKey(self):
        self.dragSrcToDest(0, 17)
        self.exitLauncher()

    def dragToFirstLeftKey(self):
        self.dragSrcToDest(17, 0)
        self.exitLauncher()

    def dragToCenterRightKey(self):
        self.dragSrcToDest(0, 17, 'right')

    def dragToSecond(self):
        self.dragSrcToDest(0, 1)
        self.exitLauncher()

    def dragToFirstRowEnd(self):
        self.dragSrcToDest(0, 6)
        self.exitLauncher()

    def dragToFirstColumnEnd(self):
        columnEndIndex = self.getColumnEndIndex()
        self.dragSrcToDest(0, columnEndIndex)
        self.exitLauncher()

    def dragToEnd(self):
        endIndex = len(self.launcherObj.child('all',roleName='list').children)
        self.dragSrcToDest(0, endIndex-1)
        self.exitLauncher()

    def getColumnEndIndex(self):
        nums = len(self.launcherObj.child('all',roleName='list').children)
        left = nums%7
        clumns = nums/7
        if left !=0:
            return clumns*7
        else:
            return (clumns-1)*7

    def disableDrag(self):
        self.categoryMode()
        win = findWindow('dde-launcher')
        if win == None:
            pyautogui.press('winleft')
            googleCoor = self.getIconCoorCategory('internet')
            musicCoor = self.getIconCoorCategory('music')
            pyautogui.mouseDown(googleCoor)
            pyautogui.dragTo(musicCoor, duration=2)
            self.exitLauncher()

launcher = Launcher()
