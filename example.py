from corpengine2 import *

Engine = InitEngine(960, 540, "Corporation")
Game = Engine.game  # TODO change the game to be capitalized

Player = NewEntity("Player", Game.Workspace, Game.Assets.LoadTexture("stone", "stone.png"))

Engine.Mainloop()
