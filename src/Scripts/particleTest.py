from ..CORPEngine.objects.particleEmitter import ParticleEmitter
from random import uniform, randint, choice
import math

class ParticleTest(ParticleEmitter):
    def __init__(self, parent):
        super().__init__(parent)
        self.name = 'ParticleTest'
        self.shapes = ['circle', 'rectangle']
    
    def update(self, dt):
        #self.create([320, 180], [5, 3], (255, 0, 0), 7, [-0.5, -0.2], -0.1)
        game = self.parent.parent
        player = game.getService('Workspace').getChild('Player')
        input = game.getService('UserInputService')
        """
        if player != None:
            newPos = [player.position[0], player.position[1]]
            self.create(newPos, [uniform(-3, 3), 0], (randint(0, 255), randint(0, 255), randint(0, 255)), 10, (0, 0.06), -0.05, shape=choice(self.shapes))
        """
        for i in range(3):
            position = [320, 15]
            self.create(position, [uniform(-3.5, 3.5), 0], (randint(0, 255), randint(0, 255), randint(0, 255)), 13, (0, 0.1), -0.1, shape=choice(self.shapes), collidable=True)
