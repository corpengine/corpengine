
class GlobalScript(object):
    def __init__(self, parent):
        self.name = 'GlobalScript'
        self.type = 'GlobalScript'
        self.parent = parent
    
    def getGameService(self):
        game = self.parent
        while game.type != 'GameService':
            game = game.parent
        return game
