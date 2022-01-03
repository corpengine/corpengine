from ...CORPEngine.objects.globalScript import GlobalScript

class CameraControlScript(GlobalScript):
    def __init__(self, parent):
        super().__init__(parent)
    
    def update(self, dt):
        game = self.getGameService()
        workspace = game.getService('Workspace')
        currentCamera = workspace.currentCamera
        input = game.getService('UserInputService')

        speed = 4
        if currentCamera != None:
            currentCamera.position[0] += input.isKeyPressed('right_arrow')*speed*dt + input.isKeyPressed('left_arrow')*-speed*dt
            currentCamera.position[1] += input.isKeyPressed('down_arrow')*speed*dt + input.isKeyPressed('up_arrow')*-speed*dt
