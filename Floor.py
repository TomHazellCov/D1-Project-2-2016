from Sprite import Sprite
from Entity import Entity

class Floor(Entity):
	sprite = Sprite("Assets/floor.png", True)
	def __init__(self):
		super(Floor,self).__init__(0, 0, self.sprite)
		self.sprite.setSize(0.75,1)