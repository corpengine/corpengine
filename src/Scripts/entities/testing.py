from ...CORPEngine.objects.entity import Entity

class Testing(Entity):
    def __init__(self, parent):
        super().__init__(parent)
        self.name = 'Testing'
    
    def setup(self):
        assets = self.getGameService().getService('Assets')
        self.image = assets.getImage('dev_close')
        self.size = [2.5, 2.5]
        self.position = [100, 50]
    
    def update(self, dt):
        workspace = self.getGameService().getService('Workspace')
        entityFolder = workspace.getChild('EntityFolder')
        print(self.isColliding('Player', entityFolder))
