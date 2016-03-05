from ItemManager import ItemManager
from kivy.uix.floatlayout import FloatLayout
from Entities import *
from random import random

class GameScreen(FloatLayout):
	
	def __init__(self, game):
		super(GameScreen,self).__init__(size_hint = (0.75, 1))
		self.game = game
		
		# ADD BACKGROUND
		self.floor = FloorEntity()
		self.floor.addToLayout(self)
		
	
	