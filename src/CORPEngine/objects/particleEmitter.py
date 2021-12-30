from random import randint
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
        camX, camY = self.getCameraPosition(workspace)
        particle[1][0] += particle[4][0]*dt
        if particle[7]: # check if collidable
            for child in workspace.getChildren():
                if child.type == 'Entity' and child.collisionGroup == particle[8] and child.image != None:
                    self.particleCollision(child, particle, camX, camY, dt)
                if child.type == 'Folder':
                    for child2 in child.getChildren():
                        self.particleCollision(child2, particle, camX, camY, dt)
        else:
            particle[1][1] += particle[4][1]*dt

    def particleCollision(self, child, particle, camX, camY, dt):
        childRect = pygame.Rect(child.position[0], child.position[1], child.image.get_width(), child.image.get_height())
        childRect.width *= child.size[0]
        childRect.height *= child.size[1]
        childRect.x = (child.position[0] - camX)-childRect.width/2
        childRect.y = (child.position[1] - camY)-childRect.height/2
        selfRect = pygame.Rect(particle[0][0], particle[0][1], particle[3], particle[3])
        if childRect.colliderect(selfRect):
            # reset y velocity
            particle[0][1] -= particle[1][1]
            particle[1][1] = 0
        else:
            particle[1][1] += particle[4][1]*dt
        for child2 in child.getChildren():
            self.particleCollision(child2, particle, camX, camY, dt)

    
    def render(self, dt):
        # FIXME THIS PLACE HAS MAJOR CAMERA ISSUES AND MOSTLY NEEDS THE CAMERA POS TO BE MANUALLY ADDED BY THE USER.
        # FIX THIS!!!!!!!!
        game = self.getGameService()
        workspace = game.getService('Workspace')
        window = game.parent.window
        windowResolutionRatio = (window.screen.get_width()/defaultScreenSize[0], window.screen.get_height()/defaultScreenSize[1])
        renderService = game.getService('EngineRenderService')
        camX, camY = self.getCameraPosition(workspace)
        # updating the particles
        for particle in self.particleData:
            # update position
            if particle[1][0] > dt:
                particle[0][0] += particle[1][0]*dt
            if particle[1][1] > dt:
                particle[0][1] += particle[1][1]*dt
            self.updateParticleVelocity(particle, dt)
            # update size
            particle[3] += particle[5]*dt
            # delete any small particle
            if particle[3] < 0.1:
                self.particleData.remove(particle)
            
        # rendering
        for particle in self.particleData:
            if not particle[0][0] - camX > defaultScreenSize[0] and not particle[0][1] - camY > defaultScreenSize[1]:
                x = particle[0][0] * windowResolutionRatio[0]
                y = particle[0][1] * windowResolutionRatio[1]
                if particle[6] == 'circle':
                    pygame.draw.circle(window.particle_window, particle[2], (x, y), particle[3]*windowResolutionRatio[1])
                elif particle[6] == 'rectangle':
                    size = particle[3]*windowResolutionRatio[1]
                    pygame.draw.rect(window.particle_window, particle[2], (x, y, size, size))
                if renderService != None:
                    renderService.totalParticlesRendered += 1
    
    def getCameraPosition(self, workspace):
        if workspace.currentCamera != None:  # if a default camera exists:
            camX, camY = workspace.currentCamera.position
        else:
            camX, camY = (0, 0)
        return camX, camY
    
    def getEngine(self):
        engine = self.parent
        while engine.type != 'Engine':
            engine = engine.parent
        return engine
