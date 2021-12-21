import pygame
from pygame.locals import *
from ..coreContent import availableResolutions

class EngineEventService(object):
    def __init__(self, parent):
        self.parent = parent
        self.name = 'EngineEventService'
        self.type = 'EngineEventService'
        self.currentRes = 0
    
    def events(self):
        game = self.parent
        window = game.parent.window
        guiService = game.getService('GUIService')
        debugMenu = guiService.getChild('DebugMenu')
        developerConsole = guiService.getChild('DeveloperConsole')
        # pygame events
        for event in pygame.event.get():
            if event.type == QUIT:
                game.parent.running = False
            # developer tools
            if event.type == KEYDOWN:
                # debug menu toggling
                if event.key == K_F1:
                    if debugMenu != None:
                        debugMenu.enabled = not debugMenu.enabled
                # change resolution
                if event.key == K_F8:
                    self.currentRes += 1
                    if self.currentRes == len(availableResolutions):
                        self.currentRes = 0
                    window.screen = pygame.display.set_mode(availableResolutions[self.currentRes])
                # dev console toggling:
                if event.key == K_F6:
                    if developerConsole != None:
                        developerConsole.enabled = not developerConsole.enabled
        
        # CORP Engine events
