from ...CORPEngine.objects.particleEmitter import ParticleEmitter
from random import uniform, randint, choice
import math

class ParticleTest(ParticleEmitter):
    def __init__(self, parent):
        super().__init__(parent)
        self.name = 'ParticleTest'
        self.shapes = ['circle', 'rectangle']
