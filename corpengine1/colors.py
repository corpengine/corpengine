
# Pytility @LercDsgn - thanks for the credit, pyxle :p
def mix(*colors: tuple) -> tuple:
    res = [0] * 3
    for color in colors:
        for index, param in enumerate(color):
            if res[index] + param < 256 and res[index] + param > -1:  # 1.2.dev3: fixed value range checking
                res[index] += param
    return tuple(res)

def all(value) -> tuple:
    return tuple([value] * 3)

def onlyFill(place, value=255) -> tuple:
    colors = [0] * 3
    colors[place] = value
    return tuple(colors)

def onlyEmpty(place, value=0):
    colors = [255] * 3
    colors[place] = value
    return tuple(colors)

# Black-White (r = g = b)
WHITE = all(255)
CORPWHITE = all(224)
LIGHTGRAY = all(211)
SILVER = all(192)
GRAY = all(128)
DARKGRAY = all(64)
BLACK = all(0)

# Single Colors (Full)
RED = onlyFill(0)
LIME = onlyFill(1)
BLUE = onlyFill(2)

# Single Colors (Toned)
DARKGREEN = onlyFill(2, 100)
DARKRED = onlyFill(1, 139)
GREEN = onlyFill(2, 128)

# Double Colors (Full)
MAGENTA = mix(RED, BLUE)  # onlyEmpty(2)
AQUA = mix(LIME, BLUE)  # onlyEmpty(1)
YELLOW = mix(RED,LIME)  # onlyEmpty(3)

# Double colors (Toned)
LIGHTBLUE = (0, 150, 255)
ORANGE = (255, 170, 0)

# Triple Colors (Toned)
VIOLET = (238, 130, 238)
TAN = (210, 180, 140)
FORESTGREEN = (39, 139, 34)
BABYBLUE = (137, 207, 240)
PINK = (255, 105, 180)
BROWN = (139, 69, 19)
