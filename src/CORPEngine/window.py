import pygame, time
from pygame.locals import *
from .coreContent import defaultScreenSize, openErrorWindow

class Window(object):
    def __init__(self, parent):
        self.parent = parent
        pygame.display.set_caption('game')
        flags = SCALED
        self.screen = pygame.display.set_mode(defaultScreenSize, flags, 32)
        self.render_window = self.screen.copy()
        self.gui_window = self.screen.copy()
        self.particle_window = self.screen.copy()

        self.dt = 0
        self.last_time = time.time()
        self.clock = pygame.time.Clock()
        self.performance = 'Very Good'
        self.fullscreen = False
        self.cursors = {
            'i-beam': SYSTEM_CURSOR_IBEAM,
            'hand': SYSTEM_CURSOR_HAND,
            'wait': SYSTEM_CURSOR_WAIT,
            'arrow': SYSTEM_CURSOR_ARROW,
            'crosshair': SYSTEM_CURSOR_CROSSHAIR
        }
        self.cursor = 'arrow'
      
        pygame.font.init()
    
    def setup(self):
        assets = self.parent.game.getService('Assets')
        pygame.display.set_icon(assets.getImage('icon'))
    
    def update(self):
        self.updateSurfaceSizes()
        self.screen.fill((200, 200, 200))
        self.render_window.fill((200, 200, 200))
        self.gui_window.fill((200, 200, 200))
        self.particle_window.fill((200, 200, 200))
        game = self.parent.game
        RenderService = game.getService('EngineRenderService')
        EventService = game.getService('EngineEventService')
        input = self.parent.game.getService('UserInputService')
        engine = self.parent
        # update delta time:
        self.dt = time.time() - self.last_time
        self.last_time = time.time()
        self.dt *= 60

        if RenderService != None:
            RenderService.totalParticlesRendered = 0

        # events
        game.update()
        if EventService != None: # if the EventService child exists
            EventService.events()
        # rendering stuff
        if RenderService != None: # if the RenderService child exists
            RenderService.render()
        # update the screen:
        self.screen.blit(self.render_window, (0, 0))
        self.screen.blit(self.particle_window, (0, 0))
        self.screen.blit(self.gui_window, (0, 0))
        self.clock.tick(engine.settings.debugValues['fpsCap'])

        if input.mouseFocus != 'Game':
            self.setCursor(self.cursor)
        else:
            self.setCursor('arrow')
        pygame.display.flip()
    
    def updateSurfaceSizes(self):
        self.render_window = self.screen.copy()
        self.gui_window = self.screen.copy()
        self.particle_window = self.screen.copy()
        self.gui_window.set_colorkey((200, 200, 200))
        self.particle_window.set_colorkey((200, 200, 200))
    
    def setCursor(self, name):
        try:
            pygame.mouse.set_cursor(self.cursors[name])
        except Exception:
            openErrorWindow(f'No cursor named "{name}".', self.parent)
