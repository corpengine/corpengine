from corpengine2 import *

Engine = InitEngine(960, 540, "Corporation")
Game = Engine.Game

Player = NewGameObject("Player", Engine)

class Test(ScriptComponent):
    def Setup(self):
        pass
    
    def Update(self):
        print("test")

Player.AddComponent(Test)

Engine.Mainloop()
