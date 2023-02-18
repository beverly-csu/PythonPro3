KEY_CHANGE_CAMERA = 'c'
KEY_FORWARD = 'w'
KEY_BACK = 's'
KEY_LEFT = 'a'
KEY_RIGHT = 'd'

KEY_TURN_LEFT = 'n'
KEY_TURN_RIGHT = 'm'

KEY_UP = 'e'
KEY_DOWN = 'q'

KEY_BUILD = 'b'
KEY_DESTROY = 'v'


class Hero:
    def __init__(self, pos, land):
        self.land = land
        self.mode = True
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

    def check_dir(self, angle):
        if angle >= 0 and angle <= 20:
            return (0, -1)
        elif angle <= 65:
            return (1, -1)
        elif angle <= 110:
            return (1, 0)
        elif angle <= 155:
            return (1, 1)
        elif angle <= 200:
            return (0, 1)
        elif angle <= 245:
            return (-1, 1)
        elif angle <= 290:
            return (-1, 0)
        elif angle <= 335:
            return (-1, -1)
        else:
            return (0, -1)

    def look_at(self, angle):
        x_from = int(self.hero.getX())
        y_from = int(self.hero.getY())
        z_from = int(self.hero.getZ())

        dx, dy = self.check_dir(angle)

        x_to = x_from + dx
        y_to = y_from + dy

        return (x_to, y_to, z_from)

    def just_move(self, angle):
        pos = self.look_at(angle)
        self.hero.setPos(pos)

    def move_to(self, angle):
        if self.mode:
            self.just_move(angle)

    def forward(self):
        angle = self.hero.getH() % 360
        self.move_to(angle)

    def left(self):
        angle = (self.hero.getH() + 90) % 360
        self.move_to(angle)
    
    def right(self):
        angle = (self.hero.getH() + 270) % 360
        self.move_to(angle)
    
    def back(self):
        angle = (self.hero.getH() + 180) % 360
        self.move_to(angle)

    def turn_left(self):
        heading = self.hero.getH()
        heading += 10
        self.hero.setH(heading)
    
    def turn_right(self):
        heading = self.hero.getH()
        heading -= 10
        self.hero.setH(heading)

    def up(self):
        if self.mode:
            z = self.hero.getZ()
            self.hero.setZ(z + 1)

    def down(self):
        if self.mode:
            z = self.hero.getZ()
            self.hero.setZ(z - 1)

    def acceptEvents(self):
        base.accept(KEY_CHANGE_CAMERA, self.cameraChange)

        base.accept(KEY_DOWN, self.down)
        base.accept(KEY_UP, self.up)

        base.accept(KEY_TURN_LEFT, self.turn_left)
        base.accept(KEY_TURN_LEFT + '-repeat', self.turn_left)
        base.accept(KEY_TURN_RIGHT, self.turn_right)
        base.accept(KEY_TURN_RIGHT + '-repeat', self.turn_right)

        base.accept(KEY_FORWARD, self.forward)
        base.accept(KEY_FORWARD + '-repeat', self.forward)
        base.accept(KEY_BACK, self.back)
        base.accept(KEY_BACK + '-repeat', self.back)
        base.accept(KEY_LEFT, self.left)
        base.accept(KEY_LEFT + '-repeat', self.left)
        base.accept(KEY_RIGHT, self.right)
        base.accept(KEY_RIGHT + '-repeat', self.right)