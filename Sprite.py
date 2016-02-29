from kivy.uix.image import Image
from kivy.vector import Vector
from kivy.properties import NumericProperty, ReferenceListProperty

class Sprite(Image):
	def __init__(self, source, stretch = False):
		super(Sprite,self).__init__(source = source)
		if(self.texture == None):
			super(Sprite,self).__init__(source = "Assets/default.png")
		
		self.allow_stretch = stretch
		# we don't want to keep ratio if it's stretched
		self.keep_ratio = not stretch
		
	# sets size acording to window's dimention. Takes float in range [0,1)
	def setSize(self, width, height):
		self.size_hint = (width,height)
		
	def setPosition(self, x, y):
		self.pos = (x,y)
		self.pos_hint = {'x' : x, 'y' : y}