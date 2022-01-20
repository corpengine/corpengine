# Import CORP Engine
import corpengine
from corpengine import flags

engine = corpengine.init(windowTitle='Example Window', flags=flags.RESIZABLE)
engine.window.setTargetFPS(144)
print(corpengine.version('sdl'))
engine.mainloop()