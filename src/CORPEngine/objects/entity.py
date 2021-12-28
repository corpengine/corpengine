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
        self.collisionGroup = 0
        self.size = [1, 1]
        self.rotation = 0
    
    def getChild(self, name):
        for child in self.children:
            if child.name == name:
                return child
        raise SyntaxError
    
    def getChildren(self):
        return self.children
    
    def isColliding(self, name, parent='Workspace'):
        game = self.getGameService()
        # TODO: support for objects rather than only services as parents
        parentObj = game.getService(parent)
        for child in parentObj.getChildren():
            if child.name == name and child.collisionGroup == self.collisionGroup and child.type == 'Entity':
                childRect = pygame.Rect(child.position[0], child.position[1], child.image.get_width(), child.image.get_height())
                selfRect = pygame.Rect(self.position[0], self.position[1], self.image.get_width(), self.image.get_height())
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

        
