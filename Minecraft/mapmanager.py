class Mapmanager:
    def __init__(self):
        self.model = 'block.egg'
        self.texture = 'block.png'
        self.colors = [
            (1, 0, 0, 1), (0, 1, 0, 1), (0, 0, 1, 1),
            (1, 1, 0, 1), (0, 1, 1, 1), (1, 1, 1, 1)
        ]
        self.startNew()

    def startNew(self):
        self.land = render.attachNewNode('land')

    def addBlock(self, position):
        block = loader.loadModel(self.model)
        texture = loader.loadTexture(self.texture)
        block.setTexture(texture)
        color = self.getColor(position[2])
        block.setColor(color)
        block.setPos(position)
        block.reparentTo(self.land)

    def clear(self):
        self.land.removeNode()
        self.startNew()

    def loadLand(self, filename):
        self.clear()
        with open(filename) as file:
            y = 0
            for line in file:
                x = 0
                line = line.split()
                for z in line:
                    for z0 in range(int(z) + 1):
                        self.addBlock((x, y, z0))
                    x += 1
                y += 1
    
        return x, y

    def getColor(self, z):
        if z < len(self.colors):
            return self.colors[z]
        else:
            return self.colors[-1]