import corpengine as corp

engine = corp.init(flags=corp.flags.SCALED)

class Test(corp.Entity):
    def __init__(self, parent):
        super().__init__(parent)

    def setup(self):
        corp.TestComponent().add(self)

    def update(self, dt):
        print(self.foo(5))

engine.game.Object.new(Test(engine.game.Workspace))

engine.mainloop()