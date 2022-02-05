import raylib as rl
import easygui
import inspect
import sys
from corpengine2 import colors

def openErrorWindow(text: str, engine: object) -> None:
    callerFrame = sys._getframe(2)
    easygui.msgbox(
        f'file: {inspect.getmodule(callerFrame)} in line {callerFrame.f_lineno}\n\n -- {text}\n\nReach PyxleDev0 on github out with the error location to help me out.',
        'CORPEngine crashed!',
        'Ok'
    )
    engine.status = False
    sys.exit()

class GameObject(object):
    def __init__(self, parent: object) -> None:
        self.parent: object = parent
        self.name = type(self).__name__

class Window(object):
    def __init__(self, parent: object) -> None:
        self.parent: object = parent
        self.backgroundColor: tuple = colors.CORPWHITE
        self.targetFPS: int = 60
    
    def setup(self) -> None:
        rl.SetConfigFlags(self.windowFlags)      
        rl.InitWindow(self.screenWidth, self.screenHeight, str.encode(self.title))
        rl.SetTargetFPS(self.targetFPS)
        iconImg = rl.LoadImage(b"resources/icon.png")
        rl.SetWindowIcon(iconImg)
        rl.UnloadImage(iconImg)

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
