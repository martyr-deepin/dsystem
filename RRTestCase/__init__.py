__ALL__ = ['Launcher_StartAllAPP',
           'Launcher_SendToDesktop',
           'Launcher_AddToDock',
           'Launcher_AutoStart',
           'Launcher_Uninstall',
           'Dock_Exist',
           'Dock_DefaultSetting',
           'Dock_ChangeDisplay',
           'Dock_ChangePosition',
           'Dock_ChangeIconSize',
           'Dock_ChangeHide',
           'Dock_DragDockiconToDel',
           'DCC_Click_LightSlider',
           'DCC_Click_SoundSlider',
           'DCC_ShowModules',
           'Command_useradd',
           'Command_userdel',
           'Command_passwd',
           'Command_pwd',
           'Command_cd',
           'Command_mkdir',
           'Command_rmdir',
           'Command_cp',
           'Command_mv',
           'Command_rm',
           'Command_file',
           'Command_find',
           'Command_grep',
           'Command_chown',
           'Command_sort',
           'Command_wc',
           'Command_ifconfig',
           'Command_ping',
           'Command_ping_ip',
           'Command_ping_local_ip',
           'Command_netstat_i',
           'Command_netstat_r',
           'Command_telnet',
           'Command_traceroute',
           ]

from .testLauncher_StartAllAPP import Launcher_StartAllAPP
from .testLauncher_SendToDesktop import Launcher_SendToDesktop
from .testLauncher_AddToDock import Launcher_AddToDock
from .testLauncher_AutoStart import Launcher_AutoStart
from .testLauncher_Uninstall import Launcher_Uninstall

from .testDock_Exist import Dock_Exist
from .testDock_DefaultSetting import Dock_DefaultSetting
from .testDock_ChangeDisplay import Dock_ChangeDisplay
from .testDock_ChangePosition import Dock_ChangePosition
from .testDock_ChangeIconSize import Dock_ChangeIconSize
from .testDock_ChangeHide import Dock_ChangeHide
from .testDock_DragDockiconToDel import Dock_DragDockiconToDel

from .testDCC_ClickLightslider  import DCC_Click_LightSlider
from .testDCC_ClickSoundslider  import DCC_Click_SoundSlider
from .testDCC_ShowAllModules  import DCC_ShowModules

from .testCommand_useradd import Command_useradd
from .testCommand_userdel import Command_userdel
from .testCommand_passwd import Command_passwd
from .testCommand_pwd import Command_pwd
from .testCommand_cd import Command_cd
from .testCommand_mkdir import Command_mkdir
from .testCommand_rmdir import Command_rmdir
from .testCommand_cp import Command_cp
from .testCommand_mv import Command_mv
from .testCommand_rm import Command_rm
from .testCommand_file import Command_file
from .testCommand_find import Command_find
from .testCommand_grep import Command_grep
from .testCommand_chown import Command_chown
from .testCommand_sort import Command_sort
from .testCommand_wc import Command_wc
from .testCommand_ifconfig import Command_ifconfig
from .testCommand_ping import Command_ping
from .testCommand_ping_ip import Command_ping_ip
from .testCommand_ping_local_ip import Command_ping_local_ip
from .testCommand_netstat_i import Command_netstat_i
from .testCommand_netstat_r import Command_netstat_r
from .testCommand_telnet import Command_telnet
from .testCommand_traceroute import Command_traceroute
