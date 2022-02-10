from pyray import Vector2

class ScriptComponent(object):
    def __init__(self, parent):
        self.parent = parent
        self.type = "ScriptComponent"

class TransformComponent(object):
    def __init__(self, parent):
        self.parent = parent
        self.type = "TransformComponent"
        self.position = Vector2(0, 0)
        self.scale = 1
        self.rotation = 0

class TextureComponent(object):
    def __init__(self, parent, texture=None):
        self.parent = parent
        self.type = "TextureComponent"
        self.texture = texture
