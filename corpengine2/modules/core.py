import raylib as rl
import sys, inspect, easygui
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
SetExitKey = rl.SetExitKey

def OpenErrorWindow(text: str, engine: object):
    callerFrame = sys._getframe(2)
    easygui.msgbox(
        f'file: {inspect.getmodule(callerFrame)} in line {callerFrame.f_lineno}\n\n -- {text}\n\nReach PyxleDev0 on github out with the error location to help me out.',
        'CORPEngine crashed!',
        'Ok'
    )
    engine.status = False
    sys.exit()

def GetDeltaTime():
    return rl.GetFrameTime() * 60
    # Maybe make the delta multiplied with the Target FPS
    # instead of 60?

def NewObject(object):
    objParent = object.parent
    objParent._AddChild(object)

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
        game = self.parent.game
        game._Update()
        # Drawing Process
        rl.BeginDrawing()
        rl.ClearBackground(self.__backgroundColor)
        game.EngineRenderService._Render()
        rl.DrawFPS(20, 20)
        rl.EndDrawing()
    
    def SetBackgroundColor(self, color):
        self.__backgroundColor = color
    
    def GetBackgroundColor(self):
        return self.__backgroundColor
    

class Engine(object):
    def __init__(self, screenWidth, screenHeight, title):
        self._type = "Engine"
        self.window = Window(self)
        self.window.screenWidth = screenWidth
        self.window.screenHeight = screenHeight
        self.window.title = title
        self.status = None
        self.game = GameService(self)
        
        self.window._Setup()
    
    def Mainloop(self):
        self.status = True
        while not rl.WindowShouldClose() and self.status:
            self.window._Update()
        # De-initilization process
        rl.CloseWindow()

        assets = self.game.Assets

        textures = assets.textures
        for texture in textures:
            rl.UnloadTexture(textures[texture])
        
        images = assets.images
        for image in images:
            rl.UnloadImage(images[image])
