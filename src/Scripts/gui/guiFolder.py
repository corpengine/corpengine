from ...CORPEngine.objects.folder import Folder
from .developerConsole import DeveloperConsole
from .debugMenu import DebugMenu

class GuiFolder(Folder):
    def __init__(self, parent):
        super().__init__(parent)
        self.name = 'GUIFolder'
    
    def setup(self):
        self.childrenQueue.append(DeveloperConsole(self))
        self.childrenQueue.append(DebugMenu(self))
