import pygame

class Object:
    def __init__(self, parent):
        self.name = 'Object'
        self.type = 'Object'
        self.parent = parent
    
    def new(self, object, parent):
        workspace = self.parent.getService('Workspace')
        newObject = object(parent)
        workspace.childrenQueue.append(newObject)
