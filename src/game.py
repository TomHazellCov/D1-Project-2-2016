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
        self.picked_items = []
        self.entities = []
        self.settings = Settings()
        self.itemManager = ItemManager("../Databases/items.db")
        self.sortingManager = SortingManager(self.settings)
        self.settingsPanel = SettingsPanel(self)
        self.soundmanager = SoundManager()
        self.gameScreen = FloatLayout(size_hint = (GAME_SCREEN_WIDTH/SCREEN_WIDTH, 1.00))
        self.map = Map(self,"../Databases/map.txt")
        self.pathfinding = Pathfinding(self.map.collisionmap)
        self.robot = Robot(0.5+self.map.nodesize_x/2.0,0.5+self.map.nodesize_y/2.0)

        self.robot.addToLayout(self.gameScreen)
        self.map.debug()
        self.running = False

        Window.size = (SCREEN_WIDTH, SCREEN_HEIGHT)

    def start(self):
        self.running = True
        self.picked_items = []
        for item in self.map.items:
            self.map.remove_item(item)
        self.add_items()
        self.closest_item = None
        self.path = self.build_path()
        self.node_id = 0
        print(self.path)

    def update(self, dt):

        if(self.running == True):
            self.settings.time -= dt

            if(self.settings.time <= 0):
                self.end()
            if(len(self.picked_items) == len(self.map.items)):
                self.end()

            if(self.robot.moving == False):
                if(self.node_id >= len(self.path)):
                    self.end()
                else:
                    node = self.path[self.node_id]
                    self.robot.moveTo((self.path[self.node_id].x/self.map.gridsize_x)+self.map.nodesize_x/2.0,
                                      (self.path[self.node_id].y/self.map.gridsize_y)+self.map.nodesize_y/2.0)
                    self.node_id += 1

            self.robot.update(dt)
            self.robot.addToLayout(self.gameScreen)
            self.update_pick_item()

    def end(self):
        self.running = False

    def update_pick_item(self):
        for item in self.map.items:
            item_point = Rectangle(item.bounds.position.x,item.bounds.position.y,0.01,0.01)
            if(self.robot.bounds.overlaps(item_point)):
                self.picked_items.append(item)
                self.map.remove_item(item)


    def build_path(self):
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


    def update_path_follow(self):
        pass

    def add_items(self):
        items = self.settingsPanel.getSelectedItems()
        itemsleft = len(items)
        collision_map = self.map.create_collision_map()
        while(itemsleft > 0):
            randx = int((self.map.gridsize_x)*random())
            randy = int((self.map.gridsize_y)*random())

            if(collision_map[randx][randy] == 0):
                item = items.pop()
                itemsleft = len(items)
                self.map.add_item(randx,randy,item.id)

    def find_closest_item(self):
        closest = self.map.items[0]
        for item in self.map.items:
            distance = item.bounds.position.distance(self.robot.bounds.position)
            closestDistance = closest.bounds.position.distance(self.robot.bounds.position)
            if(distance < closestDistance):
                closest = item

        return closest

    def collidesWithEntities(self, item):
        for entity in self.entities:
            if(entity.bounds.intersects(item.bounds)):
                return True
        return False

    def addEntity(self, entity):
        self.entities.append(entity)
        entity.addToLayout(self.gameScreen)

    def draw(self, dt):
        pass
