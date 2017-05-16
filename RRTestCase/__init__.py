__ALL__ = ['Launcher_StartAllAPP',
           'Launcher_SendToDesktop',
           'Launcher_AddToDock',
           'Launcher_AutoStart',
           'Launcher_Uninstall',
           'Dock_Exist',
           'Dock_DefaultSetting',
           'Dock_ChangeDisplay',
           'Dock_DragDockiconToDel',
           'DCC_Click_LightSlider',
           'DCC_Click_SoundSlider',
           'DCC_ShowModules'
           ]

from .testLauncher_StartAllAPP import Launcher_StartAllAPP
from .testLauncher_SendToDesktop import Launcher_SendToDesktop
from .testLauncher_AddToDock import Launcher_AddToDock
from .testLauncher_AutoStart import Launcher_AutoStart
from .testLauncher_Uninstall import Launcher_Uninstall

from .testDock_Exist import Dock_Exist
from .testDock_DefaultSetting import Dock_DefaultSetting
from .testDock_ChangeDisplay import Dock_ChangeDisplay
from .testDock_DragDockiconToDel import Dock_DragDockiconToDel

from .testDCC_ClickLightslider  import DCC_Click_LightSlider
from .testDCC_ClickSoundslider  import DCC_Click_SoundSlider
from .testDCC_ShowAllModules  import DCC_ShowModules
