import pygame
from ...CORPEngine.objects.raycaster import Raycaster

class TestRaycaster(Raycaster):
    def __init__(self, parent):
        super().__init__(parent)
        self.name = 'TestRaycaster'
        self.attributes = {}
    
    def update(self, dt):
        self.drawRect((0, 0, 0), pygame.Rect(55, 25, 55, 55))
