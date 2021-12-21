from ...Scripts.player import Player
from ...Scripts.particleTest import ParticleTest

class Workspace(object):
    def __init__(self, parent):
        self.parent = parent
        self.name = 'Workspace'
        self.type = 'Workspace'
        self.children = []
        self.childrenQueue = [Player(self), ParticleTest(self)]
    
    def getChild(self, name):
        for child in self.children:
            if child.name == name:
                return child
        return None
    
    def update(self):
        self.updateQueue()
        self.childrenEvents()

    def updateQueue(self):
        if len(self.childrenQueue) > 0:
            newChild = self.childrenQueue[0]
            self.children.append(self.childrenQueue[0])
            del self.childrenQueue[0]
            # SETUP/PARENT EVENTS:
            # if the child came from another parent
            if newChild.parent != self:
                if hasattr(newChild, 'parentChanged'):
                    newChild.parentChanged()
            else: # if the child is brand new
                if hasattr(newChild, 'setup'):
                    newChild.setup()
    
    def childrenEvents(self):
        window = self.parent.parent.window
        for child in self.children:
            if hasattr(child, 'update'):
                child.update(window.dt)
                if child.type == 'ParticleEmitter':
                    if hasattr(child, 'update'):
                        child.update(window.dt)
                    child.render(window.dt)
    
    def getChildren(self):
        return self.children
