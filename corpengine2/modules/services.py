
class GameService(object):
    def __init__(self, parent):
        self.name = self.type = "GameService"
        self.Assets = Assets(self)

class Assets(object):
    def __init__(self, parent):
        self.name = self.type = "Assets"
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

class EngineRenderService(object):
    def __init__(self, parent):
        self.name = self.type = "EngineRenderService"
