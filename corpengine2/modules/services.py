from corpengine2.modules import core

class Service(object):
    def __init__(self, parent):
        self.parent = parent
        self.name = self.__type = type(self).__name__

class GameService(Service):
    def __init__(self, parent):
        super().__init__(parent)
        self.Assets = Assets(self)
    
    def GetService(self, name):
        if hasattr(self, name):
            return getattr(self, name)
        else:
            core.OpenErrorWindow(f"No service named \"{name}\".", self.parent)

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
