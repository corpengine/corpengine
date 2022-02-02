from corpengine1 import constants

def getSDLVersion() -> str:
    return pygame.version.SDL


def getPygameVersion() -> str:
    return pygame.version.ver


def getEngineVersion() -> str:
    return constants.ENGINEVERSION