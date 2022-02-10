import raylib as rl
from corpengine2.modules import core
from corpengine2.modules.colors import WHITE

class Service(object):
    def __init__(self, parent):
        self.parent = parent
        self.name = self.__type = type(self).__name__

class GameService(Service):
    def __init__(self, parent):
        super().__init__(parent)
        self.Assets = Assets(self)
        self.Workspace = Workspace(self)
        self.EngineRenderService = EngineRenderService(self)
    
    def GetService(self, name):
        if hasattr(self, name):
            return getattr(self, name)
        else:
            core.OpenErrorWindow(f"No service named \"{name}\".", self.parent)
    
    def _Update(self):
        self.Workspace._Update()


class Assets(Service):
    def __init__(self, parent):
        super().__init__(parent)
        self.images = {}
        self.textures = {}
    
    def GetImage(self, name: str):
        try:
            return self.images[name]
        except Exception:
            core.OpenErrorWindow(f"No such image with name \"{name}\"", engine)
    
    def LoadImage(self, name, path):
        try:
            self.images.update({name: rl.LoadImage(str.encode(path))})
        except Exception:
            # NOTE this error does not function properly!
            core.OpenErrorWindow("Invalid path for image or file unsupported.", self.parent.parent)

class Workspace(Service):
    def __init__(self, parent):
        super().__init__(parent)
        self.__children = {}
    
    def GetChild(self, name):
        try:
            return self.__children[name]
        except Exception:
            return None
    
    def GetChildren(self):
        return self.__children.values()
    
    def _Update(self):
        """
        for child in self.GetChildren():
            if hasattr(child, "Update"):
                child.Update()"""
        pass
    
    def _AddChild(self, obj):
        self.__children.update({obj.name: obj})
        if hasattr(object, "Setup"):
            object.Setup()

class EngineRenderService(Service):
    def __init__(self, parent):
        super().__init__(parent)
        self.Workspace = self.parent.Workspace
    
    def _Render(self):
        for child in self.Workspace.GetChildren():
            if child._type == "Entity" and child.texture != None:
                rl.DrawTextureEx(child.texture, child.position, child.rotation, child.scale, WHITE)
