import pygame
from pygame import mouse
from ..CORPEngine.objects.screenGui import screenGui
from ..CORPEngine.coreContent import defaultScreenSize

class DeveloperConsole(screenGui):
    def __init__(self, parent):
        super().__init__(parent)
        self.name = 'DeveloperConsole'
        self.firstMousePos = [0, 0]
    
    def setup(self):
        game = self.parent.parent

        self.enabled = False
        self.panelRect = pygame.Rect(0, 0, 405, 255)
        self.barRect = pygame.Rect(0, 0, 405, 23)
        self.offsetPosition = [320-self.panelRect.width/2, 180-self.panelRect.height/2]
    
    def update(self):
        game = self.parent.parent
        # render window
        self.drawRect((38, 38, 38), self.panelRect)
        self.drawRect((230, 230, 230), self.barRect)
        self.drawImage('dev_close', (382, 0))
        # other stuff lol
