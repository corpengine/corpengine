import corpengine
from corpengine import flags, PhysicsEntity, Entity, ScreenGui

engine = corpengine.init(windowTitle='Window', flags=flags.SCALED)

class TestEntity(PhysicsEntity):
    def __init__(self, parent: object) -> None:
        assets = engine.game.getService('Assets')
        super().__init__(parent)
        self.name = 'TestEntity'
        self.image = assets.getImage('x')
        self.position = [320, 180]
        self.size = [0.5, 0.5]
        #self.gravity = False
        self.gravityVel = 0.0000000000000000001

class BaseGui(ScreenGui):
    def __init__(self, parent: object) -> None:
        super().__init__(parent)
        self.name = 'BaseGui'
    
    def update(self) -> None:
        self.writeText(f'FPS: 60', [0, 0], 1, (0, 0, 0), font='pixel')

obj = engine.game.getService('Object')
assets = engine.game.getService('Assets')
assets.loadImage('res/images/square.png', 'x')
assets.loadFont('res/fonts/DisposableDroidBB.ttf', 'pixel')
obj.new(TestEntity(engine.game.getService('Workspace')))
obj.new(BaseGui(engine.game.getService('GUIService')))

engine.mainloop()