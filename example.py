from corpengine2 import *

Engine = InitEngine()

class TempComponent(Script):
    def Update(self):
        print("Nice")


"""
Player = NewEntity(
    "Player",
    Engine,
    Engine.Game.Assets.LoadTexture("player", "stone.png"),
    position=Vector2(GetScreenWidth()/2-16, GetScreenHeight()/2-16)
)

Box = NewEntity("Box", Engine, Engine.Game.Assets.LoadTexture("box", "corpengine2/res/icon.png"), position=Vector2(55, 56))
"""
Player = Engine.Game.ObjectService.New(
    "Player",
    Engine.Game.Workspace
)

Player.AddComponent(TempComponent)

Engine.Mainloop()