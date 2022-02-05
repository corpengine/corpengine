import raylib as rl
from pyray import Image
from corpengine2.core import GameObject, openErrorWindow
from typing import Final

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
