from ...CORPEngine.objects.folder import Folder
from .testEntity import TestEntity

class EntityFolder(Folder):
    def __init__(self, parent):
        super().__init__(parent)
        self.name = 'EntityFolder'
    
    def setup(self):
        self.childrenQueue.append(TestEntity(self))
