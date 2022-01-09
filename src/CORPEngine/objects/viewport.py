import pygame
from pygame.constants import WINDOWMOVED
from ..coreContent import openErrorWindow, defaultScreenSize
from pygame.locals import SRCALPHA

class Viewport(object):
    def __init__(self, parent):
        self.name = 'Viewport'
        self.type = 'Viewport'
        self.parent = parent
        self.background = [45, 45, 45]
        self.outline = 0
        self.size = [75, 50]
        self.enabled = True
        self.transparency = 100
        self.attributes = {}
        self.position = [0, 0]
        self.children = []
        self.childrenQueue = []
    
    def updateViewport(self):
        engine = self.getEngine()
        window = engine.window

        surface = pygame.Surface(self.size)
        surface = surface.convert()
        surface.fill(self.background)
        # rendering object inside:
        windowResolutionRatio = [self.size[0]/defaultScreenSize[0], self.size[1]/defaultScreenSize[1]]

        for child in self.getChildren():
            if child.type == 'Entity' and child.image != None:
                # TODO make a camera system for the viewport
                pos = [child.position[0], child.position[1]]
                size = [child.image.get_width(), child.image.get_height()]
                size[0] *= windowResolutionRatio[1]
                size[1] *= windowResolutionRatio[1]
                img = pygame.transform.scale(child.image, size)
                img = pygame.transform.rotate(img, child.rotation)
                pos[0] *= windowResolutionRatio[0]
                pos[1] *= windowResolutionRatio[1]
                pos[0] -= img.get_width()/2
                pos[1] -= img.get_height()/2
                surface.blit(img, pos)

        window.gui_window.blit(surface, self.position)
    
    def getChild(self, name):
        for child in self.children:
            if child.name == name:
                return child
        return None
    
    def _update(self):
        self.updateQueue()
        self.childrenEvents()
        self.updateViewport()

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
                        child.render(window.dt)
            if hasattr(child, '_update'):
                child._update()
    
    def getChildren(self):
        return self.children
    
    def setAttribute(self, name, val):
        self.attributes.update({name: val})
    
    def getAttribute(self, name):
        try:
            return self.attributes[name]
        except Exception:
            openErrorWindow(f'unknown attribute "{name}".', self.getEngine())
    
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