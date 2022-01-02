import pygame
from ..coreContent import defaultScreenSize

class EngineRenderService(object):
    def __init__(self, parent):
        self.parent = parent
        self.name = 'EngineRenderService'
        self.type = 'EngineRenderService'
        self.totalEntitiesRendered = 0
        self.totalParticlesRendered = 0
    
    def render(self):
        self.renderEntities()
    
    def renderEntities(self):
        self.totalEntitiesRendered = 0
        game = self.getGameService()
        workspace = self.parent.getService('Workspace')
        window = game.parent.window
        windowResolutionRatio = (window.screen.get_width()/defaultScreenSize[0], window.screen.get_height()/defaultScreenSize[1])
        camX, camY = self.getCameraPosition(workspace)
        for child in workspace.getChildren():
            if child.type == 'Entity' and child.image != None and child.render:
                self.renderEntity(child, window, windowResolutionRatio, camX, camY)
            elif child.type == 'Folder':
                for child2 in child.getChildren():
                    if child2.type == 'Entity' and child2.image != None and child2.render:
                        self.renderEntity(child2, window, windowResolutionRatio, camX, camY)
    
    def renderEntity(self, child, window, windowResolutionRatio, camX, camY):
        image = child.image
        imageSize = (image.get_width(), image.get_height())
        image = pygame.transform.scale(image, (imageSize[0]*child.size[0], imageSize[1]*child.size[1]))
        imageSize = (image.get_width(), image.get_height())
        image = pygame.transform.scale(image, (imageSize[0]*windowResolutionRatio[1], imageSize[1]*windowResolutionRatio[1]))
        image = pygame.transform.rotate(image, child.rotation)
        x = ((child.position[0] - camX) * windowResolutionRatio[0]) - image.get_width()/2
        y = ((child.position[1] - camY) * windowResolutionRatio[1]) - image.get_height()/2
        pos = [x, y]
        window.render_window.blit(image, pos)
        self.totalEntitiesRendered += 1
        for childA in child.getChildren():
            self.renderEntity(childA, window, windowResolutionRatio, camX, camY)
    
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
