#!/usr/bin/env python
#encoding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf8')

from dogtail.tree import *

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
		apps = []
		for i in range(len(self.dockObj.child('dock-mainpanel').children)):
			apps.append(self.dockObj.child('dock-mainpanel').children[i].name)
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
