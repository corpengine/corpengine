
class GameObject(object):
    def __init__(self, parent: object) -> None:
        self.name = self.type = 'Object'
        self.parent: object = parent

    def setAttributeOfObject(self, object: object) -> None:
        if not hasattr(self, object.name):
            setattr(self, object.name, object)

    def getGameService(self) -> object:
        game = self.parent
        while game.type != 'GameService':
            game = game.parent
        return game

    def getEngine(self) -> object:
        engine = self.parent
        while engine.type != 'Engine':
            engine = engine.parent
        return engine

class Camera(GameObject):
    def __init__(self, parent: object) -> None:
        super().__init__(parent)
        self.name = self.type = 'Camera'
        self.position: list = [0, 0]
        self.fieldOfView: float = 100

class Entity(GameObject):
    def __init__(self, parent: object) -> None:
        super().__init__(parent)
        self.name = self.type = 'Entity'
        self.image = None
        self.position: list = [0, 0]
        self.render: bool = True
        self.children: list = []
        self.childrenQueue: list = []
        self.collisionGroup: int = 0
        self.size: list = [1, 1]
        self.rotation: float = 0

    def isColliding(self, name, parent='Workspace') -> bool:
        game = self.getGameService()
        workspace = game.getService('Workspace')
        if parent == 'Workspace':
            parentObj = workspace
        else:
            parentObj = parent
        # collision
        if parentObj != None:
            child = parentObj.getChild(name)
            if child != None:
                childRect = pygame.Rect(child.position[0], child.position[1], child.image.get_width(), child.image.get_height())
                childRect.width *= child.size[0]
                childRect.height *= child.size[1]
                selfRect = pygame.Rect(self.position[0], self.position[1], self.image.get_width(), self.image.get_height())
                selfRect.width *= self.size[0]
                selfRect.height *= self.size[1]
                return selfRect.colliderect(childRect)
        return False

    def getChild(self, name) -> object:
        try:
            return getattr(self, name)
        except Exception:
            for child in self.children:
                if child.name == name:
                    return child
            return None

    def _update(self) -> None:
        self.updateQueue()
        self.childrenEvents()

    def updateQueue(self) -> None:
        if len(self.childrenQueue) > 0:
            newChild = self.childrenQueue[0]
            self.children.append(self.childrenQueue[0])
            del self.childrenQueue[0]
            # SETUP/PARENT EVENTS:
            if hasattr(newChild, 'setup'):
                self.setAttributeOfObject(newChild)
                newChild.setup()

    def childrenEvents(self) -> None:
        window = self.getEngine().window
        for child in self.children:
            if hasattr(child, 'update'):
                child.update(window.dt)
                if child.type == 'ParticleEmitter':
                    if hasattr(child, 'update'):
                        child.update(window.dt)
                    child.render(window.dt)
            if hasattr(child, '_update'):
                child._update()

    def getChildren(self) -> list:
        return self.children.copy()


class GlobalScript(GameObject):
    def __init__(self, parent: object):
        super().__init__(parent)
        self.name = self.type = 'GlobalScript'

class ParticleEmitter(GameObject):
    def __init__(self, parent: object):
        super().__init__(parent)
        self.name = self.type = 'ParticleEmitter'
        self.children: list = []
        self.childrenQueue: list = []
        self.particleData: list= []
        # particle 2D list:
        # [pos, vel, color, size, acc, sizeAccel, shape, collidable, collisionGroup]

    def create(self, position: list, velocity: list, color: tuple, size:float, acceleration: tuple=(0, 0), sizeAccel: float=0, shape: str='circle', collidable: bool=False, collisionGroup: int=0) -> None:
        self.particleData.append([position, velocity, color, size, acceleration, sizeAccel, shape, collidable, collisionGroup])

    def updateParticleVelocity(self, particle: list, dt: float):
        game = self.getGameService()
        workspace = game.getService('Workspace')
        camX, camY = self.getCameraPosition(workspace)
        particle[1][0] += particle[4][0]*dt
        if particle[7]: # check if collidable
            for child in workspace.getChildren():
                if child.type == 'Entity' and child.collisionGroup == particle[8] and child.image != None:
                    self.particleCollision(child, particle, camX, camY, dt)
                if child.type == 'Folder':
                    for child2 in child.getChildren():
                        self.particleCollision(child2, particle, camX, camY, dt)
        else:
            particle[1][1] += particle[4][1]*dt

    def particleCollision(self, child: object, particle: list, camX: float, camY: float, dt: float) -> None:
        childRect = pygame.Rect(child.position[0], child.position[1], child.image.get_width(), child.image.get_height())
        childRect.width *= child.size[0]
        childRect.height *= child.size[1]
        childRect.x = (child.position[0] - camX)-childRect.width/2
        childRect.y = (child.position[1] - camY)-childRect.height/2
        selfRect = pygame.Rect(particle[0][0]-camX, particle[0][1]-camY, particle[3], particle[3])
        if childRect.colliderect(selfRect):
            # reset y velocity
            particle[0][1] -= particle[1][1]
            particle[1][1] = 0
        else:
            particle[1][1] += particle[4][1]*dt
        for child2 in child.getChildren():
            self.particleCollision(child2, particle, camX, camY, dt)


    def render(self, dt: float) -> None:
        # FIXME THIS PLACE HAS MAJOR CAMERA ISSUES AND MOSTLY NEEDS THE CAMERA POS TO BE MANUALLY ADDED BY THE USER.
        # FIX THIS!!!!!!!!
        game = self.getGameService()
        workspace = game.getService('Workspace')
        window = game.parent.window
        windowResolutionRatio = (window.screen.get_width()/constants.DEFAULTSCREENSIZE[0], window.screen.get_height()/constants.DEFAULTSCREENSIZE[1])
        renderService = game.getService('EngineRenderService')
        camX, camY = self.getCameraPosition(workspace)
        # updating the particles
        for particle in self.particleData:
            # update position
            particle[0][0] += particle[1][0]*dt
            particle[0][1] += particle[1][1]*dt
            self.updateParticleVelocity(particle, dt)
            # update size
            particle[3] += particle[5]*dt
            # delete any small particle
            if particle[3] < 0.1:
                self.particleData.remove(particle)

        # rendering
        for particle in self.particleData:
            if not particle[0][0] > constants.DEFAULTSCREENSIZE[0] and not particle[0][1] > constants.DEFAULTSCREENSIZE[1]:
                x = (particle[0][0]-camX) * windowResolutionRatio[0]
                y = (particle[0][1]-camY) * windowResolutionRatio[1]
                if particle[6] == 'circle':
                    pygame.draw.circle(window.particleWindow, particle[2], (x, y), particle[3] * windowResolutionRatio[1])
                elif particle[6] == 'rectangle':
                    size = particle[3]*windowResolutionRatio[1]
                    pygame.draw.rect(window.particleWindow, particle[2], (x, y, size, size))
                renderService.totalParticlesRendered += 1

    def getCameraPosition(self, workspace: object) -> tuple:
        if workspace.currentCamera != None:  # if a default camera exists:
            camX, camY = workspace.currentCamera.position
        else:
            camX, camY = (0, 0)
        return camX, camY

    def getChild(self, name) -> object:
        try:
            return getattr(self, name)
        except Exception:
            for child in self.children:
                if child.name == name:
                    return child
            return None

    def _update(self) -> None:
        self.updateQueue()
        self.childrenEvents()

    def updateQueue(self) -> None:
        if len(self.childrenQueue) > 0:
            newChild = self.childrenQueue[0]
            self.children.append(self.childrenQueue[0])
            del self.childrenQueue[0]
            # SETUP/PARENT EVENTS:
            if hasattr(newChild, 'setup'):
                self.setAttributeOfObject(newChild)
                newChild.setup()

    def childrenEvents(self) -> None:
        window = self.getEngine().window
        for child in self.children:
            if hasattr(child, 'update'):
                child.update(window.dt)
                if child.type == 'ParticleEmitter':
                    if hasattr(child, 'update'):
                        child.render(window.dt)
            if hasattr(child, '_update'):
                child._update()

    def getChildren(self) -> list:
        return self.children.copy()

class Raycaster(GameObject):
    def __init__(self, parent: object) -> None:
        super().__init__(parent)
        self.name = self.type = 'Raycaster'
        self.children: list = []
        self.childrenQueue: list = []

    def getCameraPosition(self, workspace: object) -> tuple:
        if workspace.currentCamera != None:  # if a default camera exists:
            camX, camY = workspace.currentCamera.position
        else:
            camX, camY = (0, 0)
        return camX, camY

    def getChild(self, name) -> object:
        try:
            return getattr(self, name)
        except Exception:
            for child in self.children:
                if child.name == name:
                    return child
            return None

    def _update(self) -> None:
        self.updateQueue()
        self.childrenEvents()

    def updateQueue(self) -> None:
        if len(self.childrenQueue) > 0:
            newChild = self.childrenQueue[0]
            self.children.append(self.childrenQueue[0])
            del self.childrenQueue[0]
            # SETUP/PARENT EVENTS:
            if hasattr(newChild, 'setup'):
                self.setAttributeOfObject(newChild)
                newChild.setup()

    def childrenEvents(self) -> None:
        window = self.getEngine().window
        for child in self.children:
            if hasattr(child, 'update'):
                child.update(window.dt)
                if child.type == 'ParticleEmitter':
                    if hasattr(child, 'update'):
                        child.render(window.dt)
            if hasattr(child, '_update'):
                child._update()

    def getChildren(self) -> list:
        return self.children.copy()

    def drawRect(self, color: tuple, rect, rounded: int=0) -> None:
        game = self.getGameService()
        window = game.parent.window
        windowResolutionRatio = (window.screen.get_width()/constants.DEFAULTSCREENSIZE[0], window.screen.get_height()/constants.DEFAULTSCREENSIZE[1])
        camX, camY = self.getCameraPosition(game.getService('Workspace'))

        newRect = rect.copy()
        x = (newRect.x - camX) * windowResolutionRatio[0]
        y = (newRect.y - camY) * windowResolutionRatio[1]
        w = newRect.width * windowResolutionRatio[1]
        h = newRect.height * windowResolutionRatio[1]
        pygame.draw.rect(window.renderWindow, color, (x, y, w, h), border_radius=rounded)

    def drawImage(self, name: str, position: list) -> None:
        game = self.getGameService()
        window = game.parent.window
        windowResolutionRatio = (window.screen.get_width()/constants.DEFAULTSCREENSIZE[0], window.screen.get_height()/constants.DEFAULTSCREENSIZE[1])
        assets = game.getService('Assets')
        camX, camY = self.getCameraPosition(game.getService('Workspace'))

        image = assets.getImage(name)
        pos = [position[0], position[1]]
        x = (pos[0] - camX) * windowResolutionRatio[0]
        y = (pos[1] - camY) * windowResolutionRatio[1]
        w = image.get_width() * windowResolutionRatio[1]
        h = image.get_height() * windowResolutionRatio[1]
        image = pygame.transform.scale(image, (w, h))
        window.renderWindow.blit(image, (x, y))

    def drawPolygon(self, color: tuple, points: list, outline: int=0) -> None:
        engine = self.getEngine()
        window = engine.window
        camX, camY = self.getCameraPosition(engine.game.Workspace)
        windowResolutionRatio = (window.screen.get_width() / constants.DEFAULTSCREENSIZE[0],window.screen.get_height() / constants.DEFAULTSCREENSIZE[1])
        newPoints = []
        for point in points:
            newPoints.append(((point[0]-camX)*windowResolutionRatio[0], (point[1]-camY)*windowResolutionRatio[1]))
        pygame.draw.polygon(engine.window.renderWindow, color, newPoints, outline)

class ScreenGui(GameObject):
    def __init__(self, parent: object) -> None:
        super().__init__(parent)
        self.name = self.type = 'ScreenGui'
        self.enabled: bool = True
        self.primaryRect: pygame.Rect = None
        self.offsetPosition: list = [0, 0]
        self.children: list = []
        self.childrenQueue: list = []

    def writeText(self, text: str, position: list, size: float, color: tuple, font: str='hp_simplified', backgroundColor: tuple=None) -> None:
        window = self.getEngine().window
        assets = self.getGameService().getService('Assets')
        fonts = assets.fonts
        windowResolutionRatio = (window.screen.get_width()/constants.DEFAULTSCREENSIZE[0], window.screen.get_height()/constants.DEFAULTSCREENSIZE[1])

        textObj = fonts[font].render(str(text), True, color, backgroundColor)
        newPosition = [position[0]+self.offsetPosition[0], position[1]+self.offsetPosition[1]]
        objSize = [textObj.get_width(), textObj.get_height()]
        textObj = pygame.transform.scale(textObj, (objSize[0]*size, objSize[1]*size))
        objSize = [textObj.get_width(), textObj.get_height()]
        textObj = pygame.transform.scale(textObj, (objSize[0]*windowResolutionRatio[1], objSize[1]*windowResolutionRatio[1]))
        x = newPosition[0]*windowResolutionRatio[0]
        y = newPosition[1]*windowResolutionRatio[1]
        textObj = textObj.convert_alpha()
        pos = [x, y]
        window.guiWindow.blit(textObj, pos)

    def drawRect(self, color: tuple, rect, rounded: int=0) -> None:
        game = self.getGameService()
        window = game.parent.window
        windowResolutionRatio = (window.screen.get_width()/constants.DEFAULTSCREENSIZE[0], window.screen.get_height()/constants.DEFAULTSCREENSIZE[1])

        newRect = rect.copy()
        x = (newRect.x + self.offsetPosition[0]) * windowResolutionRatio[0]
        y = (newRect.y + self.offsetPosition[1]) * windowResolutionRatio[1]
        w = newRect.width * windowResolutionRatio[1]
        h = newRect.height * windowResolutionRatio[1]
        pygame.draw.rect(window.guiWindow, color, (x, y, w, h), border_radius=rounded)

    def drawImage(self, name: str, position: list) -> None:
        game = self.getGameService()
        window = game.parent.window
        windowResolutionRatio = (window.screen.get_width()/constants.DEFAULTSCREENSIZE[0], window.screen.get_height()/constants.DEFAULTSCREENSIZE[1])
        assets = game.getService('Assets')

        image = assets.getImage(name)
        pos = [position[0], position[1]]
        x = (pos[0] + self.offsetPosition[0]) * windowResolutionRatio[0]
        y = (pos[1] + self.offsetPosition[1]) * windowResolutionRatio[1]
        w = image.get_width() * windowResolutionRatio[1]
        h = image.get_height() * windowResolutionRatio[1]
        image = pygame.transform.scale(image, (w, h))
        window.guiWindow.blit(image, (x, y))

    def drawCheckBox(self, value, position: list) -> None:
        game = self.getGameService()
        assets = game.getService('Assets')
        input = game.getService('UserInputService')
        debugValues = self.getEngine().settings.debugValues
        window = self.getEngine().window
        windowResolutionRatio = (window.screen.get_width()/constants.DEFAULTSCREENSIZE[0], window.screen.get_height()/constants.DEFAULTSCREENSIZE[1])

        if debugValues[value]:
            image = assets.getImage('checkbox_true')
        else:
            image = assets.getImage('checkbox_false')
        pos = [(position[0] + self.offsetPosition[0]) * windowResolutionRatio[0], (position[1] + self.offsetPosition[1]) * windowResolutionRatio[1]]

        # updating the value
        imageSize = [image.get_width(), image.get_height()]
        checkboxRect = pygame.Rect(pos[0], pos[1], imageSize[0]*windowResolutionRatio[1], imageSize[1]*windowResolutionRatio[1])
        mx, my = input.getMousePosition()
        if checkboxRect.collidepoint(mx, my) and input.mouseStatus[0]:
            debugValues[value] = not debugValues[value]

        # rendering
        image = pygame.transform.scale(image, (imageSize[0]*windowResolutionRatio[1], imageSize[1]*windowResolutionRatio[1]))
        window.guiWindow.blit(image, pos)

    def updateMouseFocus(self) -> None:
        if self.primaryRect != None and self.enabled:
            window = self.getEngine().window
            input = self.getGameService().getService('UserInputService')
            x = self.primaryRect.x + self.offsetPosition[0]
            y = self.primaryRect.y + self.offsetPosition[1]
            w = self.primaryRect.width
            h = self.primaryRect.height
            windowResolutionRatio = (window.screen.get_width()/constants.DEFAULTSCREENSIZE[0], window.screen.get_height()/constants.DEFAULTSCREENSIZE[1])
            rect = pygame.Rect(x*windowResolutionRatio[0], y*windowResolutionRatio[1], w*windowResolutionRatio[1], h*windowResolutionRatio[1])
            mx, my = input.getMousePosition()
            if rect.collidepoint(mx, my):
                input.mouseFocus = self.name
            else:
                input.mouseFocus = 'Game'
            # NOTE mouse focus may have some issues

    def _update(self) -> None:
        input = self.getGameService().getService('UserInputService')
        self.updateQueue()
        self.childrenEvents()
        self.updateMouseFocus()
        if not self.enabled and input.mouseFocus == self.name:
            input.mouseFocus = 'Game'

    def getChild(self, name: str) -> object:
        try:
            return getattr(self, name)
        except Exception:
            for child in self.children:
                if child.name == name:
                    return child
            return None

    def updateQueue(self) -> None:
        if len(self.childrenQueue) > 0:
            newChild = self.childrenQueue[0]
            self.children.append(self.childrenQueue[0])
            del self.childrenQueue[0]
            # SETUP/PARENT EVENTS:
            if hasattr(newChild, 'setup'):
                self.setAttributeOfObject(newChild)
                newChild.setup()

    def childrenEvents(self) -> None:
        window = self.getEngine().window
        for child in self.children:
            if hasattr(child, 'update'):
                child.update(window.dt)
                if child.type == 'ParticleEmitter':
                    if hasattr(child, 'update'):
                        child.update(window.dt)
                    child.render(window.dt)
            if hasattr(child, '_update'):
                child._update()

    def getChildren(self) -> list:
        return self.children.copy()

class Viewport(GameObject):
    def __init__(self, parent: object) -> None:
        super().__init__(parent)
        self.name = self.type = 'Viewport'
        self.background: list = [45, 45, 45]
        self.outline: float = 0
        self.size: list = [75, 50]
        self.enabled: bool = True
        self.transparency: int = 100
        self.position: list = [0, 0]
        self.children: list = []
        self.childrenQueue: list = []

    def updateViewport(self) -> None:
        engine = self.getEngine()
        window = engine.window

        surface = pygame.Surface(self.size)
        surface = surface.convert()
        surface.fill(self.background)
        # rendering object inside:
        windowResolutionRatio = [self.size[0]/constants.DEFAULTSCREENSIZE[0], self.size[1]/constants.DEFAULTSCREENSIZE[1]]

        for child in self.getChildren():
            if child.type == 'Entity' and child.image != None:
                pos = [child.position[0], child.position[1]]
                size = [child.image.get_width(), child.image.get_height()]
                size[0] *= windowResolutionRatio[1]
                size[1] *= windowResolutionRatio[1]
                img = pygame.transform.scale(child.image, size)
                img = pygame.transform.rotate(img, child.rotation)
                pos[0] *= windowResolutionRatio[0]
                pos[1] *= windowResolutionRatio[1]
                pos[0] -= img.get_width()/2
                pos[1] -= img.get_height()/2
                surface.blit(img, pos)

        window.gui_window.blit(surface, self.position)

    def getChild(self, name) -> object:
        try:
            return getattr(self, name)
        except Exception:
            for child in self.children:
                if child.name == name:
                    return child
            return None

    def _update(self) -> None:
        self.updateQueue()
        self.childrenEvents()
        if self.enabled:
            self.updateViewport()

    def updateQueue(self) -> None:
        if len(self.childrenQueue) > 0:
            newChild = self.childrenQueue[0]
            self.children.append(self.childrenQueue[0])
            del self.childrenQueue[0]
            # SETUP/PARENT EVENTS:
            if hasattr(newChild, 'setup'):
                self.setAttributeOfObject(newChild)
                newChild.setup()

    def childrenEvents(self) -> None:
        window = self.getEngine().window
        for child in self.children:
            if hasattr(child, 'update'):
                child.update(window.dt)
                if child.type == 'ParticleEmitter':
                    if hasattr(child, 'update'):
                        child.render(window.dt)
            if hasattr(child, '_update'):
                child._update()

    def getChildren(self) -> list:
        return self.children.copy()

class Folder(GameObject):
    def __init__(self, parent: object) -> None:
        super().__init__(parent)
        self.name = self.type = 'Folder'
        self.children: list = []
        self.childrenQueue: list = []

    def getChild(self, name: str) -> object:
        try:
            return getattr(self, name)
        except Exception:
            for child in self.children:
                if child.name == name:
                    return child
            return None

    def _update(self) -> None:
        self.updateQueue()
        self.childrenEvents()

    def updateQueue(self) -> None:
        if len(self.childrenQueue) > 0:
            newChild = self.childrenQueue[0]
            self.children.append(self.childrenQueue[0])
            del self.childrenQueue[0]
            # SETUP/PARENT EVENTS:
            if hasattr(newChild, 'setup'):
                self.setAttributeOfObject(newChild)
                newChild.setup()

    def childrenEvents(self) -> None:
        window = self.getEngine().window
        for child in self.children:
            if hasattr(child, 'update'):
                if child.type == 'ScreenGUI':
                    if child.enabled:
                        child.update(window.dt)
                else:
                    child.update(window.dt)
                if child.type == 'ParticleEmitter':
                    child.render(window.dt)
            if hasattr(child, '_update'):
                child._update()

    def getChildren(self) -> list:
        return self.children.copy()