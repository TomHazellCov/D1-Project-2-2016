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

from kivy.uix.image import Image
from kivy.vector import Vector

class Sprite(Image):
	def __init__(self, width, height, source):
		super(Image,self).__init__(size = Vector(width,height), source = source)
 
class Entity:
	def __init__(self,x, y, width, height, sprite, centered = False):
		self.sprite = sprite
		self.bounds = Rectangle(x,y,width,height, centered)
		
	def addToLayout(self, layout):
		layout.add_widget(self.sprite)
	
	def setTexture(self, texture):
		self.texture = texture
		
	def setPosition(self, pos):
		self.bounds.setPosition(*pos)
		# for kivy graphics API
		self.image.pos = Vector(*pos)