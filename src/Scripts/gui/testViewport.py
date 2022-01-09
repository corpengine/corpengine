from ...CORPEngine.objects.viewport import Viewport
from ..entities.player import Player

class TestViewport(Viewport):
    def __init__(self, parent):
        super().__init__(parent)
        self.name = 'TestViewport'
        self.size = [640/4, 360/4]
        self.childrenQueue.append(Player(self))
    
    def update(self):
        game = self.getGameService()
        input = game.getService('UserInputService')
        mx, my = input.getMousePosition()
        self.position = [mx, my]
