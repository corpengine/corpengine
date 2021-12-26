from ...CORPEngine.objects.entity import Entity
from ...CORPEngine.coreContent import *

class Player(Entity):
    def __init__(self, parent):
        super().__init__(parent)
        self.name = 'Player'
    
    def setup(self):
        game = self.parent.parent
        assets = game.getService('Assets')
        self.image = assets.getImage('test')
        
        self.speed = 4
        self.position = [320, 180]
        self.collisionGroup = 1
    
    def update(self, dt):
        game = self.getGameService()
        input = game.getService('UserInputService')
        speed = self.speed * dt
        self.position[0] += input.isPressed('player_left')*-speed + input.isPressed('player_right')*speed
        self.position[1] += input.isPressed('player_up')*-speed + input.isPressed('player_down')*speed
