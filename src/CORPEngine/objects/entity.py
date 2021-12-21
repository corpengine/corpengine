from ..coreContent import *

class Entity(object):
    def __init__(self, parent):
        self.parent = parent
        self.name = 'Entity'
        self.type = 'Entity'
        self.image = None
        self.position = [0, 0]
        self.render = True
        self.children = []
    
    def getChild(self, name):
        for child in self.children:
            if child.name == name:
                return child
        raise SyntaxError
    
    def getChildren(self):
        return self.children
