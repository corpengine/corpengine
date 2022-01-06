from ..coreContent import openErrorWindow

class Camera(object):
    def __init__(self, parent):
        self.parent = parent
        self.name = 'Camera'
        self.type = 'Camera'
        self.position = [0, 0]
        self.attributes = {}
    
    def setAttribute(self, name, val):
        self.attributes.update({name: val})
    
    def getAttribute(self, name):
        try:
            return self.attributes[name]
        except Exception:
            openErrorWindow(f'unknown attribute "{name}".', self.getEngine())

    def getEngine(self):
        engine = self.parent
        while engine.type != 'Engine':
            engine = engine.parent
        return engine