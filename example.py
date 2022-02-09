import corpengine2 as cp

engine = cp.init(800, 500, "CORPORATION")

engine.setConfigFlags(cp.constants.FLAG_WINDOW_RESIZABLE)

engine.mainloop()
