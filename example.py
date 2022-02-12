from corpengine2 import *

Engine = InitEngine(960, 540, "Corporation")
Game = Engine.Game

Player = GameObject(Engine.Game.Workspace)
print(Player.GetComponents())

class TestComponent(ScriptComponent):
    def Update(self):
        print("nice")

Player.AddComponent(TestComponent)

Engine.Mainloop()
