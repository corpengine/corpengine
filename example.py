from corp import *

Engine = InitEngine()

class TempComponent(Script):
    def Update(self):
        print("Nice")


Player = Engine.Game.ObjectService.New(
    "Player",
    Engine.Game.Workspace
)

Player.AddComponent(TempComponent)

Engine.Mainloop()