from corpengine2 import *

InitEngine()

Player = NewEntity("Player", Engine)

class Temp(Script):
    def Update(self):
        print("I'm annoying you haha")
        if IsKeyPressed(KEY_SPACE):
            print("noo :(")
            self.parent.RemoveComponent("Script")

Player.AddComponent(Temp)
Engine.Mainloop()