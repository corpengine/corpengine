import pygame
from pygame.locals import *
from ..coreContent import defaultScreenSize

class UserInputService(object):
    def __init__(self, parent):
        self.parent = parent
        self.name = 'UserInputService'
        self.type = 'UserInputService'
        self.inputs = {
            'player_right': [K_d, K_RIGHT],
            'player_left': [K_a, K_LEFT],
            'player_up': [K_w, K_UP],
            'player_down': [K_s, K_DOWN],
            'f10': [K_F10],
            'shift': [K_LSHIFT, K_RSHIFT],
            'developer_console': [K_LSHIFT, K_F10]
        }
        self.mouseStatus = [False, False, False]
        self.mouseFocus = 'Game'
    
    def isPressed(self, name):
        keys = pygame.key.get_pressed()
        input = self.inputs[name]
        for key in input:
            if keys[key]:
                return True
        return False

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
