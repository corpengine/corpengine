import raylib as rl
from corpengine2.modules import constants

GetRaylibVersion = rl.rlGetVersion()

def GetEngineVersion():
    return constants.ENGINE_VERSION
