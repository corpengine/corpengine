import pygame
from ..coreContent import defaultScreenSize, openErrorWindow

class ParticleEmitter(object):
    def __init__(self, parent):
        self.parent = parent
        self.name = 'ParticleEmitter'
        self.type = 'ParticleEmitter'
        self.children = []
        self.childrenQueue = []
        self.particleData = []
        self.attributes = {}
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
            particle[0][0] += particle[1][0]*dt
            particle[0][1] += particle[1][1]*dt
            self.updateParticleVelocity(particle, dt)
            # update size
            particle[3] += particle[5]*dt
            # delete any small particle
            if particle[3] < 0.1:
                self.particleData.remove(particle)
    
        # rendering
        if self.getEngine().settings.debugValues['renderParticles']:
            for particle in self.particleData:
                if not particle[0][0] > defaultScreenSize[0] and not particle[0][1] > defaultScreenSize[1]:
                    x = particle[0][0] * windowResolutionRatio[0]
                    y = particle[0][1] * windowResolutionRatio[1]
                    if particle[6] == 'circle':
                        pygame.draw.circle(window.particle_window, particle[2], (x, y), particle[3]*windowResolutionRatio[1])
                    elif particle[6] == 'rectangle':
                        size = particle[3]*windowResolutionRatio[1]
                        pygame.draw.rect(window.particle_window, particle[2], (x, y, size, size))
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
    
    def getChild(self, name):
        for child in self.children:
            if child.name == name:
                return child
        return None
    
    def _update(self):
        self.updateQueue()
        self.childrenEvents()

    def updateQueue(self):
        if len(self.childrenQueue) > 0:
            newChild = self.childrenQueue[0]
            self.children.append(self.childrenQueue[0])
            del self.childrenQueue[0]
            # SETUP/PARENT EVENTS:
            # if the child came from another parent
            if newChild.parent != self:
                if hasattr(newChild, 'parentChanged'):
                    newChild.parentChanged()
            else: # if the child is brand new
                if hasattr(newChild, 'setup'):
                    newChild.setup()
    
    def childrenEvents(self):
        window = self.getEngine().window
        for child in self.children:
            if hasattr(child, 'update'):
                child.update(window.dt)
                if child.type == 'ParticleEmitter':
                    if hasattr(child, 'update'):
                        child.render(window.dt)
            if hasattr(child, '_update'):
                child._update()
    
    def getChildren(self):
        return self.children
    
    def setAttribute(self, name, val):
        self.attributes.update({name: val})
    
    def getAttribute(self, name):
        try:
            return self.attributes[name]
        except Exception:
            openErrorWindow(f'unknown attribute "{name}".', self.getEngine())
