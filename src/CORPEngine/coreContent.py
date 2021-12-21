import sys, inspect

engineVersion = '0.1.0'
gameVersion = '1.0'
defaultScreenSize = (640, 360)
availableResolutions = ((640, 360), (1280, 720), (1024, 576), (1152, 648), (1366, 768))

def cprint(value):
    caller_frame = sys._getframe(1)
    a = ' '*24
    print(f'{value} {a} -- {inspect.getmodule(caller_frame)}')