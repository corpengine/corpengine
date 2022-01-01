from ...CORPEngine.objects.particleEmitter import ParticleEmitter
from random import randint

class Test(ParticleEmitter):
    def __init__(self, parent):
        super().__init__(parent)
    
    def update(self, dt):
        game = self.getGameService()
        input = game.getService('UserInputService')
        if input.isMouseButtonDown('middle') and input.mouseFocus == 'Game':
            a = randint(0, 255)
            mx, my = input.getMousePosition(True)
            self.create([mx, my], [-1, 0], (a, a, a), 8.5, (0, 0.4), -0.05, collidable=True)