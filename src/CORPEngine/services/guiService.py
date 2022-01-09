from ...Scripts.gui.guiFolder import GuiFolder
from ...Scripts.gui.testViewport import TestViewport

class GUIService(object):
    def __init__(self, parent):
        self.name = 'GUIService'
        self.type = 'GUIService'
        self.parent = parent
        self.children = []
        self.childrenQueue = [GuiFolder(self), TestViewport(self)]
    
    def update(self):
        self.updateQueue()
        self.childrenEvents()
    
    def updateQueue(self):
        # load the next member of the queue
        if len(self.childrenQueue) > 0:
            newChild = self.childrenQueue[0]
            self.children.append(self.childrenQueue[0])
            del self.childrenQueue[0]
            # SETUP/PARENT EVENTS:
            # if the child came from another parent
            if newChild.parent != self:
                if hasattr(newChild, 'parentChanged'):
                    newChild.parentChanged()
            else: # if the child is brand new
                if hasattr(newChild, 'setup'):
                    newChild.setup()

    def childrenEvents(self):
        for child in self.children:
            if hasattr(child, 'update') and child.enabled == True:
                child.update()
            child._update()
    
    def getChild(self, name):
        for child in self.children:
            if child.name == name:
                return child
        return None
