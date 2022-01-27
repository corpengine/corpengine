# This is a CORP Engine example about getting keyboard input and
# using it to move an Entity.

# Importing -----------------------------------------------------|
import corpengine1 as corp

# Initilization -------------------------------------------------|
engine = corp.init(windowTitle='Examples - Keyboard Input', windowSize=(960, 720))

# Entity Class --------------------------------------------------|
class MyEntity(corp.Entity):
    def setup(self) -> None:
        assets = engine.game.Assets
        assets.loadImage('images/square.png')

    def update(self, deltaTime: float) -> None:
        pass


# Adding objects -----------------------------------------------|
print(engine.game.Object)
workspace = engine.game.Workspace

# Mainloop ------------------------------------------------------|
engine.mainloop()