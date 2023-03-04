from direct.showbase.ShowBase import ShowBase
from mapmanager import Mapmanager
from hero import Hero

class Game(ShowBase):
    def __init__(self):
        super().__init__()
        self.land = Mapmanager()
        x, y = self.land.loadLand('map.txt')
        player = Hero((0, 0, 0), self.land)
        base.camLens.setFov(90)
        self.land.saveMap()


game = Game()
game.run()