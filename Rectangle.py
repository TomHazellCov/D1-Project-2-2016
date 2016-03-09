"""
	Rectangle.py : class representing a Rectangle.
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

class Rectangle:
	""" IMPORTANT: Use given methods to change attributes, do NOT change directly. """
	
	def __init__(self, x,y,width,height):
		self.position = Vector(x, y)
		self.size = Vector(width,height)
		self.center = Vector(x+width/2.0,y+height/2.0)
		self.top = self.center.y + self.size.y/2.0
		self.right = self.center.x + self.size.x/2.0
		self.bottom = self.center.y - self.size.y/2.0
		self.left = self.center.x - self.size.x/2.0
		
	def recalculatePoints(self):
		"""	Recalculates points based on bottomLeft and size attributes """
		self.center = Vector(self.position + (self.size / 2))
		self.top = self.center.y + self.size.y/2
		self.right = self.center.x + self.size.x/2
		self.bottom = self.center.y - self.size.y/2
		self.left = self.center.x - self.size.x/2
		
	def move(self, x,y):
		self.position += Vector(x, y)
		self.recalculatePoints()
		
	def setPosition(self, x, y):
		self.position = Vector(x, y)
		self.recalculatePoints()
		
	def setSize(self,width,height):
		self.size = Vector(width,height)
		self.recalculatePoints()
		
	def set(self,x,y,width,height, centered = False):
		self.setPosition(x,y, centered)
		self.setSize(width,height)
		self.recalculatePoints()
	
	def pointInside(self,x,y):
		if((x > self.left and x < self.right) and (y > self.top and y < self.bottom)):
			return True
		else:
			return False
	
	def intersects(self,other):
		if(self.left < other.right and self.right > other.left and self.top > other.bottom and self.bottom < other.top):
			return True
		else:
			return False

		
	def __str__(self):
		return "X: " + str(self.center.x) + "Y: " + str(self.center.y)
