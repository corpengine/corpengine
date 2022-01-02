
class ScriptService(object):
    def __init__(self, parent):
        self.parent = parent
        self.name = 'ScriptService'
        self.type = 'ScriptService'
        self.children = []
        self.childrenQueue = []

    def getChild(self, name):
        for child in self.children:
            if child.name == name:
                return child
        return None
    
    def update(self):
        self.updateQueue()
        self.childrenEvents()

    def updateQueue(self):
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
        window = self.parent.parent.window
        for child in self.children:
            if hasattr(child, 'update') and child.type == 'GlobalScript':
                child.update(window.dt)
    
    def getChildren(self):
        return self.children