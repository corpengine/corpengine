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
        game = self.parent.parent
        workspace = self.parent.getService('Workspace')
        window = game.window
        windowResolutionRatio = (window.screen.get_width()/defaultScreenSize[0], window.screen.get_height()/defaultScreenSize[1])
        if workspace != None:
            for child in workspace.getChildren():
                if child.type == 'Entity' and child.image != None:
                    image = child.image
                    imageSize = (image.get_width(), image.get_height())
                    image = pygame.transform.scale(image, (imageSize[0]*windowResolutionRatio[1], imageSize[1]*windowResolutionRatio[1]))
                    x = (child.position[0] * windowResolutionRatio[0]) - image.get_width()/2
                    y = (child.position[1] * windowResolutionRatio[1]) - image.get_height()/2
                    pos = [x, y]
                    window.render_window.blit(image, pos)
                    self.totalEntitiesRendered += 1
                # TODO: ADD RENDERING SUPPORT FOR THE CHILDREN OF THE CURRENT CHILD
