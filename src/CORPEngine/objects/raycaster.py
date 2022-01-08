import pygame
from ..coreContent import defaultScreenSize, openErrorWindow

class Raycaster(object):
    def __init__(self, parent):
        self.name = 'Raycaster'
        self.type = 'Raycaster'
        self.parent = parent
        self.children = []
        self.childrenQueue = []
    
    def getCameraPosition(self, workspace):
        if workspace.currentCamera != None:  # if a default camera exists:
            camX, camY = workspace.currentCamera.position
        else:
            camX, camY = (0, 0)
        return camX, camY
    
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
    
    def drawRect(self, color, rect):
        game = self.getGameService()
        window = game.parent.window
        windowResolutionRatio = (window.screen.get_width()/defaultScreenSize[0], window.screen.get_height()/defaultScreenSize[1])
        camX, camY = self.getCameraPosition(game.getService('Workspace'))

        newRect = rect.copy()
        x = (newRect.x - camX) * windowResolutionRatio[0]
        y = (newRect.y - camY) * windowResolutionRatio[1]
        w = newRect.width * windowResolutionRatio[1]
        h = newRect.height * windowResolutionRatio[1]
        pygame.draw.rect(window.render_window, color, (x, y, w, h))
    
    def drawImage(self, name, position):
        game = self.getGameService()
        window = game.parent.window
        windowResolutionRatio = (window.screen.get_width()/defaultScreenSize[0], window.screen.get_height()/defaultScreenSize[1])
        assets = game.getService('Assets')
        camX, camY = self.getCameraPosition(game.getService('Workspace'))

        image = assets.getImage(name)
        pos = [position[0], position[1]]
        x = (pos[0] - camX) * windowResolutionRatio[0]
        y = (pos[1] - camY) * windowResolutionRatio[1]
        w = image.get_width() * windowResolutionRatio[1]
        h = image.get_height() * windowResolutionRatio[1]
        image = pygame.transform.scale(image, (w, h))
        window.render_window.blit(image, (x, y))

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
