import pygame

class Assets(object):
    def __init__(self, parent):
        self.parent = parent
        self.name = 'Assets'
        self.type = 'Assets'
        self.images = [
            ['player', pygame.image.load('res/images/player.png').convert()],
            ['dev_close', pygame.image.load('res/images/dev_close.png').convert()]
        ]
        self.fonts = {
            'hp_simplified': pygame.font.Font('res/fonts/hp-simplified.ttf', 15),
            'roboto_mono': pygame.font.Font('res/fonts/roboto-mono.ttf', 15)
        }
    
    def getImage(self, name):
        for image in self.images:
            if image[0] == name:
                return image[1].copy()
        return None
