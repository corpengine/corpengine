from corpengine2 import *

Engine = InitEngine(960, 540, "CORP Engine 2 Window")

class TestComponent(Script):
    def Update(self):
        print(self.parent.Transform.position.x)

Player = NewEntity("Player", Engine)
Player.AddComponent(TestComponent)

Engine.Mainloop()
