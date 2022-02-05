from corpengine2 import colors, constants, core, version

def init(screenWidth: int, screenHeight: int, title: str) -> core.Engine:
    return core.Engine(screenWidth, screenHeight, title)
