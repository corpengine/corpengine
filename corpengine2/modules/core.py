import raylib as rl
from pyray import Image
from corpengine2.modules.colors import CORPWHITE
from corpengine2.objects import GameService
from corpengine2.modules.constants import ENGINE_VERSION

# built-in functions:
SetConfigFlags = rl.SetConfigFlags
GetFPS = rl.GetFPS
SetTargetFPS = rl.SetTargetFPS
SetStateFlags = rl.SetWindowState
SetWindowTitle = rl.SetWindowTitle
SetWindowMinimum = rl.SetWindowMinSize

class Window(object):
    def __init__(self, parent: object):
        self.parent = parent
        self.backgroundColor = CORPWHITE
        self.targetFPS = 60
    
    def Setup(self):
        rl.SetConfigFlags(self.windowFlags)      
        rl.InitWindow(self.screenWidth, self.screenHeight, str.encode(self.title))
        iconImage: Image = rl.LoadImage(b"corpengine2/res/icon.png") 
        rl.SetWindowIcon(iconImage)
        rl.UnloadImage(iconImage)
        print(f"----\nPowered by CORP Engine 2 v{ENGINE_VERSION}.\n----")

    def Update(self):
        # Updating process
        # Drawing Process
        rl.BeginDrawing()
        rl.ClearBackground(self.backgroundColor)
        rl.DrawFPS(20, 20)
        rl.EndDrawing()

class Engine(object):
    def __init__(self, screenWidth: int, screenHeight: int, title: str):
        self.window = Window(self)
        self.window.screenWidth = screenWidth
        self.window.screenHeight = screenHeight
        self.window.title = title
        self.window.windowFlags = 0
        self.status = None
        self.game = GameService(self)
    
    def Mainloop(self):
        self.window.Setup()
        self.status = True
        while not rl.WindowShouldClose() and self.status:
            self.window.Update()
        # de-initilization process
        rl.CloseWindow()

        assets = self.game.Assets

        textures = assets.textures
        for texture in textures:
            rl.UnloadTexture(textures[texture])
        
        images = assets.images
        for image in images:
            rl.UnloadImage(images[image])
