from corpengine2 import *

Engine = InitEngine(960, 540, "Corporation")
Game = Engine.game  # TODO change the game to be capitalized

class PlayerScriptComponent(ScriptComponent):
    def Setup(self):
        self.parent.position = Vector2(480, 270)
        self.parent.texture = Game.Assets.LoadTexture("test", "stone.png")
    
    def Update(self):
        return
        print(self.parent.texture)

Player = NewEntity("Player", Game.Workspace)
Player.AddComponent(PlayerScriptComponent)

Engine.Mainloop()
