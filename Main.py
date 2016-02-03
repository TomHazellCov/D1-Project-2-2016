from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.core.image import Texture
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import NumericProperty, ReferenceListProperty,\
    ObjectProperty
    
from kivy.vector import Vector
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.lang import Builder

from Rectangle import Rectangle
	
class Background(Image):
	pass

class Entity(Image):
	
	def __init__(self,x, y, width, height):
		self.bounds = Rectangle(x,y,width,height)
		
		super(Image,self).__init__()
		
	
	
class Item(Image):
	
	def __init__(self, name, type, price, qty, **kwargs):
		self.name = name
		self.type = type
		self.price = price
		self.qty = qty
		self.bounds = Rectangle(0,0,64,64)
		
		super(Item,self).__init__(**kwargs)
	
	def setTexture(self, texture):
		self.texture = texture
			
	def setPosition(self, pos):
		self.bounds.setPosition(*pos)
		# for kivy graphics API
		self.pos = Vector(*pos)

	def __str__(self):
		return "Name: " + self.name + '\n' + "Type: " + self.type + '\n' + "Price: " + str(self.price) + '\n' + "Qty: " + str(self.qty)
		
class Robot:
	def __init__(self, position):
		pass
		
class BargainHunt(FloatLayout):
	items = []
	def __init__(self, app, **kwargs):
		super(BargainHunt,self).__init__(**kwargs)
		self.app = app
		self.add_widget(Background())
		
	def addEntity(self,entity):
		pass
	
	def update(self, dt):
		pass
	
	def on_touch_down(self, touch):
		self.add_widget(Item(name="Name",type="Type",price=199.99,qty=1,source="Assets/fish.png"))

class MainApp(App):
	def build(self):	
		self.root = BargainHunt(self)
		Clock.schedule_interval(self.root.update, 1.0 / 60.0)
		return self.root


if __name__ == '__main__':
	MainApp().run()
	
	
	
	
	
	
	
	
	
