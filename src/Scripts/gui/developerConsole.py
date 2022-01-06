import pygame, distutils
import distutils
from ...CORPEngine.objects.screenGui import ScreenGui
from ...CORPEngine.coreContent import defaultScreenSize, openErrorWindow

class DeveloperConsole(ScreenGui):
    def __init__(self, parent):
        super().__init__(parent)
        self.name = 'DeveloperConsole'
        self.firstMousePos = [0, 0]
        self.inputText = ''
        self.values = ['fpsCap', 'renderParticles']
        self.valueTypes = {'fpsCap': 'number', 'renderParticles': 'boolean'}
        self.output = []
        self.commandHistory = []
        # value data list:
        # [type, value]
    
    def setup(self):
        self.enabled = False
        self.panelRect = pygame.Rect(0, 0, 405, 255)
        self.offsetPosition = [320-self.panelRect.width/2, 180-self.panelRect.height/2]
        self.barRect = pygame.Rect(0, 0, 405, 23)
        self.closeRect = pygame.Rect(382, 0, 23, 23)
        self.commandLineRect = pygame.Rect(0, 230, 405, 25)
        
        self.primaryRect = self.panelRect
    
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
        self.writeText('Developer Console', (0, 0), 1, (35, 35, 35), font='roboto_mono')

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
        # render command line
        self.writeText('>>' + self.inputText, [0, 235], 1, (220, 220, 220), 'roboto_mono', (55, 55, 55))
        # render output
        self.writeOutput()
    
    def readLine(self):
        settings = self.getEngine().settings
        val = ''
        i = 0
        while self.inputText[i] != ";":
            val += self.inputText[i]
            i += 1
        if val == 'set':
            i += 2
            # TODO improve this part to allow some spaces to be placed
            val = ''
            while self.inputText[i] != ' ':
                val += self.inputText[i]
                i += 1

            if val in self.values:
                val2 = ''
                i += 1
                while i != len(self.inputText):
                    val2 += self.inputText[i]
                    i += 1
                # value giving stuff
                # boolean values:
                if self.valueTypes[val] == 'boolean':
                    try:
                        settings.debugValues[val] = eval(val2)
                        self.printLn(f'{val} variable set to {val2}')
                    except Exception:
                        self.printLn(f'Error: invalid value for {val}')
                elif self.valueTypes[val] == 'number':
                    try:
                        settings.debugValues[val] = int(val2)
                        self.printLn(f'{val} variable set to {val2}')
                    except Exception:
                        self.printLn(f'Error: invalid value for {val}')
            else:
                self.printLn('Error: no value named ' + val)
        elif val == 'close':
            self.enabled = False
        else:
            self.printLn(f'Error: unknown keyword "{val}"')
        
        self.commandHistory.append(self.inputText)
    
    def printLn(self, text):
        if len(self.output) > 5:
            del self.output[0]
        self.output.append(text)
    
    def writeOutput(self):
        x = 0
        y = 25
        for text in self.output:
            self.writeText(text, [x, y], 0.8, (220, 220, 220), 'roboto_mono')
            y += 14
