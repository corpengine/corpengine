import pygame
from .constants import ENGINEVERSION

def getSDLVersion() -> str:
    return pygame.version.SDL

def getPygameVersion() -> str:
    return pygame.version.ver

def getEngineVersion() -> str:
    return ENGINEVERSION
