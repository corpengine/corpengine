import raylib as rl
from pyray import Image
from corpengine2 import colors
from corpengine2.objects import GameService
from corpengine2.constants import ENGINE_VERSION

class Window(object):
    def __init__(self, parent: object):
        self.parent = parent
        self.backgroundColor = colors.CORPWHITE
        self.targetFPS = 60
    
    def setup(self):
        rl.SetConfigFlags(self.windowFlags)      
        rl.InitWindow(self.screenWidth, self.screenHeight, str.encode(self.title))
        rl.SetTargetFPS(self.targetFPS)
        iconImage: Image = rl.LoadImage(b"corpengine2/res/icon.png") 
        rl.SetWindowIcon(iconImage)
        rl.UnloadImage(iconImage)
        print(f"----\nPowered by CORP Engine 2 v{ENGINE_VERSION}.\n----")

    def update(self):
        # Updating process
        # Drawing Process
        rl.BeginDrawing()
        rl.ClearBackground(self.backgroundColor)
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

        # built-in functions:
        self.setConfigFlags = rl.SetConfigFlags
        self.getFPS = rl.GetFPS
        self.setTargetFPS = rl.SetTargetFPS
        self.setStateFlags = rl.SetWindowState
        self.setWindowTitle = rl.SetWindowTitle
        self.setWindowMinimum = rl.SetWindowMinSize
    
    def mainloop(self):
        self.window.setup()
        self.status = True
        while not rl.WindowShouldClose() and self.status:
            self.window.update()
        # de-initilization process
        rl.CloseWindow()

        assets = self.game.assets

        textures = assets.textures
        for texture in textures:
            rl.UnloadTexture(textures[texture])
        
        images = assets.images
        for image in images:
            rl.UnloadImage(images[image])
