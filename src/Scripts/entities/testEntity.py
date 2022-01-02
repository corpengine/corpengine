from ...CORPEngine.objects.entity import Entity

class TestEntity(Entity):
    def __init__(self, parent):
        super().__init__(parent)
        self.name = 'TestEntity'
    
    def setup(self):
        game = self.getGameService()
        assets = game.getService('Assets')

        self.position = [320, 85]
        self.image = assets.getImage('test')
        self.collisionGroup = 0
