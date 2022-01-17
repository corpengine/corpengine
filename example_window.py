import corpengine
from corpengine import flags, PhysicsEntity, Entity

engine = corpengine.init(windowTitle='Window', flags=flags.SCALED)

class TestEntity(PhysicsEntity):
    def __init__(self, parent: object) -> None:
        assets = engine.game.getService('Assets')
        super().__init__(parent)
        self.name = 'TestEntity'
        self.image = assets.getImage('icon')
        self.position = [320, 180]
        self.size = [0.5, 0.5]

obj = engine.game.getService('Object')
obj.new(TestEntity(engine.game.getService('Workspace')))

engine.mainloop()