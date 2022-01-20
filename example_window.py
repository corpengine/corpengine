# Import CORP Engine
import corpengine
from corpengine import flags, Entity

engine = corpengine.init(windowTitle='Example Window', flags=flags.RESIZABLE)

class Test(corpengine.Entity):
    def __init__(self, parent: object) -> None:
        super().__init__(parent)

    def setup(self) -> None:
        self.image = engine.game.getService('Assets').getImage('icon')
        self.position = [320, 180]

    def update(self, dt: float) -> None:
        input = engine.game.getService('UserInputService')
        print(input.isCollidingWithMouse(self))


class TestCamera(corpengine.Camera):
    def __init__(self, parent: object) -> None:
        super().__init__(parent)
        self.position = [100, 100]

obj = engine.game.getService('Object')
obj.new(Test(engine.game.getService('Workspace')))
obj.new(TestCamera(engine.game.getService('Workspace')))

engine.window.setTargetFPS(144)
engine.mainloop()