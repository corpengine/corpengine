from .engineEventService import EngineEventService
from .engineRenderService import EngineRenderService
from .assets import Assets
from .object import Object
from .workspace import Workspace
from .userInputService import UserInputService
from .guiService import GUIService
from .scriptService import ScriptService

class GameService(object):
    def __init__(self, parent):
        self.parent = parent
        self.name = 'GameService'
        self.type = 'GameService'
        self.children = [
            Assets(self), EngineRenderService(self), EngineEventService(self),
            UserInputService(self), Object(self), Workspace(self), GUIService(self),
            ScriptService(self)
        ]
        self.childrenQueue = []
    
    def getService(self, name):
        for service in self.children:
            if service.name == name:
                return service
        return None
    
    def update(self):
        # load the next member of the children queue
        if len(self.childrenQueue) > 0:
            self.children.append(self.childrenQueue[0])
            del self.childrenQueue[0]
        
        # update children
        for service in self.children:
            if hasattr(service, 'update'):
                service.update()
