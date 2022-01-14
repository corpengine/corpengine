import corpengine
from corpengine import flags

engine = corpengine.init(flags=flags.SCALED)
engine.mainloop()