__ALL__ = ['Launcher_StartAllAPP',
           'Launcher_SendToDesktop',
           'Launcher_AddToDock',
           'Launcher_AutoStart',
           'Dock_DragDockiconToDel',
           'DCC_Click_LightSlider',
           'DCC_Click_SoundSlider',
           'DCC_ShowModules'
           ]

from .testLauncher_StartAllAPP import Launcher_StartAllAPP
from .testLauncher_SendToDesktop import Launcher_SendToDesktop
from .testLauncher_AddToDock import Launcher_AddToDock
from .testLauncher_AutoStart import Launcher_AutoStart

from .testDock_DragDockiconToDel import Dock_DragDockiconToDel

from .testDCC_ClickLightslider  import DCC_Click_LightSlider
from .testDCC_ClickLightslider  import DCC_Click_SoundSlider
from .testDCC_ShowAllModules  import DCC_ShowModules
