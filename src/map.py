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
                # go through the data, and add appropriate entities to the map
                id = int(data.pop(0))
                if id != 0:
                    self.add_map_object(x, y, id)

    def add_item(self, grid_x, grid_y, item):
        item.setPosition((grid_x*self.nodesize_x)+self.nodesize_x/2.0, (grid_y*self.nodesize_y)+self.nodesize_y/2.0)
        self.items.append(item)
        item.addToLayout(self.game.gameScreen)

    def add_map_object(self, grid_x, grid_y, entity_id):
        entity = Entity((grid_x*self.nodesize_x)+self.nodesize_x/2.0, (grid_y*self.nodesize_y)+self.nodesize_y/2.0,  entity_id)
        self.entities.append(entity)
        entity.addToLayout(self.game.gameScreen)

    def create_collision_map(self):
        """
            Creates a 2D collision map for the A* sorting algorithm
        :return: 2D (size [gridsize_x][gridsize_y]) list with integers.
        """
        collisionmap = [[0 for y in range(self.gridsize_y+1)] for x in range(self.gridsize_x+1)]
        for y in range(self.gridsize_y):
            for x in range(self.gridsize_x):
                node_bounds = Rectangle((x*self.nodesize_x)+(self.nodesize_x/2.0),(y*self.nodesize_y)+(self.nodesize_y/2.0),self.nodesize_x*0.9,self.nodesize_y*0.9)

                for entity in self.entities:
                    if node_bounds.overlaps(entity.bounds):
                        collisionmap[x][y] = 1

                print(collisionmap[x][y], end='')
            print('')

        return collisionmap

    def remove_item(self, item):
        """
            Removes an item from the map
        :param item: item to be removed
        :return: nothing
        """
        for i, o in enumerate(self.items):
            if o == item:
                del self.items[i]
                break

        # remove the visual representation of the item from the gamescreen
        self.game.gameScreen.remove_widget(item.sprite)


