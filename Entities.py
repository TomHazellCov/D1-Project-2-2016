from Sprite import Sprite
from Entity import Entity
from math import *

class RobotEntity(Entity):
	
	def __init__(self, x, y):
		super(RobotEntity, self).__init__(0,0, 0.1, 0.1, Sprite("Assets/barrel.png", True))
		
		
	def moveTo(self, x, y):
		pass
		
	def update(self, dt):
		pass

class FloorEntity(Entity):
	def __init__(self):
		super(FloorEntity,self).__init__(0, 0, 1,1, Sprite("Assets/floor.png", True))

class BarrelEntity(Entity):
	def __init__(self, x, y):
		super(BarrelEntity,self).__init__(x, y, 0.1, 0.1, Sprite("Assets/barrel.png", True))
		
class BigBoxEntity(Entity):
	def __init__(self, x, y):
		super(BoxEntity,self).__init__(x, y, 0.2, 0.2, Sprite("Assets/large_crate.png", True))
		
class MediumBoxEntity(Entity):
	def __init__(self, x, y):
		super(BoxEntity,self).__init__(x, y, 0.2, 0.2, Sprite("Assets/large_crate.png", True))
		
class SmallBoxEntity(Entity):
	def __init__(self, x, y):
		super(BoxEntity,self).__init__(x, y, 0.2, 0.2, Sprite("Assets/large_crate.png", True))
		
class DumpEntity(Entity):
	def __init__(self, x, y):
		super(DumpEntity, self).__init__(x, y, 0.1, 0.1, Sprite("Assets/dump.png", True))
		
class ForkliftEntity(Entity):
	def __init__(self, x, y):
		super(ForkliftEntity, self).__init__(x, y, 0.1, 0.1, Sprite("Assets/forklift.png", True))
		
class Item(Entity):

	def __init__(self, id, name, type, price, qty, x, y, wanted):
		super(Item,self).__init__(x,y, 0.3, 0.3,Sprite("Assets/dump.png"))
		self.id = id
		self.name = name
		self.type = type
		self.price = price
		self.qty = qty
		
	
	def __str__(self):
		return "Name: " + self.name + ", X: " + str(self.bounds.bottomLeft.x) + ", Y: " + str(self.bounds.bottomLeft.y)

	def __eq__(self, other): 
		return self.__dict__ == other.__dict__