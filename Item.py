from Entity import Entity
from Sprite import Sprite
class Item(Entity):
	sprite = Sprite("Assets/fish.png")
	
	def __init__(self, id, name, type, price, qty, x, y, wanted):
		super(Item,self).__init__(x,y, self.sprite)
		self.id = id
		self.name = name
		self.type = type
		self.itemPrice = price
		self.qty = qty
		self.wanted = wanted
	
	def __str__(self):
		return "Name: " + self.name + ", X: " + str(self.bounds.bottomLeft.x) + ", Y: " + str(self.bounds.bottomLeft.y)

	def __eq__(self, other): 
		return self.__dict__ == other.__dict__