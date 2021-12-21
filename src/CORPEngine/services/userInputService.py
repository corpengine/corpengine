import pygame
from pygame.locals import *

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

    def isMouseButtonClicked(self, num):
        mouseButtons = {
            'left': 0,
            'middle': 1,
            'right': 2
        }
        mouse = pygame.mouse.get_pressed()
        return mouse[mouseButtons[num]]
