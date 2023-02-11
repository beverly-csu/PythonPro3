KEY_CHANGE_CAMERA = 'c'


class Hero:
    def __init__(self, pos, land):
        self.land = land
        self.hero = loader.loadModel('teapot')
        self.hero.setPos(pos)
        self.hero.setColor((0, 1, 0, 1))
        self.hero.reparentTo(render)
        self.cameraBind()
        self.acceptEvents()
        
    def cameraBind(self):
        base.disableMouse()
        base.camera.setH(180)
        base.camera.reparentTo(self.hero)
        base.camera.setPos(0, 0, 1.5)
        self.cameraOn = True

    def cameraUp(self):
        pos = self.hero.getPos()
        base.mouseInterfaceNode.setPos(-pos[0], -pos[1], -pos[2] - 3)
        base.camera.reparentTo(render)
        base.enableMouse()
        self.cameraOn = False

    def cameraChange(self):
        if self.cameraOn:
            self.cameraUp()
        else:
            self.cameraBind()

    def acceptEvents(self):
        base.accept(KEY_CHANGE_CAMERA, self.cameraChange)
