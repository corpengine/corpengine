import random
import corpengine
from corpengine import flags, colors, GlobalScript, constants, ScreenGui

engine = corpengine.init(windowTitle='Colors', windowSize=(500, 500))

class ColorChanger(GlobalScript):
    def __init__(self, parent: object) -> None:
        super().__init__(parent)
        self.name = 'ColorChanger'
        self.colors = ['AQUA', 'BABYBLUE', 'GREEN', 'RED', 'MAGENTA']
    
    def update(self, dt: float) -> None:
        input = self.getGameService().getService('UserInputService')
        if input.isMouseButtonPressed('left'):
            constants.BACKGROUND_COLOR = getattr(colors, random.choice(self.colors))

class BaseGui(ScreenGui):
    def __init__(self, parent: object) -> None:
        super().__init__(parent)
        self.name = 'BaseGui'
    
    def update(self) -> None:
        self.writeText(f'Color: {constants.BACKGROUND_COLOR}', [0, 0], 1, (0, 0, 0), font='pixel')

scriptService = engine.game.getService('ScriptService')
guiService = engine.game.getService('GUIService')

scriptService.childrenQueue.append(ColorChanger(scriptService))
guiService.childrenQueue.append(BaseGui(guiService))

constants.BACKGROUND_COLOR = colors.RED
engine.game.getService('Assets').loadFont('res/fonts/rainyhearts.ttf', 'pixel')

engine.mainloop()
