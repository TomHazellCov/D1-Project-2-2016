from SettingsPanel import SettingsPanel
from ItemManager import ItemManager
from kivy.uix.floatlayout import FloatLayout
from Entities import *
from Settings import *

class Game:
	def __init__(self):
		self.entities = []
		self.itemManager = ItemManager("Databases/sql.db")
		self.settings = Settings()
		self.gameScreen = FloatLayout(size_hint = (0.75, 1.00))
		self.settingsPanel = SettingsPanel(self)
		
		self.createMap()
		
		
	def start(self):
		pass
		
	def createMap(self):
		self.addEntity(FloorEntity())
		self.addEntity(BarrelEntity(0,0))
		self.addEntity(BarrelEntity(0.12,0.02))
		self.addEntity(BarrelEntity(0,0))
		
		for entity in self.entities:
			entity.addToLayout(self.gameScreen)
		
	def addEntity(self, entity):
		self.entities.append(entity)
		
	def update(self, dt):
		pass
	
	def draw(self, dt):
		pass
		