from Entities import *
from Global import *

class Map:
    def __init__(self, game, filename):
        self.game = game
        self.entities = []
        self.items = []
        self.gridsize = 18
        self.nodesize = 1.0/self.gridsize
        self.loadFromFile(filename)

    def loadFromFile(self, filename):
        # read map data, convert it to int list
        file = open(filename)
        data = file.read()
        data = data.replace('\n', ' ')
        data = [int(x) for x in data.split(' ')]

        for y in range(self.gridsize, 0, -1):
            for x in range(self.gridsize):
                id = int(data.pop(0))+1
                print(id)
                if id != 0:
                    self.add_map_object(x, y, id-1)

    def add_item(self, x, y, entity_id):
        self.add_entity(x, y, entity_id, self.items)

    def add_map_object(self, x, y, entity_id):
        self.add_entity(x, y, entity_id, self.entities)

    def add_entity(self, x, y, id, container):
        entity = Entity(x/GAME_SCR_WIDTH, y/GAME_SCR_WIDTH, id)
        entity.move(0, -self.nodesize/GAME_SCR_HEIGHT)
        container.append(entity)
        entity.addToLayout(self.game.gameScreen)

