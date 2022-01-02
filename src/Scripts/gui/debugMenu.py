from ...CORPEngine.objects.screenGui import ScreenGui
from ...CORPEngine.coreContent import *

class DebugMenu(ScreenGui):
    def __init__(self, parent):
        super().__init__(parent)
        self.name = 'DebugMenu'
    
    def setup(self):
        self.enabled = False
    
    def update(self, dt):
        game = self.getGameService()
        window = game.parent.window
        renderService = game.getService('EngineRenderService')
        res = window.screen.get_size()
        if renderService != None:
            debugValues = [
                f'fps: {round(window.clock.get_fps())} - {window.performance}', f'engine info: CORP Engine v{engineVersion}', f'game version: {gameVersion}',
                f'total entities rendered: {renderService.totalEntitiesRendered}', f'total particles rendered: {renderService.totalParticlesRendered}',
                f'resolution: {res[0]}x{res[1]}'
            ]
            y = 0
            for value in debugValues:
                self.writeText(value, [0, y], 1, (0, 0, 0))
                y += 13
