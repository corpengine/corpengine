import pygame, time
from pygame.locals import *
from .coreContent import defaultScreenSize

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
        self.fps_cap = 144
        self.performance = 'Very Good'
        self.fullscreen = False
      
        pygame.font.init()
    
    def update(self):
        self.updateSurfaceSizes()
        self.screen.fill((200, 200, 200))
        self.render_window.fill((200, 200, 200))
        self.gui_window.fill((200, 200, 200))
        self.particle_window.fill((200, 200, 200))
        game = self.parent.game
        RenderService = game.getService('EngineRenderService')
        EventService = game.getService('EngineEventService')
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
        pygame.display.update()
    
    def updateSurfaceSizes(self):
        self.render_window = self.screen.copy()
        self.gui_window = self.screen.copy()
        self.particle_window = self.screen.copy()
        self.gui_window.set_colorkey((200, 200, 200))
        self.particle_window.set_colorkey((200, 200, 200))
