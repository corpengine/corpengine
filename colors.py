# taken from https://github.com/LercDsgn/pytility/blob/main/colors
 def mix(*colors: tuple) -> tuple:
    res = [0]*3
    for color in colors:
        for index, param in enumerate(color):   
            if 0 > res[index]+param > 255: 
                res[index] += param
    return tuple(res)
