class Component(object):
    def __init__(self, parent):
        self.parent = parent

class ScriptComponent(Component):
    def __init__(self, parent):
        super().__init__(parent)
