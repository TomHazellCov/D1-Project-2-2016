from Sprite import Sprite
from Entity import Entity

class RobotEntity(Entity):
	def __init__(self, x, y):
		super(RobotEntity, self).__init__(0,0, Sprite("Assets/barrel.png", True))
		self.sprite.setSize(0.1,0.1)

class FloorEntity(Entity):
	def __init__(self):
		super(FloorEntity,self).__init__(0, 0, Sprite("Assets/floor.png", True))
		self.sprite.setSize(1,1)

class BarrelEntity(Entity):
	def __init__(self, x, y):
		super(BarrelEntity,self).__init__(x, y, Sprite("Assets/barrel.png", True))
		self.sprite.setSize(0.1, 0.1)
		
class BoxEntity(Entity):
	def __init__(self, x, y):
		super(BoxEntity,self).__init__(x, y, Sprite("Assets/large_crate.png", True))
		self.sprite.setSize(0.1, 0.1)
		
class DumpEntity(Entity):
	def __init__(self, x, y):
		super(DumpEntity, self).__init__(x, y, Sprite("Assets/dump.png", True))
		self.sprite.setSize(0.1, 0.1)
		
class ForkliftEntity(Entity):
	def __init__(self, x, y):
		super(ForkliftEntity, self).__init__(x, y, Sprite("Assets/forklift.png", True))
		self.sprite.setSize(0.1, 0.1)