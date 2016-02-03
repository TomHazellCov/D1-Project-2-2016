"""
	Rectangle.py : class representing a Rectangle.
	Programmed by: Edvinas Kilbauskas


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
	along with BargainHunt.  If not, see <http://www.gnu.org/licenses/>.
    
"""

from kivy.vector import Vector

class Rectangle:
	""" IMPORTANT: Use given methods to change attributes, do NOT change directly. """
	
	def __init__(self, x,y,width,height, centered = False):
		self.bottomLeft = Vector(0,0)
		self.topRight = Vector(0,0)
		self.size = Vector(width,height)
		self.center = Vector(0,0)
		self.top = 0
		self.bottom = 0
		self.left = 0
		self.right = 0
		self.setPosition(x,y,centered)
		
	def recalculatePoints(self):
		"""	Recalculates points based on bottomLeft and size attributes """
		self.topRight = self.bottomLeft + self.size
		self.center = Vector(self.bottomLeft + (self.size/2))
		self.top = self.topRight.y
		self.right = self.topRight.x
		self.bottom = self.bottomLeft.y
		self.left = self.bottomLeft.x
		
	def move(self, x,y):
		self.bottomLeft += Vector(x,y)
		self.recalculatePoints()
		
	def setPosition(self, x,y, centered = False):
		"""	Sets position and recalculates points, if centered = True then x,y will be center of the rectangle,
			otherwise, x,y will be bottomLeft """
			
		if(centered == True):
			self.bottomLeft = Vector(x,y) - (self.size/2)
		else:
			self.bottomLeft = Vector(x,y)
		
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
			
		return False
	
	def collided(self,other):
		pass
	
	def __str__(self):
		return "BottomLeft: " + self.bottomLeft + '\n' + \
			"TopRight: " + self.topRight + '\n' + \
			"Center: " + self.center + '\n' + \
			"Size: " + self.size + '\n'
