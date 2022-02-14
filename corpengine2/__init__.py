from corpengine2.modules.colors import *
from corpengine2.modules.constants import *
from corpengine2.modules.version import *
from corpengine2.modules.core import *
from corpengine2.modules.objects import *
from corpengine2.modules.components import *

def InitEngine(screenWidth=960, screenHeight=540, title="CORP Engine 2 Window"):
    """Initialize the Engine"""    
    return Engine(screenWidth, screenHeight, title)
