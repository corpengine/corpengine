import corpengine
from corpengine import flags, ScreenGui, Entity

engine = corpengine.init(windowTitle='Window', flags=flags.SCALED)

class BaseGui(ScreenGui):
    def __init__(self, parent: object) -> None:
        super().__init__(parent)
        self.name = 'BaseGui'
    
    def update(self) -> None:
        self.writeText(f'FPS: {engine.window.getFPS()}', [0, 0], 1, (0, 0, 0), font='pixel')

class Test(Entity):
    def __init__(self, parent: object) -> None:
        super().__init__(parent)
        self.velocity = [0, 0]
    
    def setup(self) -> None:
        assets = engine.game.getService('Assets')
        self.image = assets.getImage('icon')
        self.position = [320, 180]
    
    def update(self, dt: float) -> None:
        input = engine.game.getService('UserInputService')
        self.position[0] += input.getControllerAxis(0, 0)*7*dt
        self.position[1] += input.getControllerAxis(0, 1)*7*dt

obj = engine.game.getService('Object')
assets = engine.game.getService('Assets')
assets.loadImage('res/images/square.png', 'x')
assets.loadFont('res/fonts/DisposableDroidBB.ttf', 'pixel')
obj.new(BaseGui(engine.game.getService('GUIService')))
obj.new(Test(engine.game.getService('Workspace')))

input = engine.game.getService('UserInputService')
print(input.getControllerName(0))
print(input.getControllerPowerLevel(0))

engine.mainloop()