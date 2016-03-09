from SettingsPanel import SettingsPanel
from ItemManager import ItemManager
from kivy.uix.floatlayout import FloatLayout
from sound_manager import SortingManager
from Pathfinding import *
from Entities import *
from Settings import *
from random import random
from Map import Map
from kivy.uix.scatter import *
from Global import *

class Game:
    def __init__(self):
        self.entities = []
        self.items = []

        self.pathFinding = Pathfinding(self.entities)
        self.settings = Settings()
        self.itemManager = ItemManager("Databases/VRBH.db")
        self.sortingManager = SortingManager(self.settings)
        self.settingsPanel = SettingsPanel(self)
        """self.gameScreen = Scatter(do_rotation=False,
                                  do_scale=False,
                                  do_translation_y=False,
                                  do_translation_x=False,
                                  scale_min = 1,
                                  scale_max = 1,
                                  size_hint = (0.75, 1.00))"""
        self.gameScreen = FloatLayout(size_hint = (0.75, 1.00))

        self.map = Map(self,"Databases/map.txt")
        # add background
        self.map.add_map_object(0,0,0)

        #self.robot = RobotEntity(0.5,0.5)
        #self.robot.addToLayout(self.gameScreen)

        self.running = False

    def start(self):
        self.running = True
        items = self.settingsPanel.getSelectedItems()
        for item in items:
            item.setPosition(random()-64/GAME_SCR_WIDTH, random()-64/GAME_SCR_HEIGHT)
            if(self.collidesWithEntities(item)):
                self.items.append(item)
                item.addToLayout(self.gameScreen)

    def collidesWithEntities(self, item):
        for entity in self.entities:
            if(entity.bounds.intersects(item.bounds)):
                return True

        return False



    def addEntity(self, entity):
        self.entities.append(entity)
        entity.addToLayout(self.gameScreen)

    def update(self, dt):
        if(self.running == True):
            pass


    def draw(self, dt):
        pass
