import raylib as rl
from corpengine2.modules.colors import CORPWHITE
from corpengine2.modules.services import GameService
from corpengine2.modules.constants import ENGINE_VERSION

# built-in functions:
SetConfigFlags = rl.SetConfigFlags
GetFPS = rl.GetFPS
SetTargetFPS = rl.SetTargetFPS
SetStateFlags = rl.SetWindowState
SetWindowTitle = rl.SetWindowTitle
SetWindowMinimum = rl.SetWindowMinSize

def OpenErrorWindow(text: str, engine: object):
    callerFrame = sys._getframe(2)
    easygui.msgbox(
        f'file: {inspect.getmodule(callerFrame)} in line {callerFrame.f_lineno}\n\n -- {text}\n\nReach PyxleDev0 on github out with the error location to help me out.',
        'CORPEngine crashed!',
        'Ok'
    )
    engine.status = False
    sys.exit()

class Window(object):
    def __init__(self, parent: object):
        self.parent = parent
        self.__backgroundColor = CORPWHITE
    
    def _Setup(self):  
        rl.InitWindow(self.screenWidth, self.screenHeight, str.encode(self.title))
        iconImage = rl.LoadImage(b"corpengine2/res/icon.png") 
        rl.SetWindowIcon(iconImage)
        rl.UnloadImage(iconImage)
        print(f"----\nPowered by CORP Engine 2 v{ENGINE_VERSION}.\n----")

    def _Update(self):
        # Updating process
        # Drawing Process
        rl.BeginDrawing()
        rl.ClearBackground(self.__backgroundColor)
        rl.DrawFPS(20, 20)
        rl.EndDrawing()
    
    def SetBackgroundColor(self, color):
        self.__backgroundColor = color
        

class Engine(object):
    def __init__(self, screenWidth, screenHeight, title):
        self.window = Window(self)
        self.window.screenWidth = screenWidth
        self.window.screenHeight = screenHeight
        self.window.title = title
        self.status = None
        self.game = GameService(self)
    
    def Mainloop(self):
        self.window._Setup()
        self.status = True
        while not rl.WindowShouldClose() and self.status:
            self.window._Update()
        # de-initilization process
        rl.CloseWindow()

        assets = self.game.Assets

        textures = assets.textures
        for texture in textures:
            rl.UnloadTexture(textures[texture])
        
        images = assets.images
        for image in images:
            rl.UnloadImage(images[image])
