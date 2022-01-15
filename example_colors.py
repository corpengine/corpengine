# This is a CORP Engine example about the usage of colors, constants and objects.

# Importing ----------------------------------------------------------------|
import random
import corpengine
from corpengine import flags, colors, GlobalScript, constants, ScreenGui

# Initialization -----------------------------------------------------------|
engine = corpengine.init(windowTitle='Examples - Colors', windowSize=(500, 500))

# Object classes -----------------------------------------------------------|
class ColorChanger(GlobalScript):
    def __init__(self, parent: object) -> None:
        super().__init__(parent)
        self.name = 'ColorChanger'
        self.colors = ['AQUA', 'BABYBLUE', 'GREEN', 'RED', 'MAGENTA']  # colors to be used
    
    def update(self, dt: float) -> None:
        input = self.getGameService().getService('UserInputService')  # get input service
        # check for left mouse button press
        if input.isMouseButtonPressed('left'):
            # change the background color to a random color
            constants.BACKGROUND_COLOR = getattr(colors, random.choice(self.colors))

class BaseGui(ScreenGui):
    def __init__(self, parent: object) -> None:
        super().__init__(parent)
        self.name = 'BaseGui'
    
    def update(self) -> None:
        # Writing
        self.writeText(f'Color RGB: {constants.BACKGROUND_COLOR}', [0, 0], 1, (0, 0, 0), font='pixel')
        self.writeText('Click to pick a random color!', [0, 32], 0.85, (0, 0, 0), font='pixel')

# Getting services --------------------------------------------------------|
scriptService = engine.game.getService('ScriptService')
guiService = engine.game.getService('GUIService')
assets = engine.game.getService('Assets')
obj = engine.game.getService('Object')

# Adding objects ----------------------------------------------------------|
obj.new(ColorChanger(scriptService), scriptService)
obj.new(BaseGui(guiService), guiService)

constants.BACKGROUND_COLOR = colors.RED
assets.loadFont('res/fonts/rainyhearts.ttf', 'pixel', size=32, bold=True)

engine.mainloop()
