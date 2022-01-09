from ..coreContent import openErrorWindow

class SoundService(object):
    def __init__(self, parent):
        self.parent = parent
        self.name = 'SoundService'
        self.type = 'SoundService'
    
    def playFile(self, name):
        assets = self.parent.getService('Assets')
        try:
            assets.sounds[name].play()
        except Exception:
            openErrorWindow(f'No sound file named "{name}".', self.parent.parent)
    
    def stopFile(self, name):
        assets = self.parent.getService('Assets')
        try:
            assets.sounds[name].stop()
        except Exception:
            openErrorWindow(f'No sound file named "{name}".', self.parent.parent)

    def setVolume(self, name, value):
        assets = self.parent.getService('Assets')
        try:
            assets.sounds[name].set_volume(value)
        except Exception:
            openErrorWindow(f'Invalid value for volume or file not found.', self.parent.parent)
    
    def getVolume(self, name):
        assets = self.parent.getService('Assets')
        try:
            return assets.sounds[name].get_volume()
        except Exception:
            openErrorWindow('Sound file not found.', self.parent.parent)
    
    def getLength(self, name):
        assets = self.parent.getService('Assets')
        try:
            return assets.sounds[name].get_length()
        except Exception:
            openErrorWindow(f'Invalid value for volume or file not found.', self.parent.parent)
