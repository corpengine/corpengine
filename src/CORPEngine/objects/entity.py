import pygame
from ..coreContent import *

class Entity(object):
    def __init__(self, parent):
        self.parent = parent
        self.name = 'Entity'
        self.type = 'Entity'
        self.image = None
        self.position = [0, 0]
        self.render = True
        self.children = []
        self.childrenQueue = []
        self.collisionGroup = 0
        self.size = [1, 1]
        self.rotation = 0
    
    def isColliding(self, name, parent='Workspace'):
        game = self.getGameService()
        workspace = game.getService('Workspace')
        if parent == 'Workspace':
            parentObj = workspace
        else:
            parentObj = parent
        # collision
        if parentObj != None:
            for child in parentObj.getChildren():
                if child.name == name and child.collisionGroup == self.collisionGroup and child.type == 'Entity':
                    childRect = pygame.Rect(child.position[0], child.position[1], child.image.get_width(), child.image.get_height())
                    childRect.width *= child.size[0]
                    childRect.height *= child.size[1]
                    selfRect = pygame.Rect(self.position[0], self.position[1], self.image.get_width(), self.image.get_height())
                    selfRect.width *= self.size[0]
                    selfRect.height *= self.size[1]
                    return selfRect.colliderect(childRect)
        return False
    
    def getGameService(self):
        game = self.parent
        while game.type != 'GameService':
            game = game.parent
        return game
    
    def getEngine(self):
        engine = self.parent
        while engine.type != 'Engine':
            engine = engine.parent
        return engine
    
    def getChild(self, name):
        for child in self.children:
            if child.name == name:
                return child
        return None
    
    def _update(self):
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
        window = self.getEngine().window
        for child in self.children:
            if hasattr(child, 'update'):
                child.update(window.dt)
                if child.type == 'ParticleEmitter':
                    if hasattr(child, 'update'):
                        child.update(window.dt)
                    child.render(window.dt)
            if hasattr(child, '_update'):
                child._update()
    
    def getChildren(self):
        return self.children
        