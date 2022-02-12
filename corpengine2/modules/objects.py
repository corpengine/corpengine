from pyray import Vector2
from corpengine2.modules.core import OpenErrorWindow
from corpengine2.modules.components import Transform, Texture

class GameObject(object):
    def __init__(self, parent, scale=1, rotation=0, position=Vector2(0, 0)):
        self.parent = parent
        self.name = self._type = type(self).__name__
        self.__components = {}
        self.AddComponent(Transform(self, scale, rotation, position))

    def GetGameService(self):
        game = self.parent
        while game.name != "GameService":
            game = game.parent
            
        return game
    
    def GetEngine(self):
        engine = self.parent
        while engine._type != "Engine":
            engine = engine.parent
            
        return engine
    
    def _AddChild(self, obj):
        self.__children.update({obj.name: obj})
    
    def GetChild(self, name):
        try:
            return self.__children[name]
        except Exception:
            return None
    
    def GetChildren(self):
        return self.__children.values()
    
    def GetComponent(self, name):
        try:
            return self.__components[name]
        except Exception:
            OpenErrorWindow(f"No component found named \"{name}\".", self.GetEngine())
    
    def HasComponent(self, name):
        return name in self.__components.keys()

    def GetComponents(self):
        return self.__components.values()
    
    def AddComponent(self, obj):
        try:
            newObj = obj(self)
        except Exception:
            newObj = obj

        if self.HasComponent(newObj.type):
            OpenErrorWindow(f"Sorry, only one {newObj.type} per Object ¯\_(ツ)_/¯", self.GetEngine())
        else:
            self.__components.update({newObj.type: newObj})
            if newObj.type == "ScriptComponent" and hasattr(newObj, "Setup"):
                newObj.Setup()

    def _Update(self):
        for child in self.GetChildren():
            if child.HasComponent("ScriptComponent"):
                ScriptComponent = child.GetComponent("ScriptComponent")
                if hasattr(ScriptComponent, "Update"):
                    ScriptComponent.Update()

class Entity(GameObject):
    def __init__(self, parent, texture=None, scale=1, rotation=0, position=Vector2(0, 0)):
        super().__init__(parent, scale, rotation, position)
        self.__children = {}
        self.__components = {}
        self.AddComponent(Texture(self, texture))

def NewEntity(name, engine, texture=None, scale=1, rotation=0, position=Vector2(0, 0)):
    """Create & return a GameObject with Texture"""
    newObject = Entity(engine.Game.Workspace, texture, scale, rotation, position)
    newObject.__name__ = newObject.name = name
    engine.Game.Workspace._AddChild(newObject)
    return newObject

def NewGameObject(name, engine, scale=1, rotation=0, position=Vector2(0, 0)):
    """Create & return a plain GameObject"""
    newObject = GameObject(engine.Game.Workspace, scale, rotation, position)
    newObject.__name__ = newObject.name = name
    engine.Game.Workspace._AddChild(newObject)
    return newObject
