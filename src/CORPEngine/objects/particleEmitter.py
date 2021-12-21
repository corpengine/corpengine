import pygame
from ..coreContent import defaultScreenSize

class ParticleEmitter(object):
    def __init__(self, parent):
        self.parent = parent
        self.name = 'ParticleEmitter'
        self.type = 'ParticleEmitter'
        self.particleData = []
        # particle 2D list:
        # [pos, vel, color, size, acc, sizeAccel, shape]
    
    def create(self, position, velocity, color, size, acceleration=(0, 0), sizeAccel=0, shape='circle'):
        self.particleData.append([position, velocity, color, size, acceleration, sizeAccel, shape])
    
    def render(self, dt):
        game = self.parent.parent
        window = game.parent.window
        windowResolutionRatio = (window.screen.get_width()/defaultScreenSize[0], window.screen.get_height()/defaultScreenSize[1])
        renderService = game.getService('EngineRenderService')
        # updating the particles
        for particle in self.particleData:
            # update position
            particle[0][0] += particle[1][0]*dt
            particle[0][1] += particle[1][1]*dt
            # update velocity
            particle[1][0] += particle[4][0]*dt
            particle[1][1] += particle[4][1]*dt
            # update size
            particle[3] += particle[5]*dt
            # delete any small particle
            if particle[3] < 0.1:
                self.particleData.remove(particle)
            
        # rendering
        for particle in self.particleData:
            if not particle[0][0] > defaultScreenSize[0] and not particle[0][1] > defaultScreenSize[1]:
                x = particle[0][0] * windowResolutionRatio[0]
                y = particle[0][1] * windowResolutionRatio[1]
                if particle[6] == 'circle':
                    pygame.draw.circle(window.particle_window, particle[2], (x, y), particle[3]*windowResolutionRatio[1])
                elif particle[6] == 'rectangle':
                    size = particle[3]*windowResolutionRatio[1]
                    pygame.draw.rect(window.particle_window, particle[2], (x, y, size, size))
                if renderService != None:
                    renderService.totalParticlesRendered += 1
