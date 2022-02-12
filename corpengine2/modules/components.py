from pyray import Vector2

class Script(object):
    def __init__(self, parent):
        self.parent = parent
        self.type = "ScriptComponent"

class Transform(object):
    def __init__(self, parent, scale=1, rotation=0, position=Vector2(0, 0)):
        self.parent = parent
        self.type = "TransformComponent"
        self.scale = scale
        self.rotation = rotation
        self.position = position

class Texture(object):
    def __init__(self, parent, texture=None):
        self.parent = parent
        self.type = "TextureComponent"
        self.texture = texture
