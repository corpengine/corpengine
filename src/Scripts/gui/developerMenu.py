import pygame
from pygame import mouse
from ...CORPEngine.objects.screenGui import screenGui
from ...CORPEngine.coreContent import defaultScreenSize

class DeveloperConsole(screenGui):
    def __init__(self, parent):
        super().__init__(parent)
        self.name = 'DeveloperConsole'
        self.firstMousePos = [0, 0]
    
    def setup(self):
        self.enabled = False
        self.panelRect = pygame.Rect(0, 0, 405, 255)
        self.barRect = pygame.Rect(0, 0, 405, 23)
        self.textBarRect = pygame.Rect(0, 230, 405, 25)
        self.closeRect = pygame.Rect(382, 0, 23, 23)
        self.offsetPosition = [320-self.panelRect.width/2, 180-self.panelRect.height/2]
    
    def update(self):
        engine = self.getEngine()
        input = self.getGameService().getService('UserInputService')
        window = engine.window
        windowResolutionRatio = (window.screen.get_width()/defaultScreenSize[0], window.screen.get_height()/defaultScreenSize[1])
        # render window
        self.drawRect((38, 38, 38), self.panelRect)
        self.drawRect((230, 230, 230), self.barRect)
        self.drawImage('dev_close', (382, 0))

        # title text
        self.writeText('Developer Menu', (-self.offsetPosition[0], -self.offsetPosition[1]), 1, (35, 35, 35), font='roboto_mono')

        # close button code
        mx, my = input.getMousePosition()
        # NOTE maybe clean up this code over here? it seems messed up ngl
        closeRect = self.closeRect.copy()
        closeRect.x += self.offsetPosition[0]
        closeRect.x *= windowResolutionRatio[0]
        closeRect.y += self.offsetPosition[1]
        closeRect.y *= windowResolutionRatio[1]
        closeRect.width *= windowResolutionRatio[1]
        closeRect.height *= windowResolutionRatio[1]
        # check for mouse click
        if closeRect.collidepoint(mx, my) and input.isMouseButtonClicked('left'):
            self.enabled = False
