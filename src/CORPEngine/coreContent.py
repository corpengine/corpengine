import sys, inspect, easygui

engineVersion = '0.1.4a'
gameVersion = '1.0'
defaultScreenSize = (640, 360)
availableResolutions = ((640, 360), (1280, 720), (1024, 576), (1152, 648), (1366, 768))

def cprint(value):
    caller_frame = sys._getframe(1)
    a = ' '*24
    print(f'{value} {a} -- {inspect.getmodule(caller_frame)}')

def openErrorWindow(text, engine):
    callerFrame = sys._getframe(1)
    easygui.msgbox(f'file: {inspect.getmodule(callerFrame)} in line {callerFrame.f_lineno}\n\n -- {text}\n\nReach PyxleDev0 on github out with the error location to help me out.', 'CORPEngine crashed!')
    engine.running = False