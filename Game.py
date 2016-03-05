from SettingsPanel import SettingsPanel
from ItemManager import ItemManager
from kivy.uix.floatlayout import FloatLayout
from SortingManager import SortingManager
from Entities import *
from Settings import *
from random import random

class Game:
	def __init__(self):
		self.entities = []
		self.settings = Settings()
		self.itemManager = ItemManager("Databases/items.db")
		self.sortingManager = SortingManager(self.settings)
		self.settingsPanel = SettingsPanel(self)
		self.gameScreen = FloatLayout(size_hint = (0.75, 1.00))
		
		self.running = False
		
		self.createMap()
		
		
	def start(self):
		self.running = True
		items = self.settingsPanel.getSelectedItems()
		for item in items:
			
			print(item.bounds)
			self.addEntity(item)
			
	def createMap(self):
		self.addEntity(FloorEntity())
		self.addEntity(BarrelEntity(0,0))
		self.addEntity(BarrelEntity(0.12,0.02))
		self.addEntity(BarrelEntity(0,0))
			
	def addEntity(self, entity):
		self.entities.append(entity)
		entity.addToLayout(self.gameScreen)
		
	def update(self, dt):
		pass
	
	def draw(self, dt):
		pass
		