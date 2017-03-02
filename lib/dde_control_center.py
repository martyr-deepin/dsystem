#!/usr/bin/env python3
#  -*- coding: utf-8 -*-

from dogtail.tree import *
from lib import utils
import time
import dbus
from lib import dde_dock
from lib import polkit_agent
import pyautogui
import gettext
import pyperclip

class Dde_control_center:
    def __init__(self):
        self.defaultDelay = 5

        self.dccObj = root.application(appName='dde-control-center', description='/usr/bin/dde-control-center')
        self.dbus_name = 'com.deepin.dde.ControlCenter'
        self.obj_path = '/com/deepin/dde/ControlCenter'
        self.interface = 'com.deepin.dde.ControlCenter'

        self.session_bus = dbus.SessionBus()
        self.session_obj = self.session_bus.get_object(self.dbus_name,
                                                       self.obj_path)

        self.interface_properties = dbus.Interface(self.session_obj,
                                                   dbus_interface=dbus.PROPERTIES_IFACE)

        self.interface_methods = dbus.Interface(self.session_obj,
                                                dbus_interface=self.interface)

        self.dbus_properties_ShowInRight = "ShowInRight"
        self.dbus_properties_Rect = "Rect"

        self.FRAME_WIDTH = 360

        # 标识控制中心点开模块的深度
        self.page_deep = 0

        # 控制中心首页
        self.string_PrevBtn = _('PrevBtn')
        self.string_NextBtn = _('NextBtn')
        self.string_SoundSlider = _('SoundSlider')
        self.string_LightSlider = _('LightSlider')
        self.string_QuickSwitchAllSettings = _('QuickSwitchAllSettings')

        # 控制中心 All Settings
        self.string_Back = _('Back')
        self.string_All_Setting = _('All Settings')

        self.string_Accounts = _('Accounts')
        self.string_Create_Account = _('Create Account')

        self.string_Display = _('Display')
        self.string_Resolution = _('Resolution')
        self.string_Rotate = _('Rotate')

        self.string_Default_Applications = _('Default Applications')
        self.string_Personalization = _('Personalization')
        self.string_Network = _('Network')
        self.string_Sound = _('Sound')
        self.string_Time_and_Date = _('Time and Date')
        self.string_Power_Management = _('Power Management')
        self.string_Mouse_and_Touchpad = _('Mouse and Touchpad')
        self.string_Keyboard_and_Language = _('Keyboard and Language')
        self.string_Update = _('Update')
        self.string_System_Information = _('System Information')

        # 账户
        self.string_Modify_Avatar = _('Modify Avatar')
        self.string_Modify_Password = _('Modify Password')
        self.string_Auto_login = _('Auto Login')
        self.string_Delete_Account = _('Delete Account')
        self.string_NewAccount_Username = _('Username')
        self.string_NewAccount_Password = _('Password')
        self.string_NewAccount_Repeat_password = _('Repeat password')
        self.string_NewAccount_Cancel = 'New_Account_Cancel'
        self.string_NewAccount_Create = 'New_Account_Create'
        self.string_NewAccount_errorTip = 'New_Account_errorTip'
        self.string_NewAccount_errorTip_Password = _("Password can't be empty.")
        self.string_NewAccount_errorTip_Username = _("Username can not be empty.")

        # 默认程序
        self.string_Browser = _('Browser')
        self.string_Mail = _('Mail')
        self.string_Text = _('Text')
        self.string_Music = _('Music')
        self.string_Video = _('Video')
        self.string_Picture = _('Picture')
        self.string_Terminal = _('Terminal')
        self.string_CD_Audio = _('CD Audio')
        self.string_DVD_Video = _('DVD Video')
        self.string_Music_Player = _('Music Player')
        self.string_Camera = _('Camera')
        self.string_Software = _('Software')

    def showDcc(self):
        waittime = 5
        self.interface_methods.Show()

        while waittime:
            time.sleep(1)
            waittime = waittime - 1
            rect = self.getRect()
            if self.FRAME_WIDTH == rect[2]:
                return True

        return False

    def showModule(self, name):
        """Show dde-control-center module

        modules name were listed bellow:
        accounts
        display
        defapp
        personalization
        network
        bluetooth
        sound
        datetime
        power
        mouse
        keyboard
        wacom
        update
        systeminfo
        """
        self.interface_methods.ShowModule(name)
        waittime = self.defaultDelay

        while waittime:
            time.sleep(1)
            waittime = waittime - 1
            rect = self.getRect()
            if self.FRAME_WIDTH == rect[2]:
                return True

        return False

    def hideDcc(self):
        waittime = self.defaultDelay
        self.interface_methods.Hide()

        while waittime:
            time.sleep(1)
            waittime = waittime - 1
            rect = self.getRect()
            if 0 == rect[2]:
                return True

        return False

    def getShowInRight(self):
        return self.interface_properties.Get(self.interface, 
                                      self.dbus_properties_ShowInRight)

    def getRect(self):
        return self.interface_properties.Get(self.interface, 
                                      self.dbus_properties_Rect)

    def moveAllSettingsDown(self):
        allsettings_string = _('All Settings')
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
        time.sleep(1)
        utils.m.click(int(utils.resolution.width/2),
                int(utils.resolution.height/2))

        waittime = self.defaultDelay

        while waittime:
            time.sleep(1)
            waittime = waittime - 1
            rect = self.getRect()
            if 0 == rect[2]:
                return True

        return False

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

            if module.position[1] > 50 \
                    and module.position[1] < utils.resolution.height/2:
                return True
            elif module.position[1] <= 50:
                utils.m.scroll(vertical=1)
            elif module.position[1] >= utils.resolution.height/2:
                utils.m.scroll(vertical=-1)

    def backToIndex(self):
        for i in range(self.page_deep):
            utils.m.move(utils.resolution.width - 340, 20)
            time.sleep(1)
            utils.m.click(utils.resolution.width - 340, 20)
            time.sleep(2)

    def exit(self):
        self.clickScreenCenter()
        time.sleep(2)

    def addUser(self, username, password, operation):
        widget_username = self.dccObj.child(self.string_NewAccount_Username)
        widget_password = self.dccObj.child(self.string_NewAccount_Password)
        widget_repeat_password = self.dccObj.child(self.string_NewAccount_Repeat_password)

        widget_username.click()
        utils.keyTypeString(username)
        widget_password.click()
        utils.keyTypeString(password)
        widget_repeat_password.click()
        utils.keyTypeString(password)

        if operation == self.string_NewAccount_Cancel:
            widget_cancel = self.dccObj.child(self.string_NewAccount_Cancel, roleName='push button')
            widget_cancel.click()
            self.page_deep -= 1
        elif operation == self.string_NewAccount_Create:
            widget_create = self.dccObj.child(self.string_NewAccount_Create, roleName='push button')
            widget_create.click()
            polkit_agent.do_polkit_agent()
            self.page_deep -= 1

    def addUserClipboard(self, username, password, operation):
        widget_username = self.dccObj.child(self.string_NewAccount_Username)
        widget_password = self.dccObj.child(self.string_NewAccount_Password)
        widget_repeat_password = self.dccObj.child(self.string_NewAccount_Repeat_password)

        widget_username.click()
        pyperclip.copy(username)
        utils.keyCtrlV()
        widget_password.click()
        pyperclip.copy(password)
        utils.keyCtrlV()
        widget_repeat_password.click()
        pyperclip.copy(password)
        utils.keyCtrlV()

        if operation == self.string_NewAccount_Cancel:
            widget_cancel = self.dccObj.child(self.string_NewAccount_Cancel, roleName='push button')
            widget_cancel.click()
            self.page_deep -= 1
        elif operation == self.string_NewAccount_Create:
            widget_create = self.dccObj.child(self.string_NewAccount_Create, roleName='push button')
            widget_create.click()
            polkit_agent.do_polkit_agent()
            self.page_deep -= 1


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

class User():
    def __init__(self, dbus_objpath):
        self.dbus_dest = 'com.deepin.daemon.Accounts'
        self.dbus_objpath = dbus_objpath
        self.dbus_interface = 'com.deepin.daemon.Accounts.User'

        self.system_bus = dbus.SystemBus()
        self.system_obj = self.system_bus.get_object(self.dbus_dest,
                                                     self.dbus_objpath)
        self.interface_properties = dbus.Interface(self.system_obj,
                                                   dbus_interface=dbus.PROPERTIES_IFACE)
        self.dbus_properties_UserName = "UserName"

    def getPropertiesUserName(self):
        return self.interface_properties.Get(self.dbus_interface,
                                             self.dbus_properties_UserName)

class Accounts():
    def __init__(self):
        self.dbus_dest  = 'com.deepin.daemon.Accounts'
        self.dbus_objpath = '/com/deepin/daemon/Accounts'
        self.dbus_interface = 'com.deepin.daemon.Accounts'

        self.system_bus = dbus.SystemBus()
        self.system_obj = self.system_bus.get_object(self.dbus_dest,
                                                     self.dbus_objpath)
        self.interface_properties = dbus.Interface(self.system_obj,
                                                   dbus_interface=dbus.PROPERTIES_IFACE)

        self.dbus_properties_UserList = "UserList"
        self.dbus_properties_GuestIcon = "GuestIcon"

    def getPropertiesUserList(self):
        return self.interface_properties.Get(self.dbus_interface,
                                             self.dbus_properties_UserList)

    def getPropertiesGuestIcon(self):
        return self.interface_properties.Get(self.dbus_interface,
                                             self.dbus_properties_GuestIcon)
    def getDeepinAllUserName(self):
        UserList = self.getPropertiesUserList()
        UserNameList = []
        for path in UserList:
            user = User(path)
            UserName = user.getPropertiesUserName()
            UserNameList.append(UserName)

        return UserNameList

class Display:
    def __init__(self):
        self.dbus_dest = 'com.deepin.daemon.Display'
        self.dbus_objpath = '/com/deepin/daemon/Display'
        self.dbus_interface = 'com.deepin.daemon.Display'

        self.session_bus = dbus.SessionBus()
        self.session_obj = self.session_bus.get_object(self.dbus_dest,
                                                       self.dbus_objpath)
        self.interface_method = dbus.Interface(self.session_obj,
                                               dbus_interface=self.dbus_interface)
        self.interface_properties = dbus.Interface(self.session_obj,
                                                   dbus_interface=dbus.PROPERTIES_IFACE)

        self.dbus_properties_primary = 'Primary'
        self.dbus_properties_monitors = 'Monitors'
        self.primary_ext = '/com/deepin/daemon/Display/Monitor'

    def getPropertiesPrimary(self):
        return self.interface_properties.Get(self.dbus_interface,
                                             self.dbus_properties_primary)

    def getPropertiesMonitors(self):
        return self.interface_properties.Get(self.dbus_interface,
                                             self.dbus_properties_monitors)

    def ListOutputNames(self):
        return self.interface_method.ListOutputNames()

    def getPrimaryPath(self):
        monitors = self.getPropertiesMonitors()
        primary = self.getPropertiesPrimary()

        for m in monitors:
            if m.endswith(primary):
                return m

        return None

class Appearance:
    def __init__(self):
        self.dbus_name  = "com.deepin.daemon.Appearance"
        self.obj_path   = "/com/deepin/daemon/Appearance"
        self.interface  = "com.deepin.daemon.Appearance"

        self.GtkTheme = 'GtkTheme'
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

class TouchPad:
    def __init__(self):
        self.dbus_name = 'com.deepin.daemon.InputDevices'
        self.obj_path = "/com/deepin/daemon/InputDevice/TouchPad"
        self.interface = "com.deepin.daemon.InputDevice.TouchPad"

        self.DisableIfTyping = 'DisableIfTyping'

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

def getTouchPadProperty():
    touchpad_obj = dbus.SessionBus().get_object(touchpad.dbus_name,touchpad.obj_path)
    return dbus.Interface(touchpad_obj,dbus_interface=dbus.PROPERTIES_IFACE)

def getTouchPadDisableIfTyping():
    touchpad_property = getTouchPadProperty()
    return touchpad_property.Get(touchpad.interface, touchpad.DisableIfTyping)
