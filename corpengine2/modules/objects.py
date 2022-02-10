from pyray import Vector2

class GameObject(object):
    def __init__(self, parent):
        self.parent = parent
        self.name = self._type = type(self).__name__
    
    def GetGameService(self):
        game = self.parent
        while game.name != "GameService":
            game = game.parent
            
        return game
    
    def _AddChild(self, obj):
        self.__children.update({obj.name: obj})
        if hasattr(object, "Setup"):
            object.Setup()
    
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

class Entity(GameObject):
    def __init__(self, parent):
        super().__init__(parent)
        self.__children = {}
        self.texture = None
        self.scale = 1
        self.rotation = 0
        self.position = Vector2(0, 0)

def NewEntity(name, parent, texture=None, scale=1, rotation=0, position=Vector2(0, 0)):
    newObject = Entity(parent)
    newObject.__name__ = name
    newObject.texture = texture
    newObject.scale = scale
    newObject.rotation = rotation
    newObject.position = position
    parent._AddChild(newObject)
