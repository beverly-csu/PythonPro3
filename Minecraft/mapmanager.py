class Mapmanager:
    def __init__(self):
        self.model = 'block.egg'
        self.texture = 'block.png'
        self.color = (1, 0, 0, 1)
        self.startNew()
        self.addBlock((0, 10, 0))
        self.addBlock((1, 10, 0))

    def startNew(self):
        self.land = render.attachNewNode('land')

    def addBlock(self, position):
        block = loader.loadModel(self.model)
        texture = loader.loadTexture(self.texture)
        block.setTexture(texture)
        block.setColor(self.color)
        block.setPos(position)
        block.reparentTo(self.land)
