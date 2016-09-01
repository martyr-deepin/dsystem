#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from dogtail.tree import *
import subprocess
import pyautogui

class Dock:
	def __init__(self):
		self.dockObj = root.application(appName='dde-dock', description='/usr/bin/dde-dock')
		#self.dockedapps = self.dockObj.child('dock-mainpanel').children

	def getDockedApps(self):
		apps = []
		for i in range(len(self.dockObj.child('dock-mainpanel').children)):
			if self.dockObj.child('dock-mainpanel').children[i].name == '':
				break
			apps.append(self.dockObj.child('dock-mainpanel').children[i].name)
		return apps

	def getAllDockApps(self):
		'''
		apps = []
		for i in range(len(self.dockObj.child('dock-mainpanel').children)):
			apps.append(self.dockObj.child('dock-mainpanel').children[i].name)
		return apps
		'''
		apps = subprocess.check_output(["gsettings get com.deepin.dde.dock docked-apps"],shell=True).decode().split("\n")
		apps = [ n for n in apps if len(n.strip()) > 0]
		apps = ''.join(apps)
		return apps

	def getAppCoor(self,app):
		coor = []
		position = self.dockObj.child(app).position
		size = self.dockObj.child(app).size
		coor.append(position[0]+size[0]/2)
		coor.append(position[1]+size[1]/2)
		return coor

	def getLastItemName(self):
		apps = self.getDockedApps()
		return self.dockObj.child('dock-mainpanel').children[len(apps)-1].name

	def unDockApp(self,app):
		app_coor = self.getAppCoor(app)
		center_coor = pyautogui.size()
		pyautogui.mouseDown(app_coor, duration=2, pause=1)
		pyautogui.dragTo(center_coor[0]/2, center_coor[1]/2, duration=2)
