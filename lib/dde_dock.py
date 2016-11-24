#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from dogtail.tree import *
import subprocess
import pyautogui
from time import sleep
from lib import utils
import re

class Dock:
	def __init__(self):
		self.dockObj = root.application(appName='dde-dock', description='/usr/bin/dde-dock')
		#self.dockedapps = self.dockObj.child('dock-mainpanel').children

	def getDockedApps(self):
		apps = []
		for i in range(len(self.dockObj.child('dock-mainpanel').children)):
			#if self.dockObj.child('dock-mainpanel').children[i].name == '':
			#	break
			apps.append(self.dockObj.child('dock-mainpanel').children[i].name)
		return apps

	def getAllApps(self):
		sleep(5)
		apps = []
		for i in range(len(self.dockObj.child('dock-mainpanel').children)):
			apps.append(self.dockObj.child('dock-mainpanel').children[i].name)
		return apps

	def getAllDockApps(self):
		'''
		apps = []
		for i in range(len(self.dockObj.child('dock-mainpanel').children)):
			apps.append(self.dockObj.child('dock-mainpanel').children[i].name)
		return apps
		'''
		apps = subprocess.getoutput("gsettings get com.deepin.dde.dock docked-apps")
		apps = re.sub('[@\/S\'\[\]]', '', apps)
		apps = apps.split(', ')
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

	def getDockDestCoor(self):
		coor = []
		apps = self.getDockedApps()
		first = self.dockObj.child('dock-mainpanel').children[0].name
		second = self.dockObj.child('dock-mainpanel').children[1].name
		first_coor = self.getAppCoor(first)
		second_coor = self.getAppCoor(second)
		dock_position = utils.getDdeDockPosition()
		if dock_position == 0 or dock_position == 2:
			x = first_coor[0] + (second_coor[0] - first_coor[0])/2
			y = first_coor[1]
			coor.append(x)
			coor.append(y)
		if dock_position == 1 or dock_position == 3:
			x = first_coor[0]
			y = first_coor[1] + (second_coor[1] - first_coor[1])/2
			coor.append(x)
			coor.append(y)
		return coor 


	def unDockApp(self,app):
		app_coor = self.getAppCoor(app)
		center_coor = pyautogui.size()
		pyautogui.mouseDown(app_coor, duration=2, pause=1)
		pyautogui.dragTo(center_coor[0]/2, center_coor[1]/2, duration=2)

	def dragInDock(self,src,dest):
		srcCoor = self.getAppCoor(src)
		destCoor = self.getAppCoor(dest)
		mouseDrag(srcCoor,destCoor)


def mouseDrag(s,d):
	pyautogui.mouseDown(s,pause=1)
	pyautogui.moveTo(d,duration=1)
	pyautogui.mouseUp(d)


if __name__ == '__main__':
	dock = Dock()
	apps = dock.getAllDockApps()
	print(apps)
