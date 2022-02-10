from corpengine2.modules.colors import *
from corpengine2.modules.constants import *
from corpengine2.modules.version import *
from corpengine2.modules.core import *
from corpengine2.modules.objects import *
from corpengine2.modules.components import *

def InitEngine(screenWidth, screenHeight, title):
    """Initialize an Engine class"""    
    return Engine(screenWidth, screenHeight, title)
