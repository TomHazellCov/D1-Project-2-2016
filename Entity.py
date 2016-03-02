"""
	Entity.py : classes representing an Entity.
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

from kivy.vector import Vector
from Rectangle import Rectangle
from Error import *
from Sprite import Sprite

class Entity:
	def __init__(self,x, y, sprite = None):
		self.sprite = sprite
		if(self.sprite != None and sprite != None):
			self.sprite = sprite
		else:
			self.sprite = Sprite("Assets/default.png")

		self.bounds = Rectangle(x,y,sprite.texture.size[0],sprite.texture.size[1])
		self.setPosition(x,y)
		
	def addToLayout(self, layout):
		layout.add_widget(self.sprite)

	def setSprite(self, sprite):
		self.sprite = sprite
		
	def setPosition(self, x, y):
		self.bounds.setPosition(x,y)
		self.sprite.setPosition(x,y)
		