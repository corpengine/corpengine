from corpengine2 import *

Engine = InitEngine(960, 540, "CORP Engine 2 Window")

class TestComponent(Script):
    def Update(self):
        print(self.parent.Transform.position.x)
        if IsKeyPressed(KEY_A):
            self.parent.Texture.enabled = False

Player = NewEntity("Player", Engine, Engine.Game.Assets.LoadTexture(" ", "stone.png"))
Player.AddComponent(TestComponent)

Engine.Mainloop()
