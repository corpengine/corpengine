from ..CORPEngine.objects.camera import Camera

class MainCamera(Camera):
    def __init__(self, parent):
        super().__init__(parent)
        self.name = 'MainCamera'
        self.position = [55, 12]
