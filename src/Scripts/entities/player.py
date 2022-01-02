from ...CORPEngine.objects.entity import Entity
from ...CORPEngine.coreContent import *

class Player(Entity):
    def __init__(self, parent):
        super().__init__(parent)
        self.name = 'Player'
    
    def setup(self):
        game = self.getGameService()
        assets = game.getService('Assets')
        self.image = assets.getImage('q')
        
        self.speed = 4
        self.position = [320, 180]
        self.collisionGroup = 0
    
    def update(self, dt):
        game = self.getGameService()
        guiFolder = game.getService('GUIService').getChild('GUIFolder')
        devConsole = None
        if guiFolder != None:
            devConsole = guiFolder.getChild('DeveloperConsole')
        if devConsole != None and not devConsole.enabled:
            input = game.getService('UserInputService')
            speed = self.speed * dt
            self.position[0] += input.isPressed('player_left')*-speed + input.isPressed('player_right')*speed
            self.position[1] += input.isPressed('player_up')*-speed + input.isPressed('player_down')*speed
