import corpengine
from corpengine import flags

engine = corpengine.init(windowTitle='Example Window', flags=flags.RESIZABLE)

engine.mainloop()
