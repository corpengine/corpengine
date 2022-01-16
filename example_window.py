import corpengine
from corpengine import flags

engine = corpengine.init(windowTitle='Window', flags=flags.SCALED)

engine.mainloop()