#!/usr/bin/env python3
#  -*- coding: utf-8 -*-

from dogtail.tree import *
from lib import utils
import time
import dbus

class Dde_control_center:
    def __init__(self):
        self.dccObj = root.application(appName='dde-control-center', description='/usr/bin/dde-control-center')
        self.dbus_name = 'com.deepin.dde.ControlCenter'
        self.obj_path = '/com/deepin/dde/ControlCenter'
        self.interface = 'com.deepin.dde.ControlCenter'

    def getDccIfc(self):
        dcc_obj = dbus.SessionBus().get_object(Dde_control_center().dbus_name, Dde_control_center().obj_path)
        return dbus.Interface(dcc_obj, dbus_interface=self.interface)

    def showDcc(self):
        dcc_ifc = self.getDccIfc()
        dcc_ifc.Show()

    def showModule(self, name):
        dcc_ifc = self.getDccIfc()
        dcc_ifc.ShowModule(name)

    def hideDcc(self):
        dcc_ifc = self.getDccIfc()
        dcc_ifc.Hide()

    def moveAllSettingsDown(self):
        allsettings_string = 'All Settings'
        allsettings = self.dccObj.child(allsettings_string)
        if None == allsettings:
            return False

        x, y = utils.getWidgetCenterPoint(allsettings)
        utils.m.move(x, y + 50)
        time.sleep(2)
        return True

    def clickBack(self):
        backBtn = self.dccObj.child('Back')
        backBtn.click()

    def clickScreenCenter(self):
        utils.m.move(int(utils.resolution.width/2),
                int(utils.resolution.height/2))

    def openGUI(self):
        utils.m.move(utils.resolution.width - 1, utils.resolution.height - 1)
        time.sleep(3)
        return True

    def openModule(self, modulename = None):
        if None == modulename:
            return False

        quickSwitchAllSettings = self.dccObj.child('QuickSwitchAllSettings')
        quickSwitchAllSettings.click()

        module = self.dccObj.child(modulename)
        if None == module:
            return False

        if False == self.moveAllSettingsDown():
            return False

        while True:
            module = self.dccObj.child(modulename)

            if module.position[1] > 70 \
                    and module.position[1] < utils.resolution.height/2:
                return True
            elif module.position[1] <= 70:
                utils.m.scroll(vertical=1)
            elif module.position[1] >= utils.resolution.height/2:
                utils.m.scroll(vertical=-1)

class DefaultApplications:
    def __init__(self):
        self.dbus_dest      = 'com.deepin.api.Mime'
        self.dbus_objpath   = '/com/deepin/api/Manager'
        self.dbus_interface = 'com.deepin.api.Manager'
        self.defaultAppsCategory = ('Browser', 'Mail', 'Text', 'Music', 
                'Video', 'Picture', 'Terminal', 'CD_Audio', 'DVD_Video', 
                'MusicPlayer', 'Camera', 'Software')

        self.session_bus = dbus.SessionBus()
        self.session_obj = self.session_bus.get_object(self.dbus_dest,
                                                       self.dbus_objpath)
        self.interface_manager = dbus.Interface(self.session_obj,
                                                dbus_interface=self.dbus_interface)

    def GetDefaultApp(self, category):
        mimetype = self.getTypeByCategory(category)
        return self.interface_manager.GetDefaultApp(mimetype)

    def ListApps(self, category):
        mimetype = self.getTypeByCategory(category)
        return self.interface_manager.ListApps(mimetype)

    def getTypeByCategory(self, category):
        return self.getTypeListByCategory(category)[0]

    def getTypeListByCategory(self, category):
        return {
                'Browser': ["x-scheme-handler/http",
                            "x-scheme-handler/ftp",
                            "x-scheme-handler/https",
                            "text/html",
                            "text/xml",
                            "text/xhtml_xml",
                            "text/xhtml+xml"],

                'Mail': ["x-scheme-handler/mailto",
                         "message/rfc822",
                         "application/x-extension-eml",
                         "application/x-xpinstall"],

                'Text': ["text/plain"],

                'Music': ["audio/mpeg",
                         "audio/mp3",
                         "audio/x-mp3",
                         "audio/mpeg3",
                         "audio/x-mpeg-3",
                         "audio/x-mpeg",
                         "audio/flac",
                         "audio/x-flac",
                         "application/x-flac",
                         "audio/ape",
                         "audio/x-ape",
                         "application/x-ape",
                         "audio/ogg",
                         "audio/x-ogg",
                         "audio/musepack",
                         "application/musepack",
                         "audio/x-musepack",
                         "application/x-musepack",
                         "audio/mpc",
                         "audio/x-mpc",
                         "audio/vorbis",
                         "audio/x-vorbis",
                         "audio/x-wav",
                         "audio/x-ms-wma"],

                'Video': ["video/mp4",
                          "audio/mp4",
                          "audio/x-matroska",
                          "video/x-matroska",
                          "application/x-matroska",
                          "video/avi",
                          "video/msvideo",
                          "video/x-msvideo",
                          "video/ogg",
                          "application/ogg",
                          "application/x-ogg",
                          "video/3gpp",
                          "video/3gpp2",
                          "video/flv",
                          "video/x-flv",
                          "video/x-flic",
                          "video/mpeg",
                          "video/x-mpeg",
                          "video/x-ogm",
                          "application/x-shockwave-flash",
                          "video/x-theora",
                          "video/quicktime",
                          "video/x-ms-asf",
                          "application/vnd.rn-realmedia",
                          "video/x-ms-wmv"],

                'Picture': ["image/jpeg",
                            "image/pjpeg",
                            "image/bmp",
                            "image/x-bmp",
                            "image/png",
                            "image/x-png",
                            "image/tiff",
                            "image/svg+xml",
                            "image/x-xbitmap",
                            "image/gif",
                            "image/x-xpixmap"],

                'Terminal': ["application/x-terminal"],

                'CD_Audio': ["x-content/audio-cdda"],

                'DVD_Video': ["x-content/video-dvd"],

                'MusicPlayer': ["x-content/audio-player"],

                'Camera': ["x-content/image-dcf"],

                'Software': ["x-content/unix-software"]

        }.get(category, None)

class Appearance:
    def __init__(self):
        self.dbus_name  = "com.deepin.daemon.Appearance"
        self.obj_path   = "/com/deepin/daemon/Appearance"
        self.interface  = "com.deepin.daemon.Appearance"

        self.FontSize   = "FontSize"
        self.IconTheme  = "IconTheme"
        self.CursorTheme = "CursorTheme"
        self.MonospaceFont = "MonospaceFont"
        self.StandardFont = "StandardFont"


class Network:
    def __init__(self):
        self.dbus_name = "com.deepin.daemon.Network"
        self.obj_path = "/com/deepin/daemon/Network"
        self.interface = "com.deepin.daemon.Network"

        self.VpnEnabled = 'VpnEnabled'

class Mouse:
    def __init__(self):
        self.dbus_name = "com.deepin.daemon.InputDevices"
        self.obj_path = "/com/deepin/daemon/InputDevice/Mouse"
        self.interface = "com.deepin.daemon.InputDevice.Mouse"

        self.DoubleClick = 'DoubleClick'
        self.LeftHanded = 'LeftHanded'
        self.NaturalScroll = 'NaturalScroll'
        self.DisableTpad = 'DisableTpad'
        self.MotionAcceleration = 'MotionAcceleration'

class Timedate:
    def __init__(self):
        self.dbus_name = "com.deepin.daemon.Timedate"
        self.obj_path = "/com/deepin/daemon/Timedate"
        self.interface = "com.deepin.daemon.Timedate"

        self.UserTimezones = 'UserTimezones'
        self.CanNTP = 'CanNTP'
        self.LocalRTC = 'LocalRTC'
        self.NTP = 'NTP'
        self.Use24HourFormat = 'Use24HourFormat'
        self.DSTOffset = 'DSTOffset'
        self.Timezone = 'Timezone'

class Keyboard:
    def __init__(self):
        self.dbus_name  = "com.deepin.daemon.InputDevices"
        self.obj_path   = "/com/deepin/daemon/InputDevice/Keyboard"
        self.interface = "com.deepin.daemon.InputDevice.Keyboard"

        self.UserLayoutList = "UserLayoutList"
        self.CurrentLayout  = "CurrentLayout"
        self.CapslockToggle = 'CapslockToggle'
        self.RepeatDelay = 'RepeatDelay'
        self.RepeatInterval = 'RepeatInterval'

#dcc = Dde_control_center()
appearance = Appearance()
network = Network()
mouse = Mouse()
timedate = Timedate()
keyboard = Keyboard()

def getAppearanceProperty():
    appearance_obj = dbus.SessionBus().get_object(appearance.dbus_name,appearance.obj_path)
    return dbus.Interface(appearance_obj,dbus_interface=dbus.PROPERTIES_IFACE)

def getAppearanceWindowTheme():
    appearance_property = getAppearanceProperty()
    return appearance_property.Get(appearance.interface,appearance.GtkTheme)

def setAppearanceWindowTheme(windowtheme):
    appearance_property = getAppearanceProperty()
    return appearance_property.Set(appearance.interface, appearance.FontSize, windowtheme)

def getAppearanceFontSize():
    appearance_property = getAppearanceProperty()
    return appearance_property.Get(appearance.interface,appearance.FontSize)

def setAppearanceFontSize(fontsize):
    appearance_property = getAppearanceProperty()
    return appearance_property.Set(appearance.interface, appearance.FontSize, fontsize)

def getAppearanceIconTheme():
    appearance_property = getAppearanceProperty()
    return appearance_property.Get(appearance.interface,appearance.IconTheme)

def setAppearanceIconTheme(iconTheme):
    appearance_property = getAppearanceProperty()
    return appearance_property.Set(appearance.interface,appearance.IconTheme, iconTheme)

def getAppearanceCursorTheme():
    appearance_property = getAppearanceProperty()
    return appearance_property.Get(appearance.interface,appearance.CursorTheme)

def setAppearanceCursorTheme(cursorTheme):
    appearance_property = getAppearanceProperty()
    return appearance_property.Set(appearance.interface,appearance.CursorTheme, cursorTheme)

def getNetworkVpnEnabled():
    network_session = dbus.SessionBus().get_object(network.dbus_name, network.obj_path)
    network_property = dbus.Interface(network_session, dbus_interface=dbus.PROPERTIES_IFACE)
    return network_property.Get(network.interface,network.VpnEnabled)

def getMouseProperty():
    mouse_obj = dbus.SessionBus().get_object(mouse.dbus_name,mouse.obj_path)
    return dbus.Interface(mouse_obj,dbus_interface=dbus.PROPERTIES_IFACE)

def getMouseDoubleClick():
    mouse_property = getMouseProperty()
    return mouse_property.Get(mouse.interface, mouse.DoubleClick)

def getMouseLeftHanded():
    mouse_property = getMouseProperty()
    return mouse_property.Get(mouse.interface, mouse.LeftHanded)

def getMouseNaturalScroll():
    mouse_property = getMouseProperty()
    return mouse_property.Get(mouse.interface, mouse.NaturalScroll)

def getMouseDisableTpad():
    mouse_property = getMouseProperty()
    return mouse_property.Get(mouse.interface, mouse.DisableTpad)

def getMouseMotionAcceleration():
    mouse_property = getMouseProperty()
    return mouse_property.Get(mouse.interface, mouse.MotionAcceleration)

def getTimedateProperty():
    timedate_obj = dbus.SessionBus().get_object(timedate.dbus_name,timedate.obj_path)
    return dbus.Interface(timedate_obj,dbus_interface=dbus.PROPERTIES_IFACE)

def getTimedateTimezone():
    timedate_property = getTimedateProperty()
    return timedate_property.Get(timedate.interface, timedate.Timezone)

def getKeyboardProperty():
    keyboard_obj = dbus.SessionBus().get_object(keyboard.dbus_name,keyboard.obj_path)
    return dbus.Interface(keyboard_obj,dbus_interface=dbus.PROPERTIES_IFACE)

def getKeyboardCurrentLayout():
    keyboard_property = getKeyboardProperty()
    return keyboard_property.Get(keyboard.interface, keyboard.CurrentLayout)

def getKeyboardCapslockToggle():
    keyboard_property = getKeyboardProperty()
    return keyboard_property.Get(keyboard.interface, keyboard.CapslockToggle)

def getKeyboardRepeatDelay():
    keyboard_property = getKeyboardProperty()
    return keyboard_property.Get(keyboard.interface, keyboard.RepeatDelay)

def getKeyboardRepeatInterval():
    keyboard_property = getKeyboardProperty()
    return keyboard_property.Get(keyboard.interface, keyboard.RepeatInterval)

