from settingspanel import SettingsPanel
from items import ItemManager
from kivy.uix.floatlayout import FloatLayout
from sortingmanager import SortingManager
from pathfinding import *
from settings import *
from random import random
from entities import *
from map import *
from globals import *
from kivy.core.window import Window
from soundmanager import *
from math import *

class Game:
    def __init__(self):
        """
        Initializes all systems, prepares the game data.
        :return:
        """
        self.picked_items = []
        self.entities = []
        self.settings = Settings()
        self.itemManager = ItemManager("../Databases/items.db")
        self.sortingManager = SortingManager(self.settings)
        self.settingsPanel = SettingsPanel(self)
        self.soundmanager = SoundManager()
        self.gameScreen = FloatLayout(size_hint = (GAME_SCREEN_WIDTH/SCREEN_WIDTH, 1.00))
        self.map = Map(self,"../Databases/map.txt")
        self.pathfinding = Pathfinding(self.map.create_collision_map())

        self.robot = Robot(0.5+self.map.nodesize_x/2.0,0.5+self.map.nodesize_y/2.0)
        self.robot.addToLayout(self.gameScreen)
        self.running = False
        self.time = 0
        Window.size = (SCREEN_WIDTH, SCREEN_HEIGHT)

    def start(self):
        """
        This gets called after user clicks "START" in Settings panel
        Initializes and sets all variables needed for the main game loop
        :return:
        """
        self.running = True
        self.picked_items = []
        #remove all previous items (if the game was ran before)
        for item in self.map.items:
            self.map.remove_item(item)

        self.add_items()
        self.closest_item = None
        self.path = self.build_path()
        self.node_id = 0

    def update(self, dt):
        """
        Main game loop, this is where game logic sits
        :param dt: delta time (duration of the frame in seconds)
        :return:
        """
        if(self.running == True):
            self.settings.time
            self.time += dt

            # if time has run out
            if self.time >=  self.settings.time:
                self.end()

            # if all the items are picked
            if len(self.map.items) == 0:
                self.end()

            if(self.robot.moving == False):

                # if robot traveled through the path
                if(len(self.path) == 0):
                    self.end()
                else:
                    # if not, more robot to the next pathfinding node, and increment the node_id varialbe
                    node = self.path[self.node_id]
                    self.robot.moveTo((self.path[self.node_id].x/self.map.gridsize_x)+self.map.nodesize_x/2.0,
                                      (self.path[self.node_id].y/self.map.gridsize_y)+self.map.nodesize_y/2.0)
                    self.node_id += 1

            self.robot.update(dt)
            self.update_pick_item()

    def end(self):
        # called when game should be stopped
        self.running = False
        self.settingsPanel.show_results()

    def update_pick_item(self):
        """
            checks whether robot is colliding with any of the items in the map, if so,
            append it to list of picked items and remove it from map
        """
        for item in self.map.items:
            item_point = Rectangle(item.bounds.position.x,item.bounds.position.y,0.01,0.01)
            if(self.robot.bounds.overlaps(item_point)):
                self.picked_items.append(item)
                self.map.remove_item(item)


    def build_path(self):
        """
            builds a path for the robot to get ALL the items contained in the map
            :return built path
        """
        totalPath = []
        start = Node(int(self.robot.bounds.position.x*self.map.gridsize_x),
                     int(self.robot.bounds.position.y*self.map.gridsize_y))
        for item in self.map.items:
            x = int(item.bounds.position.x*self.map.gridsize_x)
            y = int(item.bounds.position.y*self.map.gridsize_y)
            destination = Node(x,y)
            path = self.pathfinding.astar(start,destination)
            start = Node(x,y)

            for n in path:
                totalPath.append(n)

        return totalPath

    def add_items(self):
        """
            Adds items selected in the Settings Panel to the game map
        :return:
        """
        items = self.settingsPanel.getSelectedItems()
        itemsleft = len(items)
        collision_map = self.map.create_collision_map()
        while(itemsleft > 0):
            randx = int((self.map.gridsize_x)*random())
            randy = int((self.map.gridsize_y)*random())

            if(collision_map[randx][randy] == 0):
                item = items.pop()
                itemsleft = len(items)
                self.map.add_item(randx,randy,item)

    def find_closest_item(self):
        """
            Finds closest item from to the robot
        :return:
        """
        closest = self.map.items[0]
        for item in self.map.items:
            distance = item.bounds.position.distance(self.robot.bounds.position)
            closestDistance = closest.bounds.position.distance(self.robot.bounds.position)
            if(distance < closestDistance):
                closest = item

        return closest

    def collidesWithEntities(self, entity):
        """
            checkes wheter entity collides with any other entity in the map
        :param item:
        :return:
        """
        for e in self.entities:
            if(e.bounds.intersects(entity.bounds)):
                return True
        return False

    def addEntity(self, entity):
        """
            adds entity to the screen
        """
        self.entities.append(entity)
        entity.addToLayout(self.gameScreen)
