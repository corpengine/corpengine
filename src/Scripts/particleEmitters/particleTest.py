from ...CORPEngine.objects.particleEmitter import ParticleEmitter
from random import uniform, randint, choice
import math

class ParticleTest(ParticleEmitter):
    def __init__(self, parent):
        super().__init__(parent)
        self.name = 'ParticleTest'
        self.shapes = ['circle', 'rectangle']
    
    def update(self, dt):
        game = self.getGameService()
        input = game.getService('UserInputService')
        if input.isMouseButtonDown('left'):
            a = randint(0, 255)
            mx, my = input.getMousePosition(True)
            self.create([mx, my], [0, 0], (a, a, a), 8.5, (0, 0.3), -0.05, collidable=True)
