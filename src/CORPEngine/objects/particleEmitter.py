import pygame
from ..coreContent import defaultScreenSize

class ParticleEmitter(object):
    def __init__(self, parent):
        self.parent = parent
        self.name = 'ParticleEmitter'
        self.type = 'ParticleEmitter'
        self.particleData = []
        # particle 2D list:
        # [pos, vel, color, size, acc, sizeAccel, shape, collidable, collisionGroup]
    
    def getGameService(self):
        game = self.parent
        while game.type != 'GameService':
            game = game.parent
        return game
    
    def create(self, position, velocity, color, size, acceleration=(0, 0), sizeAccel=0, shape='circle', collidable=False, collisionGroup=0):
        self.particleData.append([position, velocity, color, size, acceleration, sizeAccel, shape, collidable, collisionGroup])
    
    def updateParticleVelocity(self, particle, dt):
        game = self.getGameService()
        workspace = game.getService('Workspace')
        particle[1][0] += particle[4][0]*dt
        if particle[7]: # check if collidable
            for child in workspace.getChildren():
                if child.type == 'Entity' and child.collisionGroup == particle[8] and child.image != None:
                    #childRect = pygame.Rect(child.position[0], child.position[1], child.image.get_width(), child.image.get_height())
                    childRect = child.image.get_rect()
                    childRect.x = child.position[0]-child.image.get_width()/2
                    childRect.y = child.position[1]-child.image.get_height()/2
                    selfRect = pygame.Rect(particle[0][0], particle[0][1], particle[3], particle[3])
                    if selfRect.colliderect(childRect):
                        # reset y velocity
                        particle[1][1] = 0
                    else:
                        particle[1][1] += particle[4][1]*dt
            # NOTE this place may have some future issues
        else:
            particle[1][1] += particle[4][1]*dt

    
    def render(self, dt):
        game = self.getGameService()
        window = game.parent.window
        windowResolutionRatio = (window.screen.get_width()/defaultScreenSize[0], window.screen.get_height()/defaultScreenSize[1])
        renderService = game.getService('EngineRenderService')
        # updating the particles
        for particle in self.particleData:
            # update position
            particle[0][0] += particle[1][0]*dt
            particle[0][1] += particle[1][1]*dt
            self.updateParticleVelocity(particle, dt)
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
