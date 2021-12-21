import pygame
from ..coreContent import *

class screenGui(object):
    def __init__(self, parent):
        self.parent = parent
        self.name = 'ScreenGUI'
        self.type = 'ScreenGUI'
        self.enabled = True
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
        x = newPosition[0]*windowResolutionRatio[0] + self.offsetPosition[0]
        y = newPosition[1]*windowResolutionRatio[1] + self.offsetPosition[1]
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
        pos[0] *= windowResolutionRatio[0]
        pos[1] *= windowResolutionRatio[1]
        imageSize = [image.get_width(), image.get_height()]
        image = pygame.transform.scale(image, (imageSize[0]*windowResolutionRatio[1], imageSize[1]*windowResolutionRatio[1]))
        window.gui_window.blit(image, pos)
    
    def getSizeOfText(self, text, font, size):
        assets = self.parent.parent.getService('Assets')
        window = self.parent.parent.parent.window

        textObj = assets.fonts[font].render(text, True, (0, 0, 0))
        objSize = [textObj.get_width(), textObj.get_height()]
        textObj = pygame.transform.scale(textObj, (objSize[0]*size, objSize[1]*size))
        return textObj.get_width(), textObj.get_height()
