import raylib as rl
from corpengine2 import colors
from corpengine2.objects import GameService

class Window(object):
    def __init__(self, parent: object) -> None:
        self.parent: object = parent
        self.backgroundColor: tuple = colors.CORPWHITE
        self.targetFPS: int = 60
    
    def setup(self) -> None:
        rl.SetConfigFlags(self.windowFlags)      
        rl.InitWindow(self.screenWidth, self.screenHeight, str.encode(self.title))
        rl.SetTargetFPS(self.targetFPS)

    def update(self) -> None:
        # Updating process
        # Drawing Process
        rl.BeginDrawing()
        rl.ClearBackground(self.backgroundColor)
        rl.EndDrawing()

class Engine(object):
    def __init__(self, screenWidth: int, screenHeight: int, title: str) -> None:
        self.window = Window(self)
        self.window.screenWidth = screenWidth
        self.window.screenHeight = screenHeight
        self.window.title = title
        self.window.windowFlags = 0
        self.status = None
        self.game = GameService(self)

        # built-in functions:
        self.setConfigFlags = rl.SetConfigFlags
        self.getFPS = rl.GetFPS
        self.setTargetFPS = rl.SetTargetFPS
        self.setStateFlags = rl.SetWindowState
        self.setWindowTitle = rl.SetWindowTitle
    
    def mainloop(self) -> None:
        self.window.setup()
        self.status = True
        while not rl.WindowShouldClose() and self.status:
            self.window.update()
        # de-initilization process
        rl.CloseWindow()
