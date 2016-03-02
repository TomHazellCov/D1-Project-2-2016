 from Sprite import Sprite
from Entity import Entity

class Floor(Entity):
	def __init__(self):
		super(Floor,self).__init__(0, 0, Sprite("Assets/floor.png", True))
		self.sprite.setSize(0.75,1)

class Barrel(Entity):
	def __init__(self, x, y):
		super(Floor,self).__init__(x, y, Sprite("Assets/floor.png", True))
		