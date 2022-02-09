from corpengine2 import *

engine = InitEngine(960, 540, "Corporation")

class Test(Entity):
    def Setup(self):
        print("Setup event")
        self.texture = None
    
    def Update(self):
        pass

NewObject(Test(engine.game.Workspace))

engine.Mainloop()
