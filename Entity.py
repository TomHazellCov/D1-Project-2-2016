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
<<<<<<< HEAD
		
=======
		
class Background(Entity):
	width = 800
	height = 600
	
	def __init__(self):
		super(Background,self).__init__(0, 0, self.width, self.height, Sprite(self.width,self.height,"Assets/background.jpeg"))
		self.size = Vector(self.width, self.height)	
	
class Item(Entity):
	width = 64
	height = 64

	def __init__(self, name, type, price, qty):
		self.name = name
		self.type = type
		self.price = price
		self.qty = qty
		self.bounds = Rectangle(0,0,64,64)

	def __str__(self):
		return "Name: " + self.name + '\n' + "Type: " + self.type + '\n' + "Price: " + str(self.price) + '\n' + "Qty: " + str(self.qty)
		
class Item:
	width = 64
	height = 64
	
	def __init__(self, itemNumber, itemName, itemType, itemPrice, itemQuantity, postionX, postitionY, itemIsWanted):
		#super(Item,self).__init__(positionX, positionY, self.width, self.height, Sprite(self.width, self.height, "Assets/fish.png"))
		self.itemNumber = itemNumber
		self.itemName = itemName
		self.itemType = itemType
		self.itemPrice = itemPrice
		self.itemQuantity = itemQuantity
		self.postionX = postionX
		self.postitionY = postitionY
		self.itemIsWanted = itemIsWanted

	def __eq__(self, other): 
		# whoever did this, is genius
		return self.__dict__ == other.__dict__
		
>>>>>>> bb69b7eb2de57ca9757a6f57f56a1ef424470237
