from ItemManager import ItemManager
from kivy.uix.floatlayout import FloatLayout
from random import random

class GameScreen(FloatLayout):
	
	def __init__(self, root):
		super(GameScreen,self).__init__()
		
		# ADD BACKGROUND
		self.floor = Floor()
		self.floor.addToLayout(self)
		
		# LOAD ITEMS
		self.itemManager = ItemManager("Databases/sql.db")
		self.items = self.itemManager.getItems()
		
		self.settingsPanel = SettingsPanel(self)
		
	def loadItems(self):
		pass
	
	def update(self, dt):
		pass
	
	def on_touch_down(self, touch):
		super(FloatLayout,self).on_touch_down(touch)