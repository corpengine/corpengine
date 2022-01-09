import pygame
from src.CORPEngine.window import Window
from src.CORPEngine.services.gameService import GameService
from src.CORPEngine.coreContent import engineVersion
from src.settings import Settings

class Engine:
    def __init__(self):
        self.type = 'Engine'
        self.window = Window(self)
        self.game = GameService(self)
        self.settings = Settings(self)
        self.running = False

    def run(self):
        self.window.setup()
        self.running = True
        while self.running:
            self.window.update()

if __name__ =='__main__':
    print(f'[CORP] Engine {engineVersion} - Made by DaGhostyBoi.')
    print(f'pygame version: v{pygame.version.ver}   SDL version: {pygame.version.SDL}')
    Engine().run()
