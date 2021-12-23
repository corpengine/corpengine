import pygame
from ...CORPEngine.objects.screenGui import screenGui
from ...CORPEngine.coreContent import defaultScreenSize

class MouseCursor(screenGui):
    def __init__(self, parent):
        super().__init__(parent)
    
    def setup(self):
        assets = self.getGameService().getService('Assets')
        assets.images[5][1] = pygame.transform.scale(assets.images[5][1], (assets.images[5][1].get_width()//100, assets.images[5][1].get_height()//100))
        pygame.mouse.set_visible(False)
    
    def update(self):
        window = self.getEngine().window
        windowResolutionRatio = (window.screen.get_width()/defaultScreenSize[0], window.screen.get_height()/defaultScreenSize[1])
        input = self.getGameService().getService('UserInputService')
        mx, my = input.getMousePosition()
        self.drawImage('cursor', (mx/windowResolutionRatio[0], my/windowResolutionRatio[1]))
