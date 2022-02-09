
class GameObject(object):
    def __init__(self, parent):
        self.parent = parent
        self.name = type(self).__name__
        self.type = "Entity"

class Entity(GameObject):
    def __init__(self, parent):
        super().__init__(parent)
        self.__children = {}
        self.texture = None
        self.scale = 1
        self.rotation = 0
    
    def GetChild(self, name):
        try:
            return self.__children[name]
        except Exception:
            return None
    
    def GetChildren(self):
        return self.__children.values()
    
    def _Update(self):
        pass
