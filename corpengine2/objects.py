import raylib as rl
from pyray import Image
from typing import Final
import easygui
import inspect
import sys

def openErrorWindow(text: str, engine: object) -> None:
    callerFrame = sys._getframe(2)
    easygui.msgbox(
        f'file: {inspect.getmodule(callerFrame)} in line {callerFrame.f_lineno}\n\n -- {text}\n\nReach PyxleDev0 on github out with the error location to help me out.',
        'CORPEngine crashed!',
        'Ok'
    )
    engine.status = False
    sys.exit()

class GameObject(object):
    def __init__(self, parent: object) -> None:
        self.parent: object = parent
        self.name = type(self).__name__

class GameService(GameObject):
    def __init__(self, parent: object) -> None:
        super().__init__(parent)
        self.type: Final = "GameService"

class Assets(GameObject):
    def __init__(self, parent: object) -> None:
        super().__init__(parent)
        self.type: Final = "Assets"
        self.images: dict = {}
        self.textures: dict = {}
    
    def getImage(self, name: str) -> Image:
        try:
            return self.images[name]
        except Exception:
            openErrorWindow(f"No such image with name \"{name}\"", engine)
    
    def loadImage(self, name: str, path: str) -> None:
        try:
            self.images.update({name: rl.LoadImage(path)})
        except Exception:
            openErrorWindow("Invalid path for image or file unsupported.", self.parent.parent)
