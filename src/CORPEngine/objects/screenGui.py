import pygame
from ..coreContent import defaultScreenSize, openErrorWindow

class ScreenGui(object):
    def __init__(self, parent):
        self.parent = parent
        self.name = 'ScreenGUI'
        self.type = 'ScreenGUI'
        self.enabled = True
        self.primaryRect = None
        self.offsetPosition = [0, 0]
        self.children = []
        self.childrenQueue = []
        self.attributes = {}
    
    def writeText(self, text, position, size, color, font='hp_simplified', backgroundColor=None):
        window = self.getEngine().window
        assets = self.getGameService().getService('Assets')
        fonts = assets.fonts
        windowResolutionRatio = (window.screen.get_width()/defaultScreenSize[0], window.screen.get_height()/defaultScreenSize[1])

        textObj = fonts[font].render(str(text), True, color, backgroundColor)
        newPosition = [position[0]+self.offsetPosition[0], position[1]+self.offsetPosition[1]]
        objSize = [textObj.get_width(), textObj.get_height()]
        textObj = pygame.transform.scale(textObj, (objSize[0]*size, objSize[1]*size))
        objSize = [textObj.get_width(), textObj.get_height()]
        textObj = pygame.transform.scale(textObj, (objSize[0]*windowResolutionRatio[1], objSize[1]*windowResolutionRatio[1]))
        x = newPosition[0]*windowResolutionRatio[0]
        y = newPosition[1]*windowResolutionRatio[1]
        pos = [x, y]
        window.gui_window.blit(textObj, pos)
    
    def drawRect(self, color, rect):
        game = self.getGameService()
        window = game.parent.window
        windowResolutionRatio = (window.screen.get_width()/defaultScreenSize[0], window.screen.get_height()/defaultScreenSize[1])

        newRect = rect.copy()
        x = (newRect.x + self.offsetPosition[0]) * windowResolutionRatio[0]
        y = (newRect.y + self.offsetPosition[1]) * windowResolutionRatio[1]
        w = newRect.width * windowResolutionRatio[1]
        h = newRect.height * windowResolutionRatio[1]
        pygame.draw.rect(window.gui_window, color, (x, y, w, h))
    
    def drawImage(self, name, position):
        game = self.getGameService()
        window = game.parent.window
        windowResolutionRatio = (window.screen.get_width()/defaultScreenSize[0], window.screen.get_height()/defaultScreenSize[1])
        assets = game.getService('Assets')

        image = assets.getImage(name)
        pos = [position[0], position[1]]
        x = (pos[0] + self.offsetPosition[0]) * windowResolutionRatio[0]
        y = (pos[1] + self.offsetPosition[1]) * windowResolutionRatio[1]
        w = image.get_width() * windowResolutionRatio[1]
        h = image.get_height() * windowResolutionRatio[1]
        image = pygame.transform.scale(image, (w, h))
        window.gui_window.blit(image, (x, y))
    
    def drawCheckBox(self, value, position):
        game = self.getGameService()
        assets = game.getService('Assets')
        input = game.getService('UserInputService')
        debugValues = self.getEngine().settings.debugValues
        window = self.getEngine().window
        windowResolutionRatio = (window.screen.get_width()/defaultScreenSize[0], window.screen.get_height()/defaultScreenSize[1])

        if debugValues[value]:
            image = assets.getImage('checkbox_true')
        else:
            image = assets.getImage('checkbox_false')
        pos = [(position[0] + self.offsetPosition[0]) * windowResolutionRatio[0], (position[1] + self.offsetPosition[1]) * windowResolutionRatio[1]]
        
        # updating the value
        imageSize = [image.get_width(), image.get_height()]
        checkboxRect = pygame.Rect(pos[0], pos[1], imageSize[0]*windowResolutionRatio[1], imageSize[1]*windowResolutionRatio[1])
        mx, my = input.getMousePosition()
        if checkboxRect.collidepoint(mx, my) and input.mouseStatus[0]:
            debugValues[value] = not debugValues[value]
        
        # rendering
        image = pygame.transform.scale(image, (imageSize[0]*windowResolutionRatio[1], imageSize[1]*windowResolutionRatio[1]))
        window.gui_window.blit(image, pos)
    
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
    
    def updateMouseFocus(self):
        if self.primaryRect != None and self.enabled:
            window = self.getEngine().window
            input = self.getGameService().getService('UserInputService')
            x = self.primaryRect.x + self.offsetPosition[0]
            y = self.primaryRect.y + self.offsetPosition[1]
            w = self.primaryRect.width
            h = self.primaryRect.height
            windowResolutionRatio = (window.screen.get_width()/defaultScreenSize[0], window.screen.get_height()/defaultScreenSize[1])
            rect = pygame.Rect(x*windowResolutionRatio[0], y*windowResolutionRatio[1], w*windowResolutionRatio[1], h*windowResolutionRatio[1])
            mx, my = input.getMousePosition()
            if rect.collidepoint(mx, my):
                input.mouseFocus = self.name
            else:
                input.mouseFocus = 'Game'
            # NOTE mouse focus may have some issues
    
    def _update(self):
        input = self.getGameService().getService('UserInputService')
        self.updateQueue()
        self.childrenEvents()
        self.updateMouseFocus()
        if not self.enabled and input.mouseFocus == self.name:
            input.mouseFocus = 'Game'
    
    def getChild(self, name):
        for child in self.children:
            if child.name == name:
                return child
        return None

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
    
    def setAttribute(self, name, val):
        self.attributes.update({name: val})
    
    def getAttribute(self, name):
        try:
            return self.attributes[name]
        except Exception:
            openErrorWindow(f'unknown attribute "{name}".', self.getEngine())
