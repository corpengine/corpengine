from corpengine2 import *

engine = InitEngine(960, 540, "Corporation")

class Test(Entity):
    def Setup(self):
        print("Setup event")
    
    def Update(self):
        print("Update event")

engine.game.Object.New(Test(engine.game.Workspace))

engine.Mainloop()
