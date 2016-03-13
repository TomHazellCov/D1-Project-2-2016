from entities import *


class Map:

    def __init__(self, game, filename):
        self.game = game
        self.gridsize_x = 24
        self.gridsize_y = 18
        self.nodesize_x = 1.0/24.0
        self.nodesize_y = 1.0/18.0
        self.entities = []
        self.items = []
        self.collisionmap = [[0 for y in range(self.gridsize_y+1)] for x in range(self.gridsize_x+1)]

        background = Entity(0.5,0.5,1)
        background.addToLayout(self.game.gameScreen)

        self.loadFromFile(filename)

    def loadFromFile(self, filename):
        """
        :param filename: name of the file from which to load the map from
        :return: nothing
        """
        # read map data, convert it to int list
        file = open(filename)
        data = file.read()
        data = data.replace('\n', ' ')
        data = [int(x) for x in data.split(' ')]

        for y in range(self.gridsize_y):
            for x in range(self.gridsize_x):
                id = int(data.pop(0))
                if id != 0:
                    self.add_map_object(x, y, id)

    def add_item(self, grid_x, grid_y, entity_id):
        """
        Add item to the map
        :param grid_x: item x position in grid
        :param grid_y: item y position in grid
        :param entity_id: id of the entity
        :return: nothing
        """
        self.add_entity(grid_x*self.nodesize_x, grid_y*self.nodesize_y, entity_id, self.items)

    def add_map_object(self, grid_x, grid_y, entity_id):
        self.add_entity(grid_x*self.nodesize_x, grid_y*self.nodesize_y, entity_id, self.entities)

    def create_collision_map(self):
        for y in range(self.gridsize_y):
            for x in range(self.gridsize_x):
                node_bounds = Rectangle((x*self.nodesize_x)+(self.nodesize_x/2.0),(y*self.nodesize_y)+(self.nodesize_y/2.0),self.nodesize_x*0.9,self.nodesize_y*0.9)

                for entity in self.entities:
                    if node_bounds.overlaps(entity.bounds):
                        self.collisionmap[x][y] = 1

                print(self.collisionmap[x][y], end='')
            print('')


        return self.collisionmap

    def debug(self):
        for i in self.entities:
            print(i)

    def remove_item(self, item):
        for i, o in enumerate(self.items):
            if o == item:
                del self.items[i]
                break

        self.game.gameScreen.remove_widget(item.sprite)

    def world_to_grid(self, x, y):
        return Vector(x*self.gridsize_x, y*self.gridsize_y)

    def add_entity(self, x, y, id, list):
        entity = Entity(x+self.nodesize_x/2.0, y+self.nodesize_y/2.0,  id)
        list.append(entity)
        entity.addToLayout(self.game.gameScreen)
