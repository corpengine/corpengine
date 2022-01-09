import pygame
from pygame.locals import *
from ..coreContent import defaultScreenSize, openErrorWindow

class UserInputService(object):
    def __init__(self, parent):
        self.parent = parent
        self.name = 'UserInputService'
        self.type = 'UserInputService'
        self.inputs = {
            'player_right': [K_d],
            'player_left': [K_a],
            'player_up': [K_w],
            'player_down': [K_s],
            'right_arrow': [K_RIGHT],
            'left_arrow': [K_LEFT],
            'up_arrow': [K_UP],
            'down_arrow': [K_DOWN],
            'space': [K_SPACE]
        }
        self.mouseStatus = [False, False, False]
        self.mouseFocus = 'Game'
    
    def isKeyPressed(self, name):
        keys = pygame.key.get_pressed()
        try:
            input = self.inputs[name]
            for key in input:
                if keys[key]:
                    return True
            return False
        except KeyError:
            openErrorWindow(f'unknown input "{name}".', self.parent.parent)

    def isMultiplePressed(self, name):
        keys = pygame.key.get_pressed()
        input = self.inputs[name]
        for key in input:
            if not keys[key]:
                return False
        return True

    def isMouseButtonDown(self, num):
        mouseButtons = {
            'left': 0,
            'middle': 1,
            'right': 2
        }
        mouse = pygame.mouse.get_pressed()
        return mouse[mouseButtons[num]]
    
    def getMousePosition(self, ratio=False):
        mx, my = pygame.mouse.get_pos()
        if ratio: # divide it with the resolution of the window
            window = self.getEngine().window
            windowResolutionRatio = (window.screen.get_width()/defaultScreenSize[0], window.screen.get_height()/defaultScreenSize[1])
            mx /= windowResolutionRatio[0]
            my /= windowResolutionRatio[1]
        return mx, my
    
    def getCameraPosition(self, workspace):
        if workspace.currentCamera != None:  # if a default camera exists:
            camX, camY = workspace.currentCamera.position
        else:
            camX, camY = (0, 0)
        return camX, camY
    
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
