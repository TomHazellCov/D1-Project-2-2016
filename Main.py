"""
	Main.py : BargainHunt game
	Credits: Edvinas Kilbauskas

	This file is part of BargainHunt.

	BargainHunt is free software: you can redistribute it and/or modify
	it under the terms of the GNU General Public License as published by
	the Free Software Foundation, either version 3 of the License, or
	(at your option) any later version.

	BargainHunt is distributed in the hope that it will be useful,
	but WITHOUT ANY WARRANTY; without even the implied warranty of
	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
	GNU General Public License for more details.

	You should have received a copy of the GNU General Public License
	along with BargainHunt. If not, see <http://www.gnu.org/licenses/>.
"""

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.vector import Vector
from kivy.clock import Clock
from kivy.core.window import Window
from ItemManager import ItemManager
from Rectangle import Rectangle
from Entity import *
from random import random
from SettingsPanel import SettingsPanel
from kivy.uix.button import *
from Floor import Floor

class Robot:
	def __init__(self, position):
		pass
		
""" Main game class with game loop """

class GameScreen(FloatLayout):
	
	def __init__(self, app):
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
	
class BargainHuntApp(App):
	def build(self):
		self.root = GameScreen(self)
		Clock.schedule_interval(self.root.update, 1.0 / 60.0)
		return self.root

if __name__ == '__main__':
	BargainHuntApp().run()