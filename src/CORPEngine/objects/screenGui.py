import pygame
from ..coreContent import *

class ScreenGui(object):
    def __init__(self, parent):
        self.parent = parent
        self.name = 'ScreenGUI'
        self.type = 'ScreenGUI'
        self.enabled = True
        self.primaryRect = None
        self.offsetPosition = [0, 0]
    
    def writeText(self, text, position, size, color, font='hp_simplified', backgroundColor=None):
        window = self.parent.parent.parent.window
        assets = self.parent.parent.getService('Assets')
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
        game = self.parent.parent
        window = game.parent.window
        windowResolutionRatio = (window.screen.get_width()/defaultScreenSize[0], window.screen.get_height()/defaultScreenSize[1])

        newRect = rect.copy()
        newRect.x += self.offsetPosition[0]
        newRect.y += self.offsetPosition[1]
        newRect.x *= windowResolutionRatio[0]
        newRect.y *= windowResolutionRatio[1]
        newRect.width *= windowResolutionRatio[1]
        newRect.height *= windowResolutionRatio[1]
        pygame.draw.rect(window.gui_window, color, newRect)
    
    def drawImage(self, name, position):
        game = self.parent.parent
        window = game.parent.window
        windowResolutionRatio = (window.screen.get_width()/defaultScreenSize[0], window.screen.get_height()/defaultScreenSize[1])
        assets = game.getService('Assets')

        image = assets.getImage(name)
        pos = [position[0], position[1]]
        pos[0] += self.offsetPosition[0]
        pos[1] += self.offsetPosition[1]
        print(self.getGameService().getService('UserInputService').mouseFocus)
        pos[0] *= windowResolutionRatio[0]
        pos[1] *= windowResolutionRatio[1]
        rect = pygame.Rect(pos[0], pos[1], image.get_width()*windowResolutionRatio[1], image.get_height()*windowResolutionRatio[1])
        imageSize = [image.get_width(), image.get_height()]
        image = pygame.transform.scale(image, (imageSize[0]*windowResolutionRatio[1], imageSize[1]*windowResolutionRatio[1]))
        window.gui_window.blit(image, pos)
    
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
    
    def updateMouseFocus(self, element):
        input = self.getGameService().getService('UserInputService')
        mx, my = input.getMousePosition()
        if element.collidepoint(mx, my):
            input.mouseFocus = self.name
        else:
            input.mouseFocus = 'Game'
    
    def _update(self):
        if self.primaryRect != None:
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
