import pygame
from pygame.locals import *
from ..coreContent import availableResolutions

class EngineEventService(object):
    def __init__(self, parent):
        self.parent = parent
        self.name = 'EngineEventService'
        self.type = 'EngineEventService'
        self.currentRes = 0
        self.test = ''
        pygame.event.set_allowed([QUIT, KEYDOWN, MOUSEBUTTONDOWN, VIDEORESIZE])
    
    def events(self):
        game = self.parent
        window = game.parent.window
        guiService = game.getService('GUIService')
        input = game.getService('UserInputService')
        guiFolder = guiService.getChild('GUIFolder')
        debugMenu = guiFolder.getChild('DebugMenu')
        developerConsole = guiFolder.getChild('DeveloperConsole')

        input.mouseStatus = [False, False, False]
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
                    flags = SCALED
                    window.screen = pygame.display.set_mode(availableResolutions[self.currentRes], flags, 32)
                # dev console toggling:
                if event.key == K_F6:
                    if developerConsole != None:
                        developerConsole.enabled = not developerConsole.enabled
                
                # fullscreen toggling
                if event.key == K_F11:
                    window.fullscreen = not window.fullscreen
                    if window.fullscreen:
                        flags = SCALED | FULLSCREEN
                    else:
                        flags = SCALED
                    window.screen = pygame.display.set_mode((640, 360), flags, 32)
                
                # DEVELOPER CONSOLE COMMAND LINE
                if event.key == K_BACKSPACE:
                    developerConsole.inputText = developerConsole.inputText[:-1]
                else:
                    self.devConsoleInput(developerConsole, event)
                if event.key == K_RETURN:
                    developerConsole.readLine()
                    developerConsole.inputText = ''
                if event.key == K_UP:
                    developerConsole.inputText = developerConsole.commandHistory[-1]
            
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    input.mouseStatus[0] = True
                if event.button == 3:
                    input.mouseStatus[2] = True
    
    def devConsoleInput(self, developerConsole, event):
        if developerConsole.enabled and len(developerConsole.inputText)+2 < 45:
            developerConsole.inputText += event.unicode
