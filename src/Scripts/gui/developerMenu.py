import pygame
from pygame import mouse
from ...CORPEngine.objects.screenGui import ScreenGui
from ...CORPEngine.coreContent import defaultScreenSize

class DeveloperConsole(ScreenGui):
    def __init__(self, parent):
        super().__init__(parent)
        self.name = 'DeveloperConsole'
        self.firstMousePos = [0, 0]
        self.valueData = []
        self.inputText = ''
        # value data list:
        # [type, value]
    
    def setup(self):
        self.enabled = False
        self.panelRect = pygame.Rect(0, 0, 405, 255)
        self.offsetPosition = [320-self.panelRect.width/2, 180-self.panelRect.height/2]
        self.barRect = pygame.Rect(0, 0, 405, 23)
        self.closeRect = pygame.Rect(382, 0, 23, 23)
        self.primaryRect = self.panelRect
        self.addToDevMenu('checkbox', 'vsync')
        self.addToDevMenu('show', 'vsync')
    
    def update(self, dt):
        engine = self.getEngine()
        input = self.getGameService().getService('UserInputService')
        window = engine.window
        windowResolutionRatio = (window.screen.get_width()/defaultScreenSize[0], window.screen.get_height()/defaultScreenSize[1])
        # render window
        self.drawRect((38, 38, 38), self.panelRect)
        self.drawRect((230, 230, 230), self.barRect)
        self.drawImage('dev_close', (382, 0))

        # title text
        self.writeText('Developer Menu', (0, 0), 1, (35, 35, 35), font='roboto_mono')

        #self.drawCheckBox('vsync', (200, 115))
        self.drawValues()

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
        if closeRect.collidepoint(mx, my) and input.isMouseButtonDown('left'):
            self.enabled = False
    
    def addToDevMenu(self, type, value):
        self.valueData.append([type, value])
    
    def drawValues(self):
        x = 0
        y = 50
        debugValues = self.getEngine().settings.debugValues
        for value in self.valueData:
            if value[0] == 'show':
                self.writeText(f'{value[1]}:', [x, y], 1, (220, 220, 220), 'roboto_mono')
                self.writeText(str(debugValues[value[1]]), [x+len(f'{value[1]}:')*10, y], 1, (220, 220, 220), 'roboto_mono')
            elif value[0] == 'checkbox':
                self.writeText(f'{value[1]}:', [x, y], 1, (220, 220, 220), 'roboto_mono')
                self.drawCheckBox(value[1], [x+len(f'{value[1]}:')*10, y+3.5])
            y += 16.5
